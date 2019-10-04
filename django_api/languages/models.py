from django.db import models

# Create your models here.
class Language(models.Model):
    name= models.CharField(max_length= 50)
    response_time= models.CharField(max_length= 255, default='0 s')
    


    def __str__(self):
        return self.name