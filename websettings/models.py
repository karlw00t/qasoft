from django.db import models

# Create your models here.

class Setting(models.Model):
    name = models.CharField(max_length=120, unique=True);
    value = models.CharField(max_length=120);

    def __unicode__(self):
        value = ''
        if not self.value:
            value = '<None>'
        else:
            value = self.value
        return ''.join(['setting: ', self.name,  ' = ', value])
