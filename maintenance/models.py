from django.db import models
from datetime import datetime
from index.models import index

class Running_hour(models.Model):
    pub_date = models.DateField(default=datetime.now)
    ECT = models.IntegerField(default=0000)
    MRT = models.IntegerField(default=0000)
    Machine = models.ForeignKey(index, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Machine)+" & "+str(self.pub_date)+" & "+"ECT : "+str(self.ECT)+" & "+"MRT : "+str(self.MRT)

# =========================================================================================================

class Breakfix(models.Model):

    subject = models.CharField(max_length=100)
    issue = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)

    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)

    checked_date = models.DateField(default=datetime.now)
    checked_ECT = models.IntegerField(default=0)
    checked_MRT = models.IntegerField(default=0)

    def __str__(self):
        return str(self.subject)+ " & "+str(self.title)
# =========================================================================================================

class ETC(models.Model):
 
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)

    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)

    checked_date = models.DateField(default=datetime.now)
    checked_ECT = models.IntegerField(default=0)
    checked_MRT = models.IntegerField(default=0)

    def __str__(self):
        return str(self.subject)+ " & "+str(self.title)


class PmAudit(models.Model):

    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)

    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)

    checked_date = models.DateField(default=datetime.now)
    checked_ECT = models.IntegerField(default=0)
    checked_MRT = models.IntegerField(default=0)

    def __str__(self):
        return str(self.subject)+ " & "+str(self.title)


class Overhaul(models.Model):

    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)

    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)

    checked_date = models.DateField(default=datetime.now)
    checked_ECT = models.IntegerField(default=0)
    checked_MRT = models.IntegerField(default=0)

    def __str__(self):
        return str(self.subject)+ " & "+str(self.title)









# --------------------Grease table-------------------------

class Greasing(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    grease_type = models.CharField(default='G10', max_length=30)
    grease_pcs = models.IntegerField(default=0)
    grease_expire = models.DateField()
    grease_supply = models.CharField(max_length=20)
    grease_condition = models.CharField(max_length=20)

    def __str__(self):
        return str(self.index_fk)+" & "+self.grease_type


# ----------------------Greasing work---------------------------

class Injection_ViG12(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    injection_point = models.CharField(max_length=100)
    injection_date = models.DateField()
    injection_ECT = models.IntegerField(default=0)
    injection_MRT = models.IntegerField(default=0)

    def __str__(self):
        return self.injection_point + ' & ' + str(self.index_fk)

class Injection_connecting(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    injection_point = models.CharField(max_length=100)
    injection_date = models.DateField()
    injection_ECT = models.IntegerField(default=0)
    injection_MRT = models.IntegerField(default=0)

    def __str__(self):
        return self.injection_point + ' & ' + str(self.index_fk)

class Injection_vibrail(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    injection_point = models.CharField(max_length=100)
    injection_date = models.DateField()
    injection_ECT = models.IntegerField(default=0)
    injection_MRT = models.IntegerField(default=0)

    def __str__(self):
        return self.injection_point + ' & ' + str(self.index_fk)

class Injection_xaxis(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    injection_point = models.CharField(max_length=100)
    injection_date = models.DateField()
    injection_ECT = models.IntegerField(default=0)
    injection_MRT = models.IntegerField(default=0)

    def __str__(self):
        return self.injection_point + ' & ' + str(self.index_fk)

class Injection_yaxis(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    injection_point = models.CharField(max_length=100)
    injection_date = models.DateField()
    injection_ECT = models.IntegerField(default=0)
    injection_MRT = models.IntegerField(default=0)

    def __str__(self):
        return self.injection_point + ' & ' + str(self.index_fk)

class Injection_vaccum(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    injection_point = models.CharField(max_length=100)
    injection_date = models.DateField()
    injection_ECT = models.IntegerField(default=0)
    injection_MRT = models.IntegerField(default=0)

    def __str__(self):
        return self.injection_point + ' & ' + str(self.index_fk)

class Injection_comment(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    pub_date = models.DateField()
    comment = models.TextField()

    def __str__(self):
        return self.comment + ' & ' + str(self.index_fk)

    

#    -----------------------------------------------------------------------------------

class Routine_pressfoot(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    check_date = models.DateField()
    checked_ECT = models.IntegerField(default=0)
    checked_MRT = models.IntegerField(default=0)
    comment = models.TextField() 
    bearing_condition = models.BooleanField(default=True)
    moving_condition = models.BooleanField(default=True)
    lubrication_condition = models.BooleanField(default=True)
    cleaning_condition = models.BooleanField(default=True)
    

    def __str__(self):
        return 'Routine_pressfoot : '+str(self.check_date)+str(self.index_fk)


class Routine_bladeguide(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    check_date = models.DateField()
    checked_ECT = models.IntegerField(default=0)
    checked_MRT = models.IntegerField(default=0)
    comment = models.TextField() 
    plate_condition = models.BooleanField(default=True)
    roller_condition = models.BooleanField(default=True)
    fixed_condition = models.BooleanField(default=True)
    cleaning_condition = models.BooleanField(default=True)
    

    def __str__(self):
        return 'Blade Gide : '+str(self.check_date)+str(self.index_fk)


class Routine_sharpningarm(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    check_date = models.DateField()
    checked_ECT = models.IntegerField(default=0)
    checked_MRT = models.IntegerField(default=0)
    comment = models.TextField() 
    Sharpning_Pully = models.BooleanField(default=True)
    Sharpning = models.BooleanField(default=True)
    Sharpning_wire = models.BooleanField(default=True)
    Sharpning_Arm = models.BooleanField(default=True)
    sharpning_Cleaning = models.BooleanField(default=True)
   
    
    def __str__(self):
        return 'Sharpning_Arm : '+str(self.check_date)+str(self.index_fk)



class Routine_vibration(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    check_date = models.DateField()
    checked_ECT = models.IntegerField(default=0)
    checked_MRT = models.IntegerField(default=0)
    comment = models.TextField() 
    vibration_moving = models.BooleanField(default=True)
    vibration_vibearing = models.BooleanField(default=True)
    vibration_nibearing = models.BooleanField(default=True)
    vibration_belt = models.BooleanField(default=True)
    vibration_Cleaning = models.BooleanField(default=True)
   
    
    def __str__(self):
        return 'Vibration : '+str(self.check_date)+str(self.index_fk)

# ------------------------------------------------------------------------------------------

class Routine_rotationblock(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    check_date = models.DateField()
    checked_ECT = models.IntegerField(default=0)
    checked_MRT = models.IntegerField(default=0)
    rotation_Comment = models.TextField() 
    rotation_moving = models.BooleanField(default=True)
    rotation_Belt = models.BooleanField(default=True)
    rotation_Fixed = models.BooleanField(default=True)
    rotation_cleaning = models.BooleanField(default=True)
    
    
    def __str__(self):
        return 'Rotation : '+str(self.check_date)+str(self.index_fk)


class Routine_pneumatic(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    check_date = models.DateField()
    checked_ECT = models.IntegerField(default=0)
    checked_MRT = models.IntegerField(default=0)
    pneumatic_Comment = models.TextField() 
    pneumatic_hose = models.BooleanField(default=True)
    pneumatic_bladeCylinder = models.BooleanField(default=True)
    pneumatic_pressfootcylinder = models.BooleanField(default=True)
    pneumatic_Drill = models.BooleanField(default=True)
    pneumatic_Sharpning = models.BooleanField(default=True)
    
    
    def __str__(self):
        return 'Rotation : '+str(self.check_date)+str(self.index_fk)


class Routine_airfilter(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    check_date = models.DateField()
    checked_ECT = models.IntegerField(default=0)
    checked_MRT = models.IntegerField(default=0)
    airfilter_Comment = models.TextField() 
    airfilter_cool = models.BooleanField(default=True)
    airfilter_Vaccum = models.BooleanField(default=True)
   
    
    def __str__(self):
        return 'Rotation : '+str(self.check_date)+str(self.index_fk)


class Routine_xaxis(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    check_date = models.DateField()
    checked_ECT = models.IntegerField(default=0)
    checked_MRT = models.IntegerField(default=0)
    xaxis_Comment = models.TextField() 
    xaxis_rail = models.BooleanField(default=True)
    xaxis_Cleaning = models.BooleanField(default=True)
    xaxis_plasticgear = models.BooleanField(default=True)
     
    def __str__(self):
        return 'Rotation : '+str(self.check_date)+str(self.index_fk)
 

class Routine_yaxis(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    check_date = models.DateField()
    checked_ECT = models.IntegerField(default=0)
    checked_MRT = models.IntegerField(default=0)
    yaxis_Comment = models.TextField() 
    yaxis_rail = models.BooleanField(default=True)
    yaxis_Cleaning = models.BooleanField(default=True)

     
    def __str__(self):
        return 'Rotation : '+str(self.check_date)+str(self.index_fk)

# -----------------------------------------------------------------------------------------------------

class Routine_coda(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    check_date = models.DateField()
    checked_ECT = models.IntegerField(default=0)
    checked_MRT = models.IntegerField(default=0)
    coda_Comment = models.TextField()
    coda_belt = models.BooleanField(default=True)
    coda_consol = models.BooleanField(default=True)
    coda_moving = models.BooleanField(default=True)

     
    def __str__(self):
        return 'Rotation : '+str(self.check_date)+str(self.index_fk)



class Routine_bristle(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    check_date = models.DateField()
    checked_ECT = models.IntegerField(default=0)
    checked_MRT = models.IntegerField(default=0)
    bristle_Comment = models.TextField()
    bristle_comb = models.BooleanField(default=True)
    bristle_moving = models.BooleanField(default=True)
   
    def __str__(self):
        return 'Rotation : '+str(self.check_date)+str(self.index_fk)


class Routine_airinlet(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    check_date = models.DateField()
    checked_ECT = models.IntegerField(default=0)
    checked_MRT = models.IntegerField(default=0)
    airinlet_Comment = models.TextField()
    airinlet_Regulator = models.BooleanField(default=True)
    airinlet_Separator = models.BooleanField(default=True)
    airinlet_setting = models.BooleanField(default=True)
    airinlet_pressure = models.BooleanField(default=True)


    def __str__(self):
        return 'Rotation : '+str(self.check_date)+str(self.index_fk)


class Routine_resultfabric(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    check_date = models.DateField()
    checked_ECT = models.IntegerField(default=0)
    checked_MRT = models.IntegerField(default=0)
    result_Comment = models.TextField()
    result_surface = models.BooleanField(default=True)
    result_notch = models.BooleanField(default=True)
    result_inangle = models.BooleanField(default=True)
    result_outangle = models.BooleanField(default=True)


    def __str__(self):
        return 'Rotation : '+str(self.check_date)+str(self.index_fk)



class Routine_elcabnet(models.Model):
    index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
    check_date = models.DateField()
    checked_ECT = models.IntegerField(default=0)
    checked_MRT = models.IntegerField(default=0)
    elec_Comment = models.TextField()
    elec_board = models.BooleanField(default=True)
    elec_Cable = models.BooleanField(default=True)
    elec_4axis = models.BooleanField(default=True)
    elec_cleaning = models.BooleanField(default=True)


    def __str__(self):
        return 'Rotation : '+str(self.check_date)+str(self.index_fk)






