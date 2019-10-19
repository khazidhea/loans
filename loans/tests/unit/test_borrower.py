from loans.factories import BorrowerFactory


def test_borrower(db):
    borrower = BorrowerFactory.create()
    assert isinstance(borrower.name, str)
