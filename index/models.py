from django.db import models

class index(models.Model):
    site_name = models.CharField(max_length=100)
    site_address = models.CharField(max_length=200)
    machine_type = models.CharField(max_length=100) #auto or fashion
    machine_model = models.CharField(max_length=100) #iQ80-71
    machine_number = models.CharField(max_length=100, null=True, blank=True, default='Serial_Number')
 
    def __str__(self):
        return self.site_name+" & "+self.machine_type+" & "+self.machine_model+" & "+self.machine_number



