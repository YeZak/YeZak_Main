from django.contrib.auth import get_user_model
from pickle import TRUE
from django.db import models
from datetime import datetime

# User = get_user_model()

# class Post(models.Model):
#     objects = None
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)
#     image = models.ImageField(null=True)
#
#     #Json-serialized (text) version of your list
#     tag_list = models.TextField(null=True)
#
#     THEME1 = 'theme1'  # impressionism = pastel color interior
#     THEME2 = 'theme2'  # realism = palace
#     THEME3 = 'theme3'  # orientalism + animation = warm color interior
#     THEME4 = 'theme4'  # abstract + pop_art = primary color interior
#     THEME5 = 'theme5'  # pencil_drawing = white/black interior
#
#     PREDICTION_CHOICES = [
#         (THEME1, 'theme1'),
#         (THEME2, 'theme2'),
#         (THEME3, 'theme3'),
#         (THEME4, 'theme4'),
#         (THEME5, 'theme5'),
#     ]
#     prediction = models.CharField(choices=PREDICTION_CHOICES, max_length=22)
#     public = models.BooleanField(default=True)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'

#
class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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
    img = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interior'


# class Post(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)
#     image = models.ImageField(null=True)
#     public = models.BooleanField()
#     tag_list = models.TextField(blank=True, null=True)  #그림 설명 태그 => item
#     prediction = models.CharField(max_length=22) #장르
#
#     class Meta:
#         managed = False
#         db_table = 'core_post'


class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)

    item_id = models.IntegerField(primary_key=True)
    item_pic = models.ImageField(upload_to = "uploads")
    price = models.IntegerField()
    item_size_width = models.CharField(max_length=45)
    item_size_height = models.CharField(max_length=45)
    details = models.TextField(max_length=2000, blank=True, null=True)
    seller = models.ForeignKey('Member', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField(auto_now = True)
    item_name = models.CharField(max_length=45, blank=True, null=True)

    #추가
    tag_list = models.TextField(blank=True, null=True)

    ORIENTALISM = "orientalism"
    REALISM = "realism"
    ANIMATION = "animation"
    PENCIL = "pencil"
    IMPRESSIONISM = "impressionism"
    ABSTRACT = "abstract"
    POPART = "popart"

    PREDICTION_CHOICES = [
        (ORIENTALISM, "orientalism"),
        (REALISM, "realism"),
        (ANIMATION, "animation"),
        (PENCIL, "pencil"),
        (IMPRESSIONISM, "impressionism"),
        (ABSTRACT, "abstract"),
        (POPART, "popart"),
    ]

    prediction = models.CharField(choices=PREDICTION_CHOICES, max_length=22)

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




class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'