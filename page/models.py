from django.db import models

class Info(models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length = 20)
    address = models.CharField(max_length = 255)
    description = models.TextField()

    def __str__(self):
        return self.image, self.title, self.address