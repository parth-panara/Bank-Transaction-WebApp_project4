""" transactions module """
import csv
import logging
import os
from csv import DictReader
from flask import Blueprint, render_template, abort, url_for,current_app
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound

from app.db import db
from app.db.models import Transaction, User
from app.transactions.forms import csv_upload
from werkzeug.utils import secure_filename, redirect

from sqlalchemy import func

transactions = Blueprint('transactions', __name__,
                        template_folder='templates')

@transactions.route('/transactions', methods=['GET'], defaults={"page": 1})
@transactions.route('/transactions/<int:page>', methods=['GET'])

def transactions_browse(page):

    page = page
    per_page = 1000
    pagination = Transaction.query.paginate(page, per_page, error_out=False)
    data = pagination.items


    qry = db.session.query(func.sum(Transaction.amount)).group_by(Transaction.type).filter(Transaction.user_id).all()

    if qry:
        balance = qry[0][0] + qry[1][0]

        return render_template('browse_transactions.html', data=data, pagination=pagination, balance=balance)

    try:

        return render_template('browse_transactions.html',data=data, pagination=pagination)
    except TemplateNotFound:
        abort(404)




@transactions.route('/transactions/upload', methods=['POST', 'GET'])
@login_required
def transactions_upload():
    form = csv_upload()
    if form.validate_on_submit():
        log = logging.getLogger("myApp")

        filename = secure_filename(form.file.data.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        form.file.data.save(filepath)
        #user = current_user
        list_of_transactions = []
        with open(filepath, encoding="utf-8-sig" ) as file:
            csv_file = csv.DictReader(file, dialect= 'excel')
            for row in csv_file:
                list_of_transactions.append(Transaction(row['AMOUNT'],row['TYPE']))

        current_user.transactions = list_of_transactions
        db.session.commit()

        return redirect(url_for('transactions.transactions_browse'))

    try:
        return render_template('upload.html', form=form)
    except TemplateNotFound:
        abort(404)
