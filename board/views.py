from django.shortcuts import render, redirect
from django.http import HttpResponse
from maintenance.models import *
from index.models import index

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# class index(models.Model):
#     site_name = models.CharField(max_length=100)
#     site_address = models.CharField(max_length=200)
#     machine_type = models.CharField(max_length=100) #auto or fashion
#     machine_model = models.CharField(max_length=100) #iQ80-71
#     machine_number = models.CharField(max_length=100, null=True, blank=True, default='Serial_Number')

def board(request):
    if request.user.is_authenticated:

        select_site = index.objects.all().order_by('site_name')

        context={'select_site':select_site} 

        return render(request, 'all_board.html', context)
    else:
        return redirect('account:Login')



def board_list_enterance(request, index_pk):

    if request.user.is_authenticated:

        select_site = index.objects.all().order_by('site_name')

        selected_site = index.objects.get(pk=index_pk)

        count_Breakfix = selected_site.breakfix_set.all().count()
        count_Pmaudit = selected_site.pmaudit_set.all().count()
        count_ETC = selected_site.etc_set.all().count()
        count_overhaul = selected_site.overhaul_set.all().count()
        # count_routine = selected_site.pmaudit_set.all().count()
    

        context={'select_site':select_site, 'selected_site':selected_site, 'count_Breakfix':count_Breakfix,
        'count_Pmaudit':count_Pmaudit, 'count_ETC':count_ETC, 'count_overhaul':count_overhaul} 

        return render(request, 'all_board_enterance.html', context)
    else:
        return redirect('account:Login')



def breakfix_board(request, index_pk):
    select_site = index.objects.all().order_by('site_name')

    request_site = index_pk
    selected_site = index.objects.get(pk=request_site)

    articles = selected_site.breakfix_set.all().order_by('-checked_date', '-checked_ECT', '-checked_MRT')

    page = request.GET.get('pageBREAKFIX', 1)
    paginator = Paginator(articles, 5)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context={'select_site':select_site, 'selected_site':selected_site, 
    'articles':articles,
    }

    return render(request, 'Breakfix_board.html', context)


def breakfix_board_add(request, index_pk):
    if request.method == 'GET':
        selected_site = index.objects.get(pk=index_pk)

        context={'selected_site':selected_site} 

        return render(request, 'Breakfix_board_add.html', context)

    else:
        selected_index = index.objects.get(pk=index_pk)
 
        subject = request.POST['subject']
        issue = request.POST['issue']
        title = request.POST['title']
        comment = request.POST['comment']


        checked_date = request.POST['Today_Date']
        checked_ECT = request.POST['ECT']
        checked_MRT = request.POST['MRT']

 
        new_objects = Breakfix(issue=issue, subject=subject, title=title, comment=comment,
        checked_date=checked_date, checked_ECT=checked_ECT, checked_MRT=checked_MRT,
        index_fk = selected_index)
        new_objects.save()

        return redirect('board:breakfix_board', selected_index.id)



def breakfix_board_modify(request, index_pk, modify_pk):
    if request.method == 'GET':
        selected_site = index.objects.get(pk=index_pk)
        selected_article = Breakfix.objects.get(pk=modify_pk)

        context={'selected_site':selected_site, 'selected_article':selected_article} 

        return render(request, 'Breakfix_board_modify.html', context)

    else:
        selected_index = index.objects.get(pk=index_pk)
        selected_article = Breakfix.objects.get(pk=modify_pk)
 
        subject = request.POST['subject']
        issue = request.POST['issue']
        title = request.POST['title']
        comment = request.POST['comment']
        index_fk = selected_index

        checked_date = request.POST['Today_Date']
        checked_ECT = request.POST['ECT']
        checked_MRT = request.POST['MRT']

        selected_article.subject = subject
        selected_article.issue = issue
        selected_article.title = title
        selected_article.comment = comment
        selected_article.checked_date = checked_date
        selected_article.checked_ECT = checked_ECT
        selected_article.checked_MRT = checked_MRT
        selected_article.index_fk = index_fk

        selected_article.save()

        return redirect('board:breakfix_board', selected_index.id)



def breakfix_board_delete(request, index_pk, modify_pk):
    if request.method == 'GET':
        selected_site = index.objects.get(pk=index_pk)
        selected_article = Breakfix.objects.get(pk=modify_pk)

        selected_article.delete()

        context={'selected_site':selected_site, 'selected_article':selected_article} 

        return redirect('board:breakfix_board', selected_site.id)


# -----------------------------------------------------------------------------------------------------------------

def ETC_board(request, index_pk):
    select_site = index.objects.all().order_by('site_name')

    request_site = index_pk
    selected_site = index.objects.get(pk=request_site)

    articles = selected_site.etc_set.all().order_by('-checked_date', '-checked_ECT', '-checked_MRT')

    page = request.GET.get('pageBREAKFIX', 1)
    paginator = Paginator(articles, 5)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)




    context={'select_site':select_site, 'selected_site':selected_site, 
    'articles':articles,
    }

    return render(request, 'ETC_board.html', context)




def ETC_board_add(request, index_pk):
    if request.method == 'GET':
        selected_site = index.objects.get(pk=index_pk)

        context={'selected_site':selected_site} 

        return render(request, 'ETC_board_add.html', context)

    else:
        selected_index = index.objects.get(pk=index_pk)
 
        subject = request.POST['subject']
        # issue = request.POST['issue']
        title = request.POST['title']
        comment = request.POST['comment']


        checked_date = request.POST['Today_Date']
        checked_ECT = request.POST['ECT']
        checked_MRT = request.POST['MRT']

 
        new_objects = ETC(subject=subject, title=title, comment=comment,
        checked_date=checked_date, checked_ECT=checked_ECT, checked_MRT=checked_MRT,
        index_fk = selected_index)
        new_objects.save()

        return redirect('board:ETC_board', selected_index.id)



def ETC_board_modify(request, index_pk, modify_pk):
    if request.method == 'GET':
        selected_site = index.objects.get(pk=index_pk)
        selected_article = ETC.objects.get(pk=modify_pk)

        context={'selected_site':selected_site, 'selected_article':selected_article} 

        return render(request, 'ETC_board_modify.html', context)

    else:
        selected_index = index.objects.get(pk=index_pk)
        selected_article = ETC.objects.get(pk=modify_pk)
 
        subject = request.POST['subject']
        # issue = request.POST['issue']
        title = request.POST['title']
        comment = request.POST['comment']
        index_fk = selected_index

        checked_date = request.POST['Today_Date']
        checked_ECT = request.POST['ECT']
        checked_MRT = request.POST['MRT']

        selected_article.subject = subject
        # selected_article.issue = issue
        selected_article.title = title
        selected_article.comment = comment
        selected_article.checked_date = checked_date
        selected_article.checked_ECT = checked_ECT
        selected_article.checked_MRT = checked_MRT
        selected_article.index_fk = index_fk

        selected_article.save()

        return redirect('board:ETC_board', selected_index.id)


def ETC_board_delete(request, index_pk, modify_pk):
    if request.method == 'GET':
        selected_site = index.objects.get(pk=index_pk)
        selected_article = ETC.objects.get(pk=modify_pk)

        selected_article.delete()

        context={'selected_site':selected_site, 'selected_article':selected_article} 

        return redirect('board:ETC_board', selected_site.id)



# -------------------------------------------------------------------------------------------------------------


def PMAUDIT_board(request, index_pk):
    select_site = index.objects.all().order_by('site_name')

    request_site = index_pk
    selected_site = index.objects.get(pk=request_site)

    articles = selected_site.pmaudit_set.all().order_by('-checked_date', '-checked_ECT', '-checked_MRT')

    page = request.GET.get('pageBREAKFIX', 1)
    paginator = Paginator(articles, 5)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)




    context={'select_site':select_site, 'selected_site':selected_site, 
    'articles':articles,
    }

    return render(request, 'PMAUDIT_board.html', context)





def PMAUDIT_board_add(request, index_pk):
    if request.method == 'GET':
        selected_site = index.objects.get(pk=index_pk)

        context={'selected_site':selected_site} 

        return render(request, 'PMAUDIT_board_add.html', context)

    else:
        selected_index = index.objects.get(pk=index_pk)
 
        subject = request.POST['subject']
        # issue = request.POST['issue']
        title = request.POST['title']
        comment = request.POST['comment']


        checked_date = request.POST['Today_Date']
        checked_ECT = request.POST['ECT']
        checked_MRT = request.POST['MRT']

 
        new_objects = PmAudit(subject=subject, title=title, comment=comment,
        checked_date=checked_date, checked_ECT=checked_ECT, checked_MRT=checked_MRT,
        index_fk = selected_index)
        new_objects.save()

        return redirect('board:PMAUDIT_board', selected_index.id)


def PMAUDIT_board_modify(request, index_pk, modify_pk):
    if request.method == 'GET':
        selected_site = index.objects.get(pk=index_pk)
        selected_article = PmAudit.objects.get(pk=modify_pk)

        context={'selected_site':selected_site, 'selected_article':selected_article} 

        return render(request, 'PMAUDIT_board_modify.html', context)

    else:
        selected_index = index.objects.get(pk=index_pk)
        selected_article = PmAudit.objects.get(pk=modify_pk)
 
        subject = request.POST['subject']
        # issue = request.POST['issue']
        title = request.POST['title']
        comment = request.POST['comment']
        index_fk = selected_index

        checked_date = request.POST['Today_Date']
        checked_ECT = request.POST['ECT']
        checked_MRT = request.POST['MRT']

        selected_article.subject = subject
        # selected_article.issue = issue
        selected_article.title = title
        selected_article.comment = comment
        selected_article.checked_date = checked_date
        selected_article.checked_ECT = checked_ECT
        selected_article.checked_MRT = checked_MRT
        selected_article.index_fk = index_fk

        selected_article.save()

        return redirect('board:PMAUDIT_board', selected_index.id)


def PMAUDIT_board_delete(request, index_pk, modify_pk):
    if request.method == 'GET':
        selected_site = index.objects.get(pk=index_pk)
        selected_article = PmAudit.objects.get(pk=modify_pk)

        selected_article.delete()

        context={'selected_site':selected_site, 'selected_article':selected_article} 

        return redirect('board:PMAUDIT_board', selected_site.id)






# ------------------------------------------------------------------------------------------------------------------------



def overhaul_board(request, index_pk):
    select_site = index.objects.all().order_by('site_name')

    request_site = index_pk
    selected_site = index.objects.get(pk=request_site)

    articles = selected_site.overhaul_set.all().order_by('-checked_date', '-checked_ECT', '-checked_MRT')

    page = request.GET.get('pageBREAKFIX', 1)
    paginator = Paginator(articles, 5)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)




    context={'select_site':select_site, 'selected_site':selected_site, 
    'articles':articles,
    }

    return render(request, 'overhaul_board.html', context)





def overhaul_board_add(request, index_pk):
    if request.method == 'GET':
        selected_site = index.objects.get(pk=index_pk)

        context={'selected_site':selected_site} 

        return render(request, 'overhaul_board_add.html', context)

    else:
        selected_index = index.objects.get(pk=index_pk)
 
        subject = request.POST['subject']
        # issue = request.POST['issue']
        title = request.POST['title']
        comment = request.POST['comment']


        checked_date = request.POST['Today_Date']
        checked_ECT = request.POST['ECT']
        checked_MRT = request.POST['MRT']

 
        new_objects = Overhaul(subject=subject, title=title, comment=comment,
        checked_date=checked_date, checked_ECT=checked_ECT, checked_MRT=checked_MRT,
        index_fk = selected_index)
        new_objects.save()

        return redirect('board:overhaul_board', selected_index.id)


def overhaul_board_modify(request, index_pk, modify_pk):
    if request.method == 'GET':
        selected_site = index.objects.get(pk=index_pk)
        selected_article = PmAudit.objects.get(pk=modify_pk)

        context={'selected_site':selected_site, 'selected_article':selected_article} 

        return render(request, 'overhaul_board_modify.html', context)

    else:
        selected_index = index.objects.get(pk=index_pk)
        selected_article = Overhaul.objects.get(pk=modify_pk)
 
        subject = request.POST['subject']
        # issue = request.POST['issue']
        title = request.POST['title']
        comment = request.POST['comment']
        index_fk = selected_index

        checked_date = request.POST['Today_Date']
        checked_ECT = request.POST['ECT']
        checked_MRT = request.POST['MRT']

        selected_article.subject = subject
        # selected_article.issue = issue
        selected_article.title = title
        selected_article.comment = comment
        selected_article.checked_date = checked_date
        selected_article.checked_ECT = checked_ECT
        selected_article.checked_MRT = checked_MRT
        selected_article.index_fk = index_fk

        selected_article.save()

        return redirect('board:overhaul_board', selected_index.id)


def overhaul_board_delete(request, index_pk, modify_pk):
    if request.method == 'GET':
        selected_site = index.objects.get(pk=index_pk)
        selected_article = Overhaul.objects.get(pk=modify_pk)

        selected_article.delete()

        context={'selected_site':selected_site, 'selected_article':selected_article} 

        return redirect('board:overhaul_board', selected_site.id)








# ============================================= 수 정 중 ======================================================

def board_search(request, index_pk):
   
    select_site = index.objects.all().order_by('site_name')

    request_site = index_pk
    selected_object = index.objects.get(pk=request_site)

# break fix--------------------------------------------------------------------------------------------------
    selected_breakfix = selected_object.breakfix_set.all().order_by('-checked_date')

    page = request.GET.get('pageBREAKFIX', 1)
    paginator = Paginator(selected_breakfix, 4)
    try:
        breakfix_articles = paginator.page(page)
    except PageNotAnInteger:
        breakfix_articles = paginator.page(1)
    except EmptyPage:
        breakfix_articles = paginator.page(paginator.num_pages)

# ETC --------------------------------------------------------------------------------------------------
    
    selected_ETC = selected_object.etc_set.all().order_by('-checked_date', '-checked_ECT')
    
    page = request.GET.get('pageETC', 1)
    paginator = Paginator(selected_ETC, 4)
    try:
        ETC_articles = paginator.page(page)
    except PageNotAnInteger:
        ETC_articles = paginator.page(1)
    except EmptyPage:
        ETC_articles = paginator.page(paginator.num_pages)


# Pm audit --------------------------------------------------------------------------------------------------
    
    selected_pmaudit = selected_object.pmaudit_set.all().order_by('-checked_date', '-checked_ECT')
    
    page = request.GET.get('page', 1)
    paginator = Paginator(selected_pmaudit, 4)
    try:
        pmaudit_articles = paginator.page(page)
    except PageNotAnInteger:
        pmaudit_articles = paginator.page(1)
    except EmptyPage:
        pmaudit_articles = paginator.page(paginator.num_pages)



# Overhaul --------------------------------------------------------------------------------------------------
    
    selected_overhaul = selected_object.overhaul_set.all().order_by('-checked_date', '-checked_ECT')
    
    page = request.GET.get('page', 1)
    paginator = Paginator(selected_overhaul, 4)
    try:
        pmaudit_articles = paginator.page(page)
    except PageNotAnInteger:
        pmaudit_articles = paginator.page(1)
    except EmptyPage:
        pmaudit_articles = paginator.page(paginator.num_pages)





    context={'select_site':select_site, 'selected_object':selected_object, 'selected_breakfix':selected_breakfix, 'breakfix_articles':breakfix_articles,
    'selected_ETC':selected_ETC, 'ETC_articles':ETC_articles , 'pmaudit_articles':pmaudit_articles}

    return render(request, 'all_board_search.html', context)













# ---------------------------------------------------------------------------------------------












# ---------------------------------------------------------------------------------------------


