from pickle import TRUE
from django.db import models
from datetime import datetime


class Deals(models.Model):
    item = models.OneToOneField('Item', models.DO_NOTHING, primary_key=True)
    state = models.CharField(max_length=45)
    buyer = models.ForeignKey('Member', models.DO_NOTHING, blank=True, null=True, related_name="Deals_buyer")
    seller = models.ForeignKey('Member', models.DO_NOTHING, related_name="Deals_seller")

    class Meta:
        managed = False
        db_table = 'deals'


class Image(models.Model):
    img_id = models.IntegerField(primary_key=True)
    item = models.ForeignKey('Item', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image'


class Interior(models.Model):
    interior_id = models.IntegerField(primary_key=True)
    img = models.ImageField(upload_to = "interior")


    class Meta:
        managed = False
        db_table = 'interior'


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_pic = models.ImageField(upload_to = "uploads")
    price = models.IntegerField()
    item_size_width = models.CharField(max_length=45)
    item_size_height = models.CharField(max_length=45)
    details = models.TextField(max_length=2000, blank=True, null=True)
    seller = models.ForeignKey('Member', models.DO_NOTHING, blank=True, default="user1")
    date = models.DateField(auto_now= True)
    item_name = models.CharField(max_length=45, blank=True, null=True)

    tag_list = models.CharField(max_length=45, blank=True, null=True)
    label = models.IntegerField(blank=True, null=True)
    pic_interior = models.ImageField(upload_to = "merge_interior", blank=True, null=True)
    prediction = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'


class Member(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=20)  # Field name made lowercase.
    password = models.CharField(max_length=45)
    profile_pic = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'


class Message(models.Model):
    msg_id = models.IntegerField(db_column='msg_ID', primary_key=True)  # Field name made lowercase.
    msg_content = models.CharField(max_length=2000, blank=True, null=True)
    buyer = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True, related_name="Message_buyer")
    seller = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True, related_name="Message_seller")

    class Meta:
        managed = False
        db_table = 'message'