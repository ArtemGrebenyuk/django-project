from django.db import models
import uuid

# Create your models here.
class Goods(models.Model):
    """
    Model representing a property of goods
    """
    idGoods = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for item across whole storage")
    name = models.CharField(max_length=200, help_text="Enter a goods name")
    description = models.CharField(max_length=300, help_text="Short descriptions for goods(300 symbols)")
    isGVLS = models.BooleanField(default="False", help_text='Is GVLS')
    supplier = models.ForeignKey(
        'Supplier',
        on_delete=models.SET_NULL,
        null='true',
    )

    def __str__(self):
        return self.name


    class Meta:
        ordering = ["name"]

class Supplier(models.Model):
    """
    Model representing supplier
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for supplier")
    name = models.CharField(max_length=200, help_text="Name of Supplier")
    whenCreated = models.DateField(auto_now_add="True")
    delayOfPayment = models.PositiveSmallIntegerField(blank="True", default=0, help_text="delay of payment for supplier")
    enabled = models.BooleanField(default="True", help_text="Is cooperation enabled")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Store(models.Model):
    """
    Model representing current state of stock
    """
    goods = models.ForeignKey(Goods, on_delete=models.SET_NULL, null="True")
    isPresent = models.BooleanField(default="False", help_text="Is item on the stock")
    Amount = models.PositiveIntegerField(help_text="amount of goods")
    Price = models.DecimalField(decimal_places=2)
    ExpDate = models.DateField(help_text="date of expiration")
    NumOfSeries = models.PositiveSmallIntegerField(help_text="Number of series of goods")

    class Meta:
        ordering = ["goods"]

    def __str__(self):
        return self.goods




