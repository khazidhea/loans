import random

import factory


AMOUNT_MIN = 1000
AMOUNT_MAX = 100_000
AMOUNT_STEP = 1000

TERM_MIN = 5
TERM_MAX = 30


class LoanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'loans.Loan'

    amount = factory.LazyAttribute(lambda o: random.randrange(AMOUNT_MIN, AMOUNT_MAX, AMOUNT_STEP))
    term = factory.LazyAttribute(lambda o: random.randrange(TERM_MIN, TERM_MAX))


class BorrowerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'loans.Borrower'

    name = factory.Faker('name')
