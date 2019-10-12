from django.db import models


class Loan(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
