from django.db import models


class Borrower(models.Model):
    name = models.CharField(max_length=100)


class Loan(models.Model):
    STATUS_NEW = 'new'
    STATUS_ACTIVE = 'active'
    STATUS_PAID = 'paid'
    STATUS_EXPIRED = 'expired'
    STATUS_CHOICES = (
        (STATUS_NEW, STATUS_NEW),
        (STATUS_ACTIVE, STATUS_ACTIVE),
        (STATUS_PAID, STATUS_PAID),
        (STATUS_EXPIRED, STATUS_EXPIRED),
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    term = models.IntegerField(default=5)
    term_counter = models.IntegerField(default=1)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW
    )

    def tick(self):
        self.term_counter += 1
        if self.term_counter > self.term:
            self.status = Loan.STATUS_EXPIRED
        self.save()
