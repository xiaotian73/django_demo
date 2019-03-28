from django.db import models

# Create your models here.
#定义数据库模型
class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name
