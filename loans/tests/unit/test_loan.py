import pytest

from loans.models import Loan
from loans.factories import LoanFactory


@pytest.fixture
def loan():
    return LoanFactory.create()


def test_create(db, loan):
    assert loan.term_counter == 1
    assert loan.status == Loan.STATUS_NEW


def test_tick_ok(db, loan):
    loan.tick()
    assert loan.term_counter == 2


def test_tick_status_change(db, loan):
    loan.term = 5
    loan.term_counter = 5
    loan.save()
    loan.tick()
    loan.refresh_from_db()
    assert loan.status == Loan.STATUS_EXPIRED
