from loans.models import Loan


def test_create(db):
    loan = Loan.objects.create(amount=100, term=5)
    assert loan.term_counter == 1
    assert loan.status == Loan.STATUS_NEW


def test_tick_ok(db):
    loan = Loan.objects.create(amount=100, term=5)
    loan.tick()
    assert loan.term_counter == 2


def test_tick_status_change(db):
    loan = Loan.objects.create(amount=100, term=5)
    loan.term_counter = 5
    loan.save()
    loan.tick()
    loan.refresh_from_db()
    assert loan.status == Loan.STATUS_EXPIRED
