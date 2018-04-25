from django.db import models


# Create your models here.
class Goods(models.Model):
    """
    Model representing a property of goods
    """
    name = models.CharField(max_length=200, help_text="Enter a goods name")
    description = models.CharField(max_length=300,
                                   help_text="Short descriptions for goods(300 sym)")
    gvls = models.BooleanField(default=False, help_text='Is GVLS')
    supplier = models.ForeignKey(
        'Supplier',
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Supplier(models.Model):
    """
    Model representing supplier
    """
    name = models.CharField(max_length=200, help_text="Name of Supplier")
    created_at = models.DateTimeField(auto_now_add=True)
    payment_delay = models.PositiveSmallIntegerField(blank="True", default=0,
                                                     help_text="delay of payment for supplier")
    enabled = models.BooleanField(default=True, help_text="Is cooperation enabled")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Store(models.Model):
    """
    Model representing current state of stock
    """
    goods = models.ForeignKey(Goods, on_delete=models.SET_NULL, null=True)
    is_present = models.BooleanField(default=False, help_text="Is item on the stock")
    amount = models.PositiveIntegerField(help_text="amount of goods")
    price = models.DecimalField(max_digits=9, decimal_places=2)
    exp_date = models.DateField(help_text="date of expiration")
    num_of_series = models.PositiveSmallIntegerField(help_text="Number of series of goods")

    class Meta:
        ordering = ["goods"]

    def __str__(self):
        return self.goods
