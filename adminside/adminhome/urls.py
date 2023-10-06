from django.urls import path
from .import views

urlpatterns = [

    path("adminlogin/",views.adminlogin, name="adminlogin"),
    path("adminhome/", views.adminhome, name="adminhome"),
    path("adminlogout/",views.adminlogout, name="adminlogout"),
    path("adminchangepassword/",views.admin_change_password, name="adminchangepassword"),
    
    
]