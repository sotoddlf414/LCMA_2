from django.contrib import admin
from django.urls import path
from .views import *


app_name = 'maintenance'

urlpatterns = [
    path('Hour/<int:pk>', RunningHour, name='hour'),

    path('timeform/<int:index_pk>', timeform, name='timeform'),

    path('breakfix/<int:index_pk>', breakfix, name='break_fix'),
    path('etc/<int:index_pk>', ETC_form, name='etc'),
    path('pmaudit/<int:index_pk>', pm_audit, name='pm_audit'),
    path('overhaul/<int:index_pk>', overhaul, name='overhaul'),


    path('greasing/<int:index_pk>', greasing, name='greasing'),
    path('greasing_add/<int:index_pk>', greasing_add, name='greasing_add'),
    path('greasing_modify/<int:index_pk>/<int:grease_pk>', greasing_modify, name='greasing_modify'),
    path('greasing_VibrationBearing/<int:index_pk>', greasing_VibrationBearing, name='greasing_VibrationBearing'),
    path('greasing_Connecting/<int:index_pk>', greasing_Connecting, name='greasing_Connecting'),

    path('Injection_vibrail/<int:index_pk>', injection_vibrail, name='Injection_vibrail'),
    path('injection_xaxis/<int:index_pk>', injection_xaxis, name='injection_xaxis'),
    path('injection_yaxis/<int:index_pk>', injection_Yaxis, name='injection_yaxis'),
    path('injection_vaccum/<int:index_pk>', injection_vaccum, name='injection_vaccum'),
    path('injection_comment/<int:index_pk>', injection_comment, name='injection_comment'),

    path('routine_check_1/<int:index_pk>', routine_check_1, name='routine_check_1'),
    path('routine_pressfoot/<int:index_pk>', routine_pressfoot, name='routine_pressfoot'),
    path('routine_bladeguide/<int:index_pk>', routine_bladeguide, name='routine_bladeguide'),
    path('routine_sharpningArm/<int:index_pk>', routine_sharpningArm, name='routine_sharpningArm'),
    path('routine_vibration/<int:index_pk>', routine_vibration, name='routine_vibration'),
    path('routine_rotation/<int:index_pk>', routine_rotation, name='routine_rotation'),
    path('routine_pneumaticblock/<int:index_pk>', routine_pneumaticblock, name='routine_pneumaticblock'),
    path('routine_airfilter/<int:index_pk>', routine_airfilter, name='routine_airfilter'),
    path('routine_xaxis/<int:index_pk>', routine_xaxis, name='routine_xaxis'),
    path('routine_yaxis/<int:index_pk>', routine_yaxis, name='routine_yaxis'),
    path('routine_coda/<int:index_pk>', routine_coda, name='routine_coda'),
    path('routine_bristle/<int:index_pk>', routine_bristle, name='routine_bristle'),
    path('routine_airinlet/<int:index_pk>', routine_airinlet, name='routine_airinlet'),
    path('routine_resultfabric/<int:index_pk>', routine_resultfabric, name='routine_resultfabric'),
    path('routine_elecabinet/<int:index_pk>', routine_elecabinet, name='routine_elecabinet'),


 



  
    





    


]