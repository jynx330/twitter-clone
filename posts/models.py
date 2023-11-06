from django.db import models
from cloudinary.models import CloudinaryField

class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=15, db_index=True, default='Anonymous'
    )

    body = models.CharField(
        'Body', blank=True, null=True, max_length=150, db_index=True
    )

    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )
    likes = models.PositiveIntegerField('likes', default =0, blank=True)

    pictures = CloudinaryField('pictures', blank=True)

