from django.urls import path, include
from . import views




urlpatterns = [
    path('', views.index, name='index'),
    path('sale_pg', views.sale_pg, name='sale_pg'),   
    path('aff_mkts_pg', views.aff_mkts_pg, name='aff_mkts_pg'),   
    path('human_psyc', views.human_psyc, name='human_psyc'), 
    
    
    path('sp', views.sp, name='sp'), 
    path('spa', views. spa, name=' spa'), 
    path('spb', views.spb, name='spb'), 
    
    path('amp', views.amp, name='amp'), 
    path('ampa', views.ampa, name='ampa'), 
    path('ampb', views.ampb, name='ampb'), 
    
    path('hmp', views.hmp, name='hmp'), 
    path('hmpa', views.hmpa, name='hmpa'), 
    path('hmpb', views.hmpb, name='hmpb'), 
    
      
    
    
    
    
]