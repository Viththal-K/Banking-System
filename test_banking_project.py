import pytest
from banking_project import User, BankAcc

@pytest.fixture
def bank_account():
    return BankAcc("Viththal", 23, "Male")

def test_show_details(bank_account, capsys):
    bank_account.show_details()
    captured = capsys.readouterr()
    expected_output = """Personal details ->
Name: Viththal
Age: 23
Gender: Male
"""
    assert captured.out == expected_output

def test_deposit(bank_account, capsys):
    bank_account.deposit(1000)
    captured = capsys.readouterr()
    expected_output = """Deposit of $1000 successful
Updated account balance: $1000
"""
    assert captured.out == expected_output

def test_withdraw_success(bank_account, capsys):
    bank_account.deposit(1000)
    bank_account.withdraw(400)
    captured = capsys.readouterr()
    expected_output = """Deposit of $1000 successful
Updated account balance: $1000
Withdrawal of $400 successful
Updated account balance: $600
"""
    assert captured.out == expected_output

def test_withdraw_insufficient_funds(bank_account, capsys):
    bank_account.deposit(1000)
    bank_account.withdraw(2000)
    captured = capsys.readouterr()
    expected_output = """Deposit of $1000 successful
Updated account balance: $1000
Withdrawal of $2000 denied due to insufficient funds
Current available balance: $1000
"""
    assert captured.out == expected_output
