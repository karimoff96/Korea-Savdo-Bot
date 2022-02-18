from django.db import models


class User(models.Model):
    user_id = models.BigIntegerField(default=0, unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    lang = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username


class Elon(models.Model):
    elon_id = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(default=0, blank=True, null=True)
    journey = models.CharField(max_length=20, blank=True, null=True)
    policy = models.CharField(max_length=20, blank=True, null=True)
    korobka = models.CharField(max_length=20, blank=True, null=True)
    fuel = models.CharField(max_length=30, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=False)
    cr_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='media/%Y/%m/%d', max_length=100, blank=True, null=True)
    image1 = models.ImageField(upload_to='media/%Y/%m/%d', max_length=100, blank=True, null=True)
    image2 = models.ImageField(upload_to='media/%Y/%m/%d', max_length=100, blank=True, null=True)
    memory = models.IntegerField(default=0, blank=True, null=True)
    CPU = models.IntegerField(default=0, blank=True, null=True)
    camera = models.CharField(max_length=20, blank=True, null=True)
    zaryad = models.CharField(max_length=20, blank=True, null=True)
    condition = models.CharField(max_length=30, blank=True, null=True)
    display = models.CharField(max_length=20, blank=True, null=True)
    processor = models.CharField(max_length=30, blank=True, null=True)
    step = models.IntegerField(default=0)

    def __int__(self):
        return self.elon_id
