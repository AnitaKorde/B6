"""B6_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from tokenize import Name
from django.contrib import admin
from django.urls import path, include,re_path
from book.views import delete_all, homepage,show_all_book,edit_data,delete_data,is_inactive,update_soft_del,recover_soft_del,all_soft_del

from book import views
from book.views.views import PersonCreate,PersonRetrieve, PersonDetails, PersonUpdate, PersonDelete




urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage,name = "homepage"),
    path('show-all-book/', show_all_book, name = "show_all_book"),
    path('edit/<int:id>/', edit_data,name="edit"),
    path('delete/<int:id>/', delete_data,name="delete"),
    path('delete-all-book/', delete_all, name = "delete_all_book"),
    path('soft_delete/', is_inactive, name = "soft_delete"),
    path('soft_delete_update/<int:id>/', update_soft_del, name = "soft_delete_update"),
    path('soft_delete_recovery/<int:id>/', recover_soft_del, name = "soft_delete_recovery"),
    path('all-soft-delete/', all_soft_del, name = "all_soft_delete"),
    path('form-home/', views.form_home,name = "form-home"),
    path('index-form/', views.index,name = "index-form"),
    path('emp-form/', views.emp_form,name = "emp-form"),
    path('crispy-form/', views.crispy_form,name = "crispy-form"),
    path('__debug__/', include('debug_toolbar.urls')),
    
#class based urls
    
    path('home_cbv/', views.Home.as_view(Name="abcd"),name = "home"),
    path('temp_cbv/', views.temp_cbv.as_view(),name = "temp_cbv"),

#create generic view url
    path('person-gcreate/', PersonCreate.as_view(), name = 'personCreate'),
    path('retrieve/', PersonRetrieve.as_view(), name = 'personRetrieve'),
    path('retrieve/<int:pk>/', PersonDetails.as_view(), name = 'PersonDetail'),
    path('person/<int:pk>/update/', PersonUpdate.as_view(), name = 'PersonUpdate'),
    path('person/<int:pk>/delete/', PersonDelete.as_view(), name = 'PersonDelete'),
    
    


]


urlpatterns +=[
    re_path(r'^aaa$', views.view_a, name='view_a'),
    re_path(r'^bbb$', views.view_b, name='view_b'),
    re_path(r'^ccc$', views.view_c, name='view_c'),
    re_path(r'^ddd$', views.view_d, name='view_d'),
]




# urlpatterns += [
#     path('__debug__/', include('debug_toolbar.urls'))
# ]