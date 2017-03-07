from django.db import models


class Bio(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=45)
    email = models.EmailField()
    jid = models.CharField(max_length=30)
    skype = models.CharField(max_length=20)
    dateofbirth = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.name
