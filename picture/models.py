from django.db import models

class Picture(models.Model):
    name = models.CharField(max_length=100)
    uploader = models.CharField(max_length=100)
    image = models.ImageField()
    date_upload = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_upload',)

    # Constructor
    def __str__(self):
        return self.name