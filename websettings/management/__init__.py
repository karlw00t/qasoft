from django.db.models.signals import post_syncdb
from websettings import models
from django.conf import settings

def my_callback(sender, **kwargs):
    # Your specific logic here
    for websetting in settings.WEBSETTINGS:
        setting = models.Setting.objects.filter(name=websetting['name']).count()
        if not setting:
            setting = models.Setting(name=websetting['name'])
            setting.save()
            print setting

post_syncdb.connect(my_callback, sender=models)
