"""This test the transactions"""
import pytest


from app import db
from app.db.models import Transaction, User

#adding user to test transaction database#27

@pytest.fixture
def test_user(application):
    """ setup database user and delete """

    with application.app_context():
        assert db.session.query(User).count() == 0 # pylint: disable=no-member

        # adding user
        EMAIL = 'parth@webizly.com'
        PASSWORD = 'testtest'
        user = User(EMAIL,  PASSWORD )
        db.session.add(user) # pylint: disable=no-member
        db.session.commit() # pylint: disable=no-member

        yield user

        # delete user and verify
        db.session.delete(user) # pylint: disable=no-member
        assert db.session.query(User).count() == 0 # pylint: disable=no-member
        assert db.session.query(Transaction).count() == 0 # pylint: disable=no-member


#test to check transaction database#27

def test_data_transactions(application, test_user):
    """ test basic db stuff """
    user = test_user
    assert db.session.query(Transaction).count() == 0

    # functioons addding into the database
    transactions = []
    transactions.append( Transaction(100, 'Deposit') )
    transactions.append( Transaction(20, 'Withdrawl') )

    user.transactions += transactions
    db.session.commit() # pylint: disable=no-member
    assert db.session.query(Transaction).count() == 2

    # reading the function
    trans1 = Transaction.query.filter_by(type='Deposit').first()
    assert trans1.amount == 100

    # implement the function
    trans1.amount = 200
    db.session.commit() # pylint: disable=no-member
    trans2 = Transaction.query.filter_by(amount=200).first()
    assert trans2.type == 'Deposit'

    # deleting the data
    db.session.delete(trans2)
    db.session.commit()
    assert db.session.query(Transaction).count() == 1