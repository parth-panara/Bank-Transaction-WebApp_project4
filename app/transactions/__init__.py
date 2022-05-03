""" transactions module """
import csv
import logging
import os

from flask import Blueprint, render_template, abort, url_for,current_app

from jinja2 import TemplateNotFound


from app.db.models import Transaction
from app.transactions.forms import csv_upload



transactions = Blueprint('transactions', __name__,
                        template_folder='templates')

@transactions.route('/transactions', methods=['GET'], defaults={"page": 1})
@transactions.route('/transactions/<int:page>', methods=['GET'])

def transactions_browse(page):
    page = page
    per_page = 1000
    pagination = Transaction.query.paginate(page, per_page, error_out=False)
    data = pagination.items
    try:
        return render_template('browse_transactions.html',data=data,pagination=pagination)
    except TemplateNotFound:
        abort(404)

