from django.shortcuts import render, redirect
from .models import index
from maintenance.models import Running_hour
from django.http import HttpResponse
from django.forms.models import model_to_dict   #<-- 추가된 함수 

from django.contrib.auth.models import User
from django.contrib import auth



def Index(request):

    if request.user.is_authenticated:

        index_list = index.objects.all()
        results = []  #render 로 template 넘어갈 list  
        
        for indexs in index_list:
            index_dict = model_to_dict(indexs)  #model to dict 

            try:   # try , except 안쓸시 빈 테이블시 에어 발생 , list out range error
                latest_running_hour = indexs.running_hour_set.all().order_by('-pub_date')[0] #select running hour object by ( _set )
                latest_hour_dict = model_to_dict(latest_running_hour)  #convert selected model object 'latest_running_hour' to dict
        
        # -- Method 1 -----------------------------------------------------------------------------------------------------
        # delete 'id' key and value of selected Running_hour object for prevent duplicate with index table's 'id'
        # then add 'latest_hour_dict' dictionalry value to index_dict

            # del latest_hour_dict['id']                              
            # index_dict.update(latest_hour_dict)

    #--Method 2 ------------------------------------------------------------------------------------------------       
                index_dict['pub_date'] = latest_hour_dict['pub_date']
                index_dict['ECT'] = latest_hour_dict['ECT']
                index_dict['MRT'] = latest_hour_dict['MRT']
            except: #list out range 이면 아래 값이 넘어간다 
                index_dict['pub_date'] = 'YYYY-MM-DD'
                index_dict['ECT'] = '0000'
                index_dict['MRT'] ='0000'
                
            results.append(index_dict)

        # first_index = index.objects.get(id=1)
        # last_hours_of_first_index = first_index.Running_hour_set.all()
        # array = [1,2,3,4,5]
        # array[1] = 2
        # array[1:2] = [2]
        # array[1:2][0] = 2

        context = {'results': results}
        # results = context['results']

        return render(request, 'index.html', context)
    else:
        return redirect('account:Login')




def modify_site(request, pk):
    if request.method =='POST':
        site_name = request.POST['site_name']
        site_address = request.POST['site_address']
        machine_type = request.POST['machine_type']
        machine_model = request.POST['machine_model']
        machine_number = request.POST['machine_number']

        selected_site = index.objects.get(pk=pk)
        selected_site.site_name = site_name
        selected_site.site_address = site_address
        selected_site.machine_model = machine_model
        selected_site.machine_type = machine_type
        selected_site.machine_number = machine_number
        selected_site.save()
        return redirect('/index/')
    
    
    else:
        selected_site = index.objects.get(pk=pk)
        context = {'site':selected_site}
        return render(request, 'modify_site.html', context)




def delete_site(request, pk):
    if request.method == 'POST':
        selected_site = index.objects.get(pk=pk)
        selected_site.delete()
        return redirect('/index/')
        
    else:
        selected_site = index.objects.get(pk=pk)
        context = {'selected_site':selected_site}
        return render(request, 'delete_site.html', context)



def add_site(request):
    if request.method =='POST':
        site_name = request.POST['site_name']
        site_address = request.POST['site_address']
        machine_type = request.POST['machine_type']
        machine_model = request.POST['machine_model']
        machine_number = request.POST['machine_number']
        new_site = index(site_name=site_name, site_address=site_address, 
        machine_type=machine_type, machine_model=machine_model, machine_number=machine_number)
        new_site.save()
        return redirect('/index/')

    else:    
        return render(request, 'add_site.html')