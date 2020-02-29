from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'board'

urlpatterns = [
    path('', board, name='board'), 
    path('board_search/<int:index_pk>', board_search, name='board_search'), 
    path('board_list_enterance/<int:index_pk>', board_list_enterance, name='board_list_enterance'),

    path('breakfix_board/<int:index_pk>', breakfix_board, name='breakfix_board'),
    path('breakfix_board_modify/<int:index_pk>/<int:modify_pk>', breakfix_board_modify, name='breakfix_board_modify'), 
    path('breakfix_board_delete/<int:index_pk>/<int:modify_pk>', breakfix_board_delete, name='breakfix_board_delete'),
    path('breakfix_board_add/<int:index_pk>', breakfix_board_add, name='breakfix_board_add'), 


    path('ETC_board/<int:index_pk>', ETC_board, name='ETC_board'),
    path('ETC_board_add/<int:index_pk>', ETC_board_add, name='ETC_board_add'), 
    path('ETC_board_modify/<int:index_pk>/<int:modify_pk>', ETC_board_modify, name='ETC_board_modify'), 
    path('ETC_board_delete/<int:index_pk>/<int:modify_pk>', ETC_board_delete, name='ETC_board_delete'),  


    path('PMAUDIT_board/<int:index_pk>', PMAUDIT_board, name='PMAUDIT_board'),
    path('PMAUDIT_board_add/<int:index_pk>', PMAUDIT_board_add, name='PMAUDIT_board_add'), 
    path('PMAUDIT_board_modify/<int:index_pk>/<int:modify_pk>', PMAUDIT_board_modify, name='PMAUDIT_board_modify'), 
    path('PMAUDIT_board_delete/<int:index_pk>/<int:modify_pk>', PMAUDIT_board_delete, name='PMAUDIT_board_delete'),


    path('overhaul_board/<int:index_pk>', overhaul_board, name='overhaul_board'),
    path('overhaul_board_add/<int:index_pk>', overhaul_board_add, name='overhaul_board_add'), 
    path('overhaul_board_modify/<int:index_pk>/<int:modify_pk>', overhaul_board_modify, name='overhaul_board_modify'), 
    path('overhaul_board_delete/<int:index_pk>/<int:modify_pk>', overhaul_board_delete, name='overhaul_board_delete'),




# =================================================수 정 중 ==================================================================

    # -----------------------------------------------------------------------------------------------------------------
    # path('breakfix_board_add/<int:index_pk>', breakfix_board_add, name='breakfix_board_add'), 
    # path('breakfix_board_modify/<int:index_pk>/<int:modify_pk>', breakfix_board_modify, name='breakfix_board_modify'), 
    # path('breakfix_board_delete/<int:index_pk>/<int:modify_pk>', breakfix_board_delete, name='breakfix_board_delete'),
    # -----------------------------------------------------------------------------------------------------------------------
    # path('ETC_board_add/<int:index_pk>', ETC_board_add, name='ETC_board_add'), 
    # path('ETC_board_modify/<int:index_pk>/<int:modify_pk>', ETC_board_modify, name='ETC_board_modify'), 
    # path('ETC_board_delete/<int:index_pk>/<int:modify_pk>', ETC_board_delete, name='ETC_board_delete'),  
    # -----------------------------------------------------------------------------------------------------------------------
    path('PMAUDIT_board_add/<int:index_pk>', PMAUDIT_board_add, name='PMAUDIT_board_add'), 
    path('PMAUDIT_board_modify/<int:index_pk>/<int:modify_pk>', PMAUDIT_board_modify, name='PMAUDIT_board_modify'), 
    path('PMAUDIT_board_delete/<int:index_pk>/<int:modify_pk>', PMAUDIT_board_delete, name='PMAUDIT_board_delete'),  


    


]