from django.db import models

# Create your models here.

class test(models.Model):

    _mail = models.CharField(max_length=100)

    _number = models.IntegerField(default=10)

    def __str__(self):
        return "{0} / {1}<br>".format(self._mail, str(self._number))

    def num(self):
    	return str(self._number)

    def mel(self):
    	return self._mail