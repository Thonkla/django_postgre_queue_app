from django.db import models

class MENU(models.Model):
    menu_name = models.CharField(primary_key=True, max_length=100)
    menu_price = models.FloatField(null=True)
    description = models.CharField(max_length=500)
    menu_type = models.CharField(max_length=100)
    class Meta:
        db_table="menu"
        managed = False
    def __str__(self):
        return self.menu_name
    
class USERNAME(models.Model):
    username = models.CharField(max_length=100)
    table_no = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    class Meta:
        db_table="username"
        managed = False
    def __str__(self):
        return self.username

class USERQUEUE(models.Model):
    queue_id = models.IntegerField(primary_key=True)
    username = models.CharField(null=True, max_length=100)
    table_no = models.IntegerField(null=True)
    total_price = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    payment_method = models.CharField(null=True, max_length=50)
    status = models.CharField(max_length=20)
    class Meta:
        db_table="userqueue"
        managed = False
    def __str__(self):
        return str(self.queue_id)

class USERQUEUE_DETAIL(models.Model):
    id = models.IntegerField(primary_key=True)
    queue_id = models.IntegerField()
    menu_name = models.CharField(max_length=50)
    quantity = models.IntegerField(null=True)
    price = models.FloatField(null=True)
    class Meta:
        db_table = "userqueue_detail"
        managed = False
    def __str__(self):
        return '{"queue_id":"%s","price":"%s"}' % (self.queue_id, self.price)
    
class USERTABLE(models.Model):
    username = models.CharField(max_length=100)
    table_no =  models.IntegerField(null=True)
    menu_name = models.CharField(null=True, max_length=50)
    menu_price = menu_price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)
    id = models.AutoField(primary_key=True)
    class Meta:
        db_table = "usertable"
        managed = False
    def __str__(self):
        return self.username

class PAYMENT_METHOD(models.Model):
    payment_method = models.CharField(primary_key=True, max_length=50)
    description = models.CharField(max_length=50)
    class Meta:
        db_table = "payment_method"
        managed = False
    def __str__(self):
        return self.description