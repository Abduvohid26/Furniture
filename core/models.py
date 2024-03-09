from django.db import models
from shared.models import BaseModel


class Enter(BaseModel):
    name = models.CharField(max_length=255)
    qty = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    ndc = models.PositiveIntegerField(default=12)

    @property
    def total_price(self):
        if self.price:
            total = self.price * self.qty
            return total

    @property
    def ndc_price(self):
        if self.total_price:
            ndc_rate = self.ndc
            ndc_amount = self.total_price * ndc_rate
            ndc_percentage = ndc_amount / 100
            ndc_total = self.total_price + ndc_percentage
            return ndc_total

    def __str__(self):
        return f"{self.name} qty-> {self.qty}"


class Order(BaseModel):
    name = models.CharField(max_length=255)
    qty = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()

    @property
    def price(self):
        if self.total_price:
            summ = self.total_price / self.qty
            return summ



















