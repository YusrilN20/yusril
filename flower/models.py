from django.db import models
import os
from django.utils.translation import gettext_lazy as _
class FlowerModel(models.Model):
    image = models.ImageField(_("image"), upload_to='flower_imgs/')

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return str(os.path.split(self.image.path)[-1])


class ModelPosting(models.Model):
    image = models.ImageField(_("image"), upload_to='flower_imgs/', blank=True)
    posting = models.TextField(blank=True,null=True)
    date_updated = models.DateField(auto_now=True, auto_created= True)
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return str(os.path.split(self.image.path)[-1])
# Create your models here.
