from django.db import models

# Create your models here.
class feed_inventory(models.Model):
    id = models.IntegerField(primary_key= True, auto_created= True)
    feed_name = models.CharField(max_length=20)
    feed_url = models.CharField(max_length=100)
    modified_date = models.DateTimeField()






