from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=200, null=False)
    #user = models.CharField(max_length=20, null=False)
    #size = models.CharField(max_length=20, null=False)
    #upload = models.FileField(upload_to=user_directory_path)
    #upload = models.FileField(upload_to='uploads/')
    content = models.TextField()
    create_date = models.DateTimeField(auto_now = True)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)