from django.db import models

# Create your models here.

class PropertyTypes(models.Model):
    PropertyTypeName=models.TextField(max_length=200)
    
    def __str__ (self):
        return self.PropertyTypeName
    