from django.db import models
from account.models import User
from datetime import datetime


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="post"
        )
    image = models.ImageField(
        upload_to="posts/",
        null=True,
        blank=True,
        height_field=None,
        width_field=None,
        max_length=None,
    )
    created_at = models.DateTimeField(default=datetime.now())
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class Like(models.Model):
    user = models.ForeignKey(
        User,
        related_name="user",
        on_delete=models.CASCADE
    )

    post = models.ForeignKey(
        Post,
        related_name="likes",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.user} liked {self.post} at {self.created_at}"


class Comment(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.user} - {self.post} - {self.created_at}"
        

class PostHistory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    image = models.ImageField(
        upload_to="posts/",
        null=True,
        blank=True,
        height_field=None,
        width_field=None,
        max_length=None,
    )
    deleted_at = models.DateTimeField(default=datetime.now())
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)





        

 
         
            
        

