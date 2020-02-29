from django.shortcuts import render, redirect
from django.http import HttpResponse
from index.models import index
from .models import *
from datetime import datetime, timedelta



def RunningHour(request, pk):
    if request.user.is_authenticated:

        if request.method == 'GET':
            return render(request, 'Running_hour.html',{'pk':pk})
        else:
            selected_index = index.objects.get(pk=pk)
            
            today_date = request.POST['Today_Date']
            ECT = request.POST['ECT']
            MRT = request.POST['MRT']
            new_Running_hour = Running_hour(pub_date=today_date, ECT=ECT, MRT=MRT, Machine=selected_index)
            new_Running_hour.save()

            index_pk = pk
            
            return redirect('maintenance:timeform',index_pk)       #<---수정예정 , maintenance 페이지로 이동 
    else:
        return redirect('account:Login')
        
def timeform(request, index_pk):

    selected_index = index.objects.get(pk=index_pk)
    try:
        selected_hour_now = selected_index.running_hour_set.all().order_by('-pub_date', '-ECT')[0]
        selected_hour_last = selected_index.running_hour_set.all().order_by('-pub_date', '-ECT')[1]

        date_today = selected_hour_now.pub_date
        date_last = selected_hour_last.pub_date
        date_diff = (date_today-date_last).days

        ect_today = selected_hour_now.ECT
        last_time = selected_hour_last.ECT
        ect_diff = int(ect_today)-int(last_time)

        mrt_today = selected_hour_now.MRT
        last_time = selected_hour_last.MRT
        mrt_diff = int(mrt_today)-int(last_time)

        context={'date_today':date_today, 'date_last':date_last, 'date_diff':date_diff, 
        'ect_today':ect_today, 'ect_diff':ect_diff, 'mrt_today':mrt_today, 'mrt_diff':mrt_diff, 
        'index_pk':index_pk, 'selected_index':selected_index}

        return render(request, 'Timerecord_formselection.html', context)

    except:
        selected_hour_now = selected_index.running_hour_set.all().order_by('-pub_date')[0]
        date_today = selected_hour_now.pub_date

        ect_today = selected_hour_now.ECT
        mrt_today = selected_hour_now.MRT
  

        context={'date_today':date_today, 
        'ect_today':ect_today, 'mrt_today':mrt_today,
        'index_pk':index_pk, 'selected_index':selected_index}

        return render(request, 'Timerecord_formselection.html', context)


def breakfix(request, index_pk):
    if request.method =='GET':

        selected_index = index.objects.get(pk=index_pk)
        selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]


        context={'selected_index':selected_index, 'index_pk':index_pk, 'selected_hour':selected_hour}

        return render(request, 'Breakfix.html', context)

    else:
        selected_index = index.objects.get(pk=index_pk)
        selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]

        subject = request.POST['subject']
        issue = request.POST['issue']
        title = request.POST['title']
        comment = request.POST['comment']

        checked_date = selected_hour.pub_date
        checked_ECT = selected_hour.ECT
        checked_MRT = selected_hour.MRT
 
        new_objects = Breakfix(issue=issue, subject=subject, title=title, comment=comment,
        checked_date=checked_date, checked_ECT=checked_ECT, checked_MRT=checked_MRT,
        index_fk = selected_index)
        new_objects.save()


        context={'selected_index':selected_index, 'index_pk':index_pk, 'selected_hour':selected_hour}

        return redirect('maintenance:timeform', index_pk)


def ETC_form(request, index_pk):
    if request.method =='GET':

        selected_index = index.objects.get(pk=index_pk)
        selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]


        context={'selected_index':selected_index, 'index_pk':index_pk, 'selected_hour':selected_hour}

        return render(request, 'Etc.html', context)

    else:
        selected_index = index.objects.get(pk=index_pk)
        selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]

        subject = request.POST['subject']
        title = request.POST['title']
        comment = request.POST['comment']

        checked_date = selected_hour.pub_date
        checked_ECT = selected_hour.ECT
        checked_MRT = selected_hour.MRT
        
        new_objects = ETC(subject=subject, title=title, comment=comment,index_fk = selected_index,
        checked_date=checked_date, checked_ECT=checked_ECT, checked_MRT=checked_MRT)
        new_objects.save()


        context={'selected_index':selected_index, 'index_pk':index_pk, 'selected_hour':selected_hour}

        return redirect('maintenance:timeform', index_pk)

        

def pm_audit(request, index_pk):
    if request.method =='GET':

        selected_index = index.objects.get(pk=index_pk)
        selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]


        context={'selected_index':selected_index, 'index_pk':index_pk, 'selected_hour':selected_hour}

        return render(request, 'Pmaudit.html', context)

    else:
        selected_index = index.objects.get(pk=index_pk)
        selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]

        subject = request.POST['subject']
        title = request.POST['title']
        comment = request.POST['comment']

        checked_date = selected_hour.pub_date
        checked_ECT = selected_hour.ECT
        checked_MRT = selected_hour.MRT
        
        new_objects = PmAudit(checked_date=checked_date,subject=subject, title=title, comment=comment,index_fk = selected_index,
        checked_ECT=checked_ECT,checked_MRT=checked_MRT)
        new_objects.save()


        context={'selected_index':selected_index, 'index_pk':index_pk, 'selected_hour':selected_hour}

        return redirect('maintenance:timeform', index_pk)

# ---------------------------------------------------------------------------------------------------

def overhaul(request, index_pk):
    if request.method =='GET':

        selected_index = index.objects.get(pk=index_pk)
        selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]


        context={'selected_index':selected_index, 'index_pk':index_pk, 'selected_hour':selected_hour}

        return render(request, 'Overhaul.html', context)

    else:
        selected_index = index.objects.get(pk=index_pk)
        selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]

        subject = request.POST['subject']
        title = request.POST['title']
        comment = request.POST['comment']

        checked_date = request.POST['Today_Date']
        checked_ECT = request.POST['ECT']
        checked_MRT = request.POST['MRT']
        
        new_objects = Overhaul(checked_date=checked_date,subject=subject, title=title, comment=comment,index_fk = selected_index,
        checked_ECT=checked_ECT,checked_MRT=checked_MRT)
        new_objects.save()


        context={'selected_index':selected_index, 'index_pk':index_pk, 'selected_hour':selected_hour}

        return redirect('maintenance:timeform', index_pk)


# ------------------------------------------------------------------------------------------------------
# grasring work page, indication table

def greasing(request, index_pk):

    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]

    selected_grease = selected_index.greasing_set.all().order_by('grease_type')



    #   -------------------       GREASE WORK TABLE         -------------------------------------------


    # vibration_bearing = selected_index.injection_vig12_set.all().order_by('-id')[0]
    # inject_date_vibration_bearing = vibration_bearing.injection_date
    # inject_ECT_vibration_bearing = (selected_hour.ECT - vibration_bearing.injection_ECT)
    # inject_MRT_vibration_bearing = (selected_hour.MRT - vibration_bearing.injection_MRT)

    try:
        vibration_bearing = selected_index.injection_vig12_set.all().order_by('-id')[0]
        inject_date_vibration_bearing = vibration_bearing.injection_date
        inject_ECT_vibration_bearing = (selected_hour.ECT - vibration_bearing.injection_ECT)
        inject_MRT_vibration_bearing = (selected_hour.MRT - vibration_bearing.injection_MRT)
    except:
        inject_date_vibration_bearing = 'None'
        inject_ECT_vibration_bearing = (selected_hour.ECT)
        inject_MRT_vibration_bearing = (selected_hour.MRT)

# -------------------------------------------------------------------------------------------------------
    try:
        connecting = selected_index.injection_connecting_set.all().order_by('-id')[0]
        inject_date_connecting = connecting.injection_date
        inject_ECT_connecting = (selected_hour.ECT - connecting.injection_ECT)
        inject_MRT_connecting = (selected_hour.MRT - connecting.injection_MRT)
    except:
        inject_date_connecting = 'None'
        inject_ECT_connecting = (selected_hour.ECT)
        inject_MRT_connecting = (selected_hour.MRT)


# -------------------------------------------------------------------------------------------------------
    try:
        vibrail = selected_index.injection_vibrail_set.all().order_by('-id')[0]
        inject_date_vibrail = vibrail.injection_date
        inject_ECT_vibrail = (selected_hour.ECT - vibrail.injection_ECT)
        inject_MRT_vibrail = (selected_hour.MRT - vibrail.injection_MRT)
    except:
        inject_date_vibrail = 'None'
        inject_ECT_vibrail = (selected_hour.ECT)
        inject_MRT_vibrail = (selected_hour.MRT)

# -------------------------------------------------------------------------------------------------------
    try:
        xaxis = selected_index.injection_xaxis_set.all().order_by('-id')[0]
        inject_date_xaxis = xaxis.injection_date
        inject_ECT_xaxis = (selected_hour.ECT - xaxis.injection_ECT)
        inject_MRT_xaxis = (selected_hour.MRT - xaxis.injection_MRT)
    except:
        inject_date_xaxis = 'None'
        inject_ECT_xaxis = (selected_hour.ECT)
        inject_MRT_xaxis = (selected_hour.MRT)


# -------------------------------------------------------------------------------------------------------
    try:
        yaxis = selected_index.injection_yaxis_set.all().order_by('-id')[0]
        inject_date_yaxis = yaxis.injection_date
        inject_ECT_yaxis = (selected_hour.ECT - yaxis.injection_ECT)
        inject_MRT_yaxis = (selected_hour.MRT - yaxis.injection_MRT)
    except:
        inject_date_yaxis = 'None'
        inject_ECT_yaxis = (selected_hour.ECT)
        inject_MRT_yaxis = (selected_hour.MRT)


# -------------------------------------------------------------------------------------------------------
    try:
        vaccum = selected_index.injection_vaccum_set.all().order_by('-id')[0]
        inject_date_vaccum = vaccum.injection_date
        inject_ECT_vaccum = (selected_hour.ECT - vaccum.injection_ECT)
        inject_MRT_vaccum = (selected_hour.MRT - vaccum.injection_MRT)
    except:
        inject_date_vaccum = 'None'
        inject_ECT_vaccum = (selected_hour.ECT)
        inject_MRT_vaccum = (selected_hour.MRT)


        # -------------------------------------------------------------------------------------------------------
    try:
        comment = selected_index.injection_comment_set.all().order_by('-id')[0]
        inject_pub_date = comment.pub_date
        inject_comment = comment.comment
     
    except:
        inject_pub_date = '1987-04-14'
        inject_comment = 'None'

    
     #   -------------------       //////////////////////        -------------------------------------------

    context={'selected_index':selected_index, 'index_pk':index_pk, 
    'selected_hour':selected_hour, 'selected_grease':selected_grease,
    'inject_date_vibration_bearing':inject_date_vibration_bearing,
    'inject_ECT_vibration_bearing':inject_ECT_vibration_bearing,
    'inject_MRT_vibration_bearing':inject_MRT_vibration_bearing,
    'inject_date_connecting':inject_date_connecting,
    'inject_ECT_connecting':inject_ECT_connecting,
    'inject_MRT_connecting':inject_MRT_connecting,
    'inject_date_vibrail':inject_date_vibrail,
    'inject_ECT_vibrail':inject_ECT_vibrail,
    'inject_MRT_vibrail':inject_MRT_vibrail,
    'inject_date_xaxis':inject_date_xaxis,
    'inject_ECT_xaxis':inject_ECT_xaxis,
    'inject_MRT_xaxis':inject_MRT_xaxis,
    'inject_date_yaxis':inject_date_yaxis,
    'inject_ECT_yaxis':inject_ECT_yaxis,
    'inject_MRT_yaxis':inject_MRT_yaxis,

    'inject_date_vaccum':inject_date_vaccum,
    'inject_ECT_vaccum':inject_ECT_vaccum,
    'inject_MRT_vaccum':inject_MRT_vaccum,
    'inject_pub_date':inject_pub_date,
    'inject_comment':inject_comment}

    return render(request, 'Greasing.html', context)

# ======================================================================================================

def greasing_VibrationBearing(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]

    index_fk = selected_index
    injection_point = 'VibrationBearing_G12'
    injection_date = selected_hour.pub_date
    injection_ECT = selected_hour.ECT
    injection_MRT = selected_hour.MRT
    new_object = Injection_ViG12(index_fk=selected_index, injection_point=injection_point, injection_date=injection_date,
    injection_ECT=injection_ECT, injection_MRT=injection_MRT)
    new_object.save()

    return redirect('maintenance:greasing', index_pk)


def greasing_Connecting(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]

    index_fk = selected_index
    injection_point = 'Connecting_Rod_G11'
    injection_date = selected_hour.pub_date
    injection_ECT = selected_hour.ECT
    injection_MRT = selected_hour.MRT
    new_object = Injection_connecting(index_fk=selected_index, injection_point=injection_point, injection_date=injection_date,
    injection_ECT=injection_ECT, injection_MRT=injection_MRT)
    new_object.save()

    return redirect('maintenance:greasing', index_pk)


def injection_vibrail(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]

    index_fk = selected_index
    injection_point ='VibrationRail_G10'
    injection_date = selected_hour.pub_date
    injection_ECT = selected_hour.ECT
    injection_MRT = selected_hour.MRT

    new_object = Injection_vibrail(
    index_fk = selected_index, 
    injection_point = injection_point, 
    injection_date = injection_date,
    injection_ECT = injection_ECT, 
    injection_MRT = injection_MRT)
    new_object.save()

    return redirect('maintenance:greasing', index_pk)


def injection_xaxis(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]

    index_fk = selected_index
    injection_point ='X_Axis_G10'
    injection_date = selected_hour.pub_date
    injection_ECT = selected_hour.ECT
    injection_MRT = selected_hour.MRT

    new_object = Injection_xaxis(
    index_fk = selected_index, 
    injection_point = injection_point, 
    injection_date = injection_date,
    injection_ECT = injection_ECT, 
    injection_MRT = injection_MRT)
    new_object.save()

    return redirect('maintenance:greasing', index_pk)



def injection_Yaxis(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]

    index_fk = selected_index
    injection_point ='Y_Axis_G10'
    injection_date = selected_hour.pub_date
    injection_ECT = selected_hour.ECT
    injection_MRT = selected_hour.MRT

    new_object = Injection_yaxis(
    index_fk = selected_index, 
    injection_point = injection_point, 
    injection_date = injection_date,
    injection_ECT = injection_ECT, 
    injection_MRT = injection_MRT)
    new_object.save()

    return redirect('maintenance:greasing', index_pk)



def injection_vaccum(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]

    index_fk = selected_index
    injection_point ='Vaccum Turbine'
    injection_date = selected_hour.pub_date
    injection_ECT = selected_hour.ECT
    injection_MRT = selected_hour.MRT

    new_object = Injection_vaccum(
    index_fk = selected_index, 
    injection_point = injection_point, 
    injection_date = injection_date,
    injection_ECT = injection_ECT, 
    injection_MRT = injection_MRT)
    new_object.save()

    return redirect('maintenance:greasing', index_pk)


def injection_comment(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]

    index_fk = selected_index
    injection_point ='Vaccum Turbine'
    injection_date = selected_hour.pub_date

    
    grease_comment = request.POST['comment']

    new_object = Injection_comment(
    index_fk = selected_index, 
    pub_date = injection_date,
    comment =  grease_comment)
    new_object.save()

    return redirect('maintenance:greasing', index_pk)


# --------------------------------------------------------------------------------------------------------------

def greasing_add(request, index_pk):

    if request.method == "GET":
        selected_index = index.objects.get(pk=index_pk)
        selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]
    
        context={'selected_index':selected_index, 'index_pk':index_pk, 
        'selected_hour':selected_hour}

        return render(request, 'Greasing_add.html', context)
    else:
        selected_index = index.objects.get(pk=index_pk)
        new_type = request.POST['TYPE']
        new_pcs = request.POST['pcs']
        new_expire = request.POST['expire_date']
        new_supply = request.POST['supply']
        new_condition = request.POST['condition']

        new_object = Greasing(grease_type=new_type, grease_pcs=new_pcs, 
        grease_expire=new_expire, grease_supply=new_supply, grease_condition=new_condition, index_fk=selected_index)
        new_object.save()

        return redirect('maintenance:greasing', index_pk)
        
   

def greasing_modify(request, index_pk, grease_pk):

    if request.method == 'GET':
        selected_index = index.objects.get(pk=index_pk)
        selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]         
        selected_grease = Greasing.objects.get(pk=grease_pk)
    
        context={'selected_index':selected_index, 'index_pk':index_pk, 
        'selected_hour':selected_hour, 'selected_grease':selected_grease}

        return render(request, 'Greasing_modify.html', context)

    else:
        selected_index = index.objects.get(pk=index_pk)
        selected_grease = Greasing.objects.get(pk=grease_pk)

        selected_grease.grease_type = request.POST['TYPE']
        selected_grease.grease_pcs = request.POST['pcs']
        selected_grease.grease_expire = request.POST['expire_date']
        selected_grease.grease_supply = request.POST['supply']
        selected_grease.grease_condition = request.POST['condition']
        selected_grease.save()


        return redirect('maintenance:greasing', index_pk)



# ===================================================================================================
# -----------------------------Routine check page-----------------------------------------------

def routine_check_1(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]

    
 # ---------------------press_foot---------------------------------------------------------
    try:
        selected_pressfoot = selected_index.routine_pressfoot_set.all().order_by('-id')[0]
        pressfoot_guide_ECT_Diff = (selected_hour.ECT - selected_pressfoot.checked_ECT)
        pressfoot_guide_MRT_Diff = (selected_hour.MRT - selected_pressfoot.checked_MRT)
    except:
        selected_pressfoot='No data'
        pressfoot_guide_ECT_Diff = 'No data'
        pressfoot_guide_MRT_Diff = 'No data'


 # ---------------------bladeguide---------------------------------------------------------
    try:
        selected_bladeguide = selected_index.routine_bladeguide_set.all().order_by('-id')[0]
        blguide_ECT_Diff = (selected_hour.ECT - selected_bladeguide.checked_ECT)
        blguide_MRT_Diff = (selected_hour.MRT - selected_bladeguide.checked_MRT)
    except:
        selected_bladeguide='No data'
        blguide_ECT_Diff = 'No data'
        blguide_MRT_Diff = 'No data'

 # ---------------------sharpning---------------------------------------------------------
    try:
        selected_sharpning = selected_index.routine_sharpningarm_set.all().order_by('-id')[0]
        sharpning_ECT_Diff = (selected_hour.ECT - selected_sharpning.checked_ECT)
        sharpning_MRT_Diff = (selected_hour.MRT - selected_sharpning.checked_MRT)
    except:
        selected_sharpning= 'No data'
        sharpning_ECT_Diff = 'No data'
        sharpning_MRT_Diff = 'No data'

 # ---------------------vibration---------------------------------------------------------
    try:
        selected_vibration = selected_index.routine_vibration_set.all().order_by('-id')[0]
        vibration_ECT_Diff = (selected_hour.ECT - selected_vibration.checked_ECT)
        vibration_MRT_Diff = (selected_hour.MRT - selected_vibration.checked_MRT)
    except:
        selected_vibration= 'No data'
        vibration_ECT_Diff = 'No data'
        vibration_MRT_Diff = 'No data'


 # ---------------------rotation---------------------------------------------------------
    try:
        selected_rotation = selected_index.routine_rotationblock_set.all().order_by('-id')[0]
        rotation_ECT_Diff = (selected_hour.ECT - selected_rotation.checked_ECT)
        rotation_MRT_Diff = (selected_hour.MRT - selected_rotation.checked_MRT)
    except:
        selected_rotation= 'No data'
        rotation_ECT_Diff = 'No data'
        rotation_MRT_Diff = 'No data'


#  -----------------------------Routine    --HEAD / Routine_pneumatic block------ -----------------------------------------------
    try:
        selected_pneumatic = selected_index.routine_pneumatic_set.all().order_by('-id')[0]
        pneumatic_ECT_Diff = (selected_hour.ECT - selected_pneumatic.checked_ECT)
        pneumatic_MRT_Diff = (selected_hour.MRT - selected_pneumatic.checked_MRT)
    except:
        selected_pneumatic= 'No data'
        pneumatic_ECT_Diff = 'No data'
        pneumatic_MRT_Diff = 'No data'


# -----------------------------Routine    --HEAD / Routine_airfilter------ -----------------------------------------------
    try:
        selected_airfilter = selected_index.routine_airfilter_set.all().order_by('-id')[0]
        airfilter_ECT_Diff = (selected_hour.ECT - selected_airfilter.checked_ECT)
        airfilter_MRT_Diff = (selected_hour.MRT - selected_airfilter.checked_MRT)
    except:
        selected_airfilter= 'No data'
        airfilter_ECT_Diff = 'No data'
        airfilter_MRT_Diff = 'No data'        

 # -----------------------------Routine    --HEAD / Routine_xaxis------ -----------------------------------------------
    try:
        selected_xaxis = selected_index.routine_xaxis_set.all().order_by('-id')[0]
        xaxis_ECT_Diff = (selected_hour.ECT - selected_xaxis.checked_ECT)
        xaxis_MRT_Diff = (selected_hour.MRT - selected_xaxis.checked_MRT)
    except:
        selected_xaxis= 'No data'
        xaxis_ECT_Diff = 'No data'
        xaxis_MRT_Diff = 'No data'  


 # -----------------------------Routine    --HEAD / Routine_yaxis------ -----------------------------------------------
    try:
        selected_yaxis = selected_index.routine_yaxis_set.all().order_by('-id')[0]
        yaxis_ECT_Diff = (selected_hour.ECT - selected_yaxis.checked_ECT)
        yaxis_MRT_Diff = (selected_hour.MRT - selected_yaxis.checked_MRT)
    except:
        selected_yaxis= 'No data'
        yaxis_ECT_Diff = 'No data'
        yaxis_MRT_Diff = 'No data'  

 # -----------------------------Routine    --HEAD / Routine_coda------ -----------------------------------------------

    try:
        selected_coda = selected_index.routine_coda_set.all().order_by('-id')[0]
        coda_ECT_Diff = (selected_hour.ECT - selected_coda.checked_ECT)
        coda_MRT_Diff = (selected_hour.MRT - selected_coda.checked_MRT)
    except:
        selected_coda= 'No data'
        coda_ECT_Diff = 'No data'
        coda_MRT_Diff = 'No data'  

 # -----------------------------Routine    --HEAD / Routine_bristle------ -----------------------------------------------
    try:
        selected_bristle = selected_index.routine_bristle_set.all().order_by('-id')[0]
        bristle_ECT_Diff = (selected_hour.ECT - selected_bristle.checked_ECT)
        bristle_MRT_Diff = (selected_hour.MRT - selected_bristle.checked_MRT)
    except:
        selected_bristle= 'No data'
        bristle_ECT_Diff = 'No data'
        bristle_MRT_Diff = 'No data'  

# -----------------------------Routine    --HEAD / Routine_airinlet------ -----------------------------------------------
    try:
        selected_airinlet = selected_index.routine_airinlet_set.all().order_by('-id')[0]
        airinlet_ECT_Diff = (selected_hour.ECT - selected_airinlet.checked_ECT)
        airinlet_MRT_Diff = (selected_hour.MRT - selected_airinlet.checked_MRT)
    except:
        selected_airinlet = 'No data'
        airinlet_ECT_Diff = 'No data'
        airinlet_MRT_Diff = 'No data'  

# -----------------------------Routine    --HEAD / Routine_resultfabric------ -----------------------------------------------
    try:
        selected_resultfabric = selected_index.routine_resultfabric_set.all().order_by('-id')[0]
        resultfabric_ECT_Diff = (selected_hour.ECT - selected_resultfabric.checked_ECT)
        resultfabric_MRT_Diff = (selected_hour.MRT - selected_resultfabric.checked_MRT)
    except:
        selected_resultfabric = 'No data'
        resultfabric_ECT_Diff = 'No data'
        resultfabric_MRT_Diff = 'No data'  

  # -----------------------------Routine    --HEAD / Routine_elcabnet------ -----------------------------------------------

    try:
        selected_elcabnet = selected_index.routine_elcabnet_set.all().order_by('-id')[0]
        elcabnet_ECT_Diff = (selected_hour.ECT - selected_elcabnet.checked_ECT)
        elcabnet_MRT_Diff = (selected_hour.MRT - selected_elcabnet.checked_MRT)
    except:
        selected_elcabnet = 'No data'
        elcabnet_ECT_Diff = 'No data'
        elcabnet_MRT_Diff = 'No data'  




    context = {'selected_index':selected_index,
    'selected_hour':selected_hour,
    'selected_pressfoot':selected_pressfoot,'pressfoot_guide_ECT_Diff':pressfoot_guide_ECT_Diff,'pressfoot_guide_MRT_Diff':pressfoot_guide_MRT_Diff,
    'selected_bladeguide':selected_bladeguide,'blguide_ECT_Diff':blguide_ECT_Diff,'blguide_MRT_Diff':blguide_MRT_Diff,
    'selected_sharpning':selected_sharpning, 'sharpning_ECT_Diff':sharpning_ECT_Diff,'sharpning_MRT_Diff':sharpning_MRT_Diff,
    'selected_vibration':selected_vibration,'vibration_ECT_Diff':vibration_ECT_Diff,'vibration_MRT_Diff':vibration_MRT_Diff,
    'selected_rotation':selected_rotation,'rotation_ECT_Diff':rotation_ECT_Diff,'rotation_MRT_Diff':rotation_MRT_Diff,
    'selected_pneumatic':selected_pneumatic,'pneumatic_ECT_Diff':pneumatic_ECT_Diff,'pneumatic_MRT_Diff':pneumatic_MRT_Diff,
    'selected_airfilter':selected_airfilter,'airfilter_ECT_Diff':airfilter_ECT_Diff,'airfilter_MRT_Diff':airfilter_MRT_Diff,
    'selected_xaxis':selected_xaxis,'xaxis_ECT_Diff':xaxis_ECT_Diff,'xaxis_MRT_Diff':xaxis_MRT_Diff,
    'selected_yaxis':selected_yaxis,'yaxis_ECT_Diff':yaxis_ECT_Diff,'yaxis_MRT_Diff':yaxis_MRT_Diff,
    'selected_coda':selected_coda,'coda_ECT_Diff':coda_ECT_Diff,'coda_MRT_Diff':coda_MRT_Diff,
    'selected_bristle':selected_bristle,'bristle_ECT_Diff':bristle_ECT_Diff,'bristle_MRT_Diff':bristle_MRT_Diff,
    'selected_airinlet':selected_airinlet,'airinlet_ECT_Diff':airinlet_ECT_Diff,'airinlet_MRT_Diff':airinlet_MRT_Diff,
    'selected_resultfabric':selected_resultfabric,'resultfabric_ECT_Diff':resultfabric_ECT_Diff,'resultfabric_MRT_Diff':resultfabric_MRT_Diff,
    'selected_elcabnet':selected_elcabnet,'elcabnet_ECT_Diff':elcabnet_ECT_Diff,'elcabnet_MRT_Diff':elcabnet_MRT_Diff,

}

    return render(request, 'RoutineCheck_1.html', context)


  

  # -----------------------------Routine    press foot -----------------------------------------------
def routine_pressfoot(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]
    
    new_index = selected_index
    new_date = selected_hour.pub_date
    new_ECT = selected_hour.ECT
    new_MRT = selected_hour.MRT

    new_comment = request.POST['pressfoot_Comment']

    new_item1 = request.POST['pressfoot_Bearing']
    new_item2 = request.POST['pressfoot_Moving']
    new_item3 = request.POST['pressfoot_Lubrication']
    new_item4 = request.POST['pressfoot_Cleaning']

    new_object = Routine_pressfoot(index_fk=new_index, check_date=new_date, comment=new_comment,
    bearing_condition=new_item1, moving_condition=new_item2, lubrication_condition=new_item3, cleaning_condition=new_item4,
    checked_ECT=new_ECT, checked_MRT=new_MRT)
    
    new_object.save()
    
    return redirect('maintenance:routine_check_1', index_pk)


  # -----------------------------Routine    press foot -----------------------------------------------
def routine_bladeguide(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]
    
    new_index = selected_index
    new_date = selected_hour.pub_date
    new_ECT = selected_hour.ECT
    new_MRT = selected_hour.MRT
    new_comment = request.POST['guide_Comment']

    new_item1 = request.POST['guide_Plate']
    new_item2 = request.POST['guide_Roller']
    new_item3 = request.POST['guide_Fixed']
    new_item4 = request.POST['guide_Cleaning']

    new_object = Routine_bladeguide(index_fk=new_index, check_date=new_date, comment=new_comment,
    plate_condition=new_item1, roller_condition=new_item2, fixed_condition=new_item3, cleaning_condition=new_item4,
    checked_ECT=new_ECT, checked_MRT=new_MRT)
    
    new_object.save()
    
    return redirect('maintenance:routine_check_1', index_pk)


 # -----------------------------Routine    Sharping Arm -----------------------------------------------
# class Routine_sharpningarm(models.Model):
#     index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
#     check_date = models.DateField()
#     checked_ECT = models.IntegerField(default=0)
#     checked_MRT = models.IntegerField(default=0)
#     comment = models.TextField() 
#     Pully = models.BooleanField(default=True)
#     Sharpning = models.BooleanField(default=True)
#     Sharpning_wire = models.BooleanField(default=True)
#     Sharpning_Arm = models.BooleanField(default=True)
#     sharpning_Cleaning = models.BooleanField(default=True)

def routine_sharpningArm(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]
    
    new_index = selected_index
    new_date = selected_hour.pub_date
    new_ECT = selected_hour.ECT
    new_MRT = selected_hour.MRT
    new_comment = request.POST['sharpning_Comment']

    new_item1 = request.POST['sharpning_Pully']
    new_item2 = request.POST['Sharpning']
    new_item3 = request.POST['Sharpning_wire']
    new_item4 = request.POST['Sharpning_Arm']
    new_item5 = request.POST['sharpning_Cleaning']

    new_object = Routine_sharpningarm(index_fk=new_index, check_date=new_date, comment=new_comment,
    Sharpning_Pully=new_item1, Sharpning=new_item2, Sharpning_wire=new_item3, Sharpning_Arm=new_item4, sharpning_Cleaning=new_item5,
    checked_ECT=new_ECT, checked_MRT=new_MRT)
    
    new_object.save()
    
    return redirect('maintenance:routine_check_1', index_pk)



 # -----------------------------Routine    --HEAD / Vibration Parts------ -----------------------------------------------
# class Routine_vibration(models.Model):
#     index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
#     check_date = models.DateField()
#     checked_ECT = models.IntegerField(default=0)
#     checked_MRT = models.IntegerField(default=0)
#     comment = models.TextField() 
#     vibration_moving = models.BooleanField(default=True)
#     vibration_vibearing = models.BooleanField(default=True)
#     vibration_nibearing = models.BooleanField(default=True)
#     vibration_belt = models.BooleanField(default=True)
#     vibration_Cleaning = models.BooleanField(default=True)

def routine_vibration(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]
    
    new_index = selected_index
    new_date = selected_hour.pub_date
    new_ECT = selected_hour.ECT
    new_MRT = selected_hour.MRT
    new_comment = request.POST['vibration_Comment']

    new_item1 = request.POST['vibration_moving']
    new_item2 = request.POST['vibration_vibearing']
    new_item3 = request.POST['vibration_nibearing']
    new_item4 = request.POST['vibration_belt']
    new_item5 = request.POST['vibration_Cleaning']

    new_object = Routine_vibration(index_fk=new_index, check_date=new_date, comment=new_comment,
    vibration_moving=new_item1, vibration_vibearing=new_item2, vibration_nibearing=new_item3, vibration_belt=new_item4, vibration_Cleaning=new_item5,
    checked_ECT=new_ECT, checked_MRT=new_MRT)
    
    new_object.save()
    
    return redirect('maintenance:routine_check_1', index_pk)




 # -----------------------------Routine    --HEAD / rotation block------ -----------------------------------------------
# class Routine_rotationblock(models.Model):
#     index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
#     check_date = models.DateField()
#     checked_ECT = models.IntegerField(default=0)
#     checked_MRT = models.IntegerField(default=0)
#     rotation_Comment = models.TextField() 
#     rotation_moving = models.BooleanField(default=True)
#     rotation_Belt = models.BooleanField(default=True)
#     rotation_Fixed = models.BooleanField(default=True)
#     rotation_cleaning = models.BooleanField(default=True)

def routine_rotation(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]
    
    new_index = selected_index
    new_date = selected_hour.pub_date
    new_ECT = selected_hour.ECT
    new_MRT = selected_hour.MRT
    new_comment = request.POST['rotation_Comment']

    new_item1 = request.POST['rotation_moving']
    new_item2 = request.POST['rotation_Belt']
    new_item3 = request.POST['rotation_Fixed']
    new_item4 = request.POST['rotation_cleaning']
   

    new_object = Routine_rotationblock(index_fk=new_index, check_date=new_date, rotation_Comment=new_comment,
    rotation_moving=new_item1, rotation_Belt=new_item2, rotation_Fixed=new_item3, rotation_cleaning=new_item4,
    checked_ECT=new_ECT, checked_MRT=new_MRT)
    
    new_object.save()
    
    return redirect('maintenance:routine_check_1', index_pk)



    
#  -----------------------------Routine    --HEAD / Routine_pneumatic block------ -----------------------------------------------
# class Routine_pneumatic(models.Model):
#     index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
#     check_date = models.DateField()
#     checked_ECT = models.IntegerField(default=0)
#     checked_MRT = models.IntegerField(default=0)
#     pneumatic_Comment = models.TextField() 
#     pneumatic_hose = models.BooleanField(default=True)
#     pneumatic_bladeCylinder = models.BooleanField(default=True)
#     pneumatic_pressfootcylinder = models.BooleanField(default=True)
#     pneumatic_Drill = models.BooleanField(default=True)
#     pneumatic_Sharpning = models.BooleanField(default=True)

def routine_pneumaticblock(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]
    
    new_index = selected_index
    new_date = selected_hour.pub_date
    new_ECT = selected_hour.ECT
    new_MRT = selected_hour.MRT
    new_comment = request.POST['pneumatic_Comment']

    new_item1 = request.POST['pneumatic_hose']
    new_item2 = request.POST['pneumatic_bladeCylinder']
    new_item3 = request.POST['pneumatic_pressfootcylinder']
    new_item4 = request.POST['pneumatic_Drill']
    new_item5 = request.POST['pneumatic_Sharpning']
   

    new_object = Routine_pneumatic(index_fk=new_index, check_date=new_date, pneumatic_Comment=new_comment,
    pneumatic_hose=new_item1, pneumatic_bladeCylinder=new_item2, pneumatic_pressfootcylinder=new_item3, pneumatic_Drill=new_item4,
    pneumatic_Sharpning=new_item5,
    checked_ECT=new_ECT, checked_MRT=new_MRT)
    
    new_object.save()
    
    return redirect('maintenance:routine_check_1', index_pk)




     # -----------------------------Routine    --HEAD / Routine_airfilter------ -----------------------------------------------
# class Routine_airfilter(models.Model):
#     index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
#     check_date = models.DateField()
#     checked_ECT = models.IntegerField(default=0)
#     checked_MRT = models.IntegerField(default=0)
#     airfilter_Comment = models.TextField() 
#     airfilter_cool = models.BooleanField(default=True)
#     airfilter_Vaccum = models.BooleanField(default=True)

def routine_airfilter(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]
    
    new_index = selected_index
    new_date = selected_hour.pub_date
    new_ECT = selected_hour.ECT
    new_MRT = selected_hour.MRT
    new_comment = request.POST['airfilter_Comment']

    new_item1 = request.POST['airfilter_cool']
    new_item2 = request.POST['airfilter_Vaccum']

   

    new_object = Routine_airfilter(index_fk=new_index, check_date=new_date, airfilter_Comment=new_comment,
    airfilter_cool=new_item1, airfilter_Vaccum=new_item2,
    checked_ECT=new_ECT, checked_MRT=new_MRT)
    
    new_object.save()
    
    return redirect('maintenance:routine_check_1', index_pk)




    
 # -----------------------------Routine    --HEAD / Routine_xaxis------ -----------------------------------------------
# class Routine_xaxis(models.Model):
#     index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
#     check_date = models.DateField()
#     checked_ECT = models.IntegerField(default=0)
#     checked_MRT = models.IntegerField(default=0)
#     xaxis_Comment = models.TextField() 
#     xaxis_rail = models.BooleanField(default=True)
#     xaxis_Cleaning = models.BooleanField(default=True)
#     xaxis_plasticgear = models.BooleanField(default=True)


def routine_xaxis(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]
    
    new_index = selected_index
    new_date = selected_hour.pub_date
    new_ECT = selected_hour.ECT
    new_MRT = selected_hour.MRT
    new_comment = request.POST['xaxis_Comment']

    new_item1 = request.POST['xaxis_rail']
    new_item2 = request.POST['xaxis_Cleaning']
    new_item3 = request.POST['xaxis_plasticgear']

   

    new_object = Routine_xaxis(index_fk=new_index, check_date=new_date, xaxis_Comment=new_comment,
    xaxis_rail=new_item1, xaxis_Cleaning=new_item2, xaxis_plasticgear=new_item3,
    checked_ECT=new_ECT, checked_MRT=new_MRT)
    
    new_object.save()
    
    return redirect('maintenance:routine_check_1', index_pk)


    
 # -----------------------------Routine    --HEAD / Routine_yaxis------ -----------------------------------------------
# class Routine_yaxis(models.Model):
#     index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
#     check_date = models.DateField()
#     checked_ECT = models.IntegerField(default=0)
#     checked_MRT = models.IntegerField(default=0)
#     yaxis_Comment = models.TextField() 
#     yaxis_rail = models.BooleanField(default=True)
#     yaxis_Cleaning = models.BooleanField(default=True)


def routine_yaxis(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]
    
    new_index = selected_index
    new_date = selected_hour.pub_date
    new_ECT = selected_hour.ECT
    new_MRT = selected_hour.MRT
    new_comment = request.POST['yaxis_Comment']

    new_item1 = request.POST['yaxis_rail']
    new_item2 = request.POST['yaxis_Cleaning']

   

    new_object = Routine_yaxis(index_fk=new_index, check_date=new_date, yaxis_Comment=new_comment,
    yaxis_rail=new_item1, yaxis_Cleaning=new_item2,
    checked_ECT=new_ECT, checked_MRT=new_MRT)
    
    new_object.save()
    
    return redirect('maintenance:routine_check_1', index_pk)



 # -----------------------------Routine    --HEAD / Routine_coda------ -----------------------------------------------
# class Routine_coda(models.Model):
#     index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
#     check_date = models.DateField()
#     checked_ECT = models.IntegerField(default=0)
#     checked_MRT = models.IntegerField(default=0)
#     coda_Comment = models.TextField()
#     coda_belt = models.BooleanField(default=True)
#     coda_consol = models.BooleanField(default=True)
#     coda_moving = models.BooleanField(default=True)


def routine_coda(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]
    
    new_index = selected_index
    new_date = selected_hour.pub_date
    new_ECT = selected_hour.ECT
    new_MRT = selected_hour.MRT
    new_comment = request.POST['coda_Comment']

    new_item1 = request.POST['coda_belt']
    new_item2 = request.POST['coda_consol']
    new_item3 = request.POST['coda_moving']

   

    new_object = Routine_coda(index_fk=new_index, check_date=new_date, coda_Comment=new_comment,
    coda_belt=new_item1, coda_consol=new_item2, coda_moving=new_item3,
    checked_ECT=new_ECT, checked_MRT=new_MRT)
    
    new_object.save()
    
    return redirect('maintenance:routine_check_1', index_pk)



     # -----------------------------Routine    --HEAD / Routine_bristle------ -----------------------------------------------
# class Routine_bristle(models.Model):
#     index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
#     check_date = models.DateField()
#     checked_ECT = models.IntegerField(default=0)
#     checked_MRT = models.IntegerField(default=0)
#     bristle_Comment = models.TextField()
#     bristle_comb = models.BooleanField(default=True)
#     bristle_moving = models.BooleanField(default=True)


def routine_bristle(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]
    
    new_index = selected_index
    new_date = selected_hour.pub_date
    new_ECT = selected_hour.ECT
    new_MRT = selected_hour.MRT
    new_comment = request.POST['bristle_Comment']

    new_item1 = request.POST['bristle_comb']
    new_item2 = request.POST['bristle_moving']
   

   

    new_object = Routine_bristle(index_fk=new_index, check_date=new_date, bristle_Comment=new_comment,
    bristle_comb=new_item1, bristle_moving=new_item2,
    checked_ECT=new_ECT, checked_MRT=new_MRT)
    
    new_object.save()
    
    return redirect('maintenance:routine_check_1', index_pk)


# -----------------------------Routine    --HEAD / Routine_airinlet------ -----------------------------------------------
# class Routine_airinlet(models.Model):
#     index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
#     check_date = models.DateField()
#     checked_ECT = models.IntegerField(default=0)
#     checked_MRT = models.IntegerField(default=0)
#     airinlet_Comment = models.TextField()
#     airinlet_Regulator = models.BooleanField(default=True)
#     airinlet_Separator = models.BooleanField(default=True)
#     airinlet_setting = models.BooleanField(default=True)
#     airinlet_pressure = models.BooleanField(default=True)

def routine_airinlet(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]
    
    new_index = selected_index
    new_date = selected_hour.pub_date
    new_ECT = selected_hour.ECT
    new_MRT = selected_hour.MRT
    new_comment = request.POST['airinlet_Comment']

    new_item1 = request.POST['airinlet_Regulator']
    new_item2 = request.POST['airinlet_Separator']
    new_item3 = request.POST['airinlet_setting']
    new_item4 = request.POST['airinlet_pressure']
   

    new_object = Routine_airinlet(index_fk=new_index, check_date=new_date, airinlet_Comment=new_comment,
    airinlet_Regulator=new_item1, airinlet_Separator=new_item2,airinlet_setting=new_item3,airinlet_pressure=new_item4,
    checked_ECT=new_ECT, checked_MRT=new_MRT)
    
    new_object.save()
    
    return redirect('maintenance:routine_check_1', index_pk)



# -----------------------------Routine    --HEAD / Routine_resultfabric------ -----------------------------------------------
# class Routine_resultfabric(models.Model):
#     index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
#     check_date = models.DateField()
#     checked_ECT = models.IntegerField(default=0)
#     checked_MRT = models.IntegerField(default=0)
#     result_Comment = models.TextField()
#     result_surface = models.BooleanField(default=True)
#     result_notch = models.BooleanField(default=True)
#     result_inangle = models.BooleanField(default=True)
#     result_outangle = models.BooleanField(default=True)

def routine_resultfabric(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]
    
    new_index = selected_index
    new_date = selected_hour.pub_date
    new_ECT = selected_hour.ECT
    new_MRT = selected_hour.MRT
    new_comment = request.POST['result_Comment']

    new_item1 = request.POST['result_surface']
    new_item2 = request.POST['result_notch']
    new_item3 = request.POST['result_inangle']
    new_item4 = request.POST['result_outangle']
   

    new_object = Routine_resultfabric(index_fk=new_index, check_date=new_date, result_Comment=new_comment,
    result_surface=new_item1, result_notch=new_item2,result_inangle=new_item3,result_outangle=new_item4,
    checked_ECT=new_ECT, checked_MRT=new_MRT)
    
    new_object.save()
    
    return redirect('maintenance:routine_check_1', index_pk)



  # -----------------------------Routine    --HEAD / Routine_elcabnet------ -----------------------------------------------
# class Routine_elcabnet(models.Model):
#     index_fk = models.ForeignKey(index, on_delete=models.CASCADE)
#     check_date = models.DateField()
#     checked_ECT = models.IntegerField(default=0)
#     checked_MRT = models.IntegerField(default=0)
#     elec_Comment = models.TextField()
#     elec_board = models.BooleanField(default=True)
#     elec_Cable = models.BooleanField(default=True)
#     elec_4axis = models.BooleanField(default=True)
#     elec_cleaning = models.BooleanField(default=True)

def routine_elecabinet(request, index_pk):
    selected_index = index.objects.get(pk=index_pk)
    selected_hour = selected_index.running_hour_set.all().order_by('-pub_date')[0]
    
    new_index = selected_index
    new_date = selected_hour.pub_date
    new_ECT = selected_hour.ECT
    new_MRT = selected_hour.MRT
    new_comment = request.POST['elec_Comment']

    new_item1 = request.POST['elec_board']
    new_item2 = request.POST['elec_Cable']
    new_item3 = request.POST['elec_4axis']
    new_item4 = request.POST['elec_cleaning']
   

    new_object = Routine_elcabnet(index_fk=new_index, check_date=new_date, elec_Comment=new_comment,
    elec_board=new_item1, elec_Cable=new_item2,elec_4axis=new_item3,elec_cleaning=new_item4,
    checked_ECT=new_ECT, checked_MRT=new_MRT)
    
    new_object.save()
    
    return redirect('maintenance:routine_check_1', index_pk)



    
