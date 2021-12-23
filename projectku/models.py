from django.db import models

class doc_psd(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    solusi = models.TextField()
    category = models.TextField()
    published = models.DateTimeField(auto_now_add= True)
    update  = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return "{}".format(self.title)

