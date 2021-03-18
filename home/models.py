from django.db import models

# Create your models here.
# for contact class model is being created here
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField(default='No review added')
    date = models.DateField()
    #this will show name and phone as title field
    def __str__(self):
        return ('Name : ' +self.name + ", Contact :  " +self.phone)
