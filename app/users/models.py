from django.db import models

# Create your models here.

class User(models.Model):

    first_name = models.CharField(max_length=256, blank=False, null=False)

    last_name = models.CharField(max_length=256, blank=False, null=False)

    email = models.CharField(max_length=256, blank=True, null=True)

    age = models.IntegerField(blank=True, null=True)

    def __str__ (self):
      """ Sensible string representation of a user."""
      return "{0} {1} | {2}".format(self.first_name, self.last_name, self.email)

class Profession(models.Model):
  name = models.CharField(max_length=256, blank=False, null=False)
  salary = models.IntegerField(blank=False, null=False) 

  def __str__(self):
    """ Representation of a profession object """
    return"{0} pays {1}".format(self.name, self.salary)
