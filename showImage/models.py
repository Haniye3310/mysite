from django.db import models

class Image(models.Model):
    image_field = models.FileField(upload_to="images/")

