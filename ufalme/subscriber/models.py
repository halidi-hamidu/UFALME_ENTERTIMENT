from django.db import models
import  uuid
# Create your models here.
class CustomerInformations(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique = True)
  package_name = models.CharField(max_length=100)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  phone_number = models.CharField(max_length=100)
  email = models.EmailField()
  comments = models.CharField(max_length=5000)
  created_at = models.DateTimeField(auto_now_add =True) #never change once the object is created
  updated_at = models.DateTimeField(auto_now =True) # always change when object is updated
  
  class Meta:
      verbose_name_plural = 'Customers List'
  def __str__(self):
      return (self.first_name)
