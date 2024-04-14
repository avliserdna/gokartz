from flask import Blueprint, jsonify, session, request
from flask_login import login_required, current_user
from app.models import Transaction, db
from app.forms import TransactionForm

transaction_routes = Blueprint('transactions', __name__)

@transaction_routes.route('/')
def transactions():
  transactions = Transaction.query.all()
  return {transaction.id: transactions.to_dict() for transaction in transactions}
