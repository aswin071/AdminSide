from django.urls import path
from .import views

urlpatterns = [

   path("courses/",views.course_view, name="courses"),
   path("addCourse/", views.addCourse, name="addCourse"),
   path("activecourse/",views.active_courses, name="activecourse"),
   path("inactivecourse/",views.inactive_courses, name="inactivecourse"),
   path("editcourse/<int:id>/",views.EditCourse, name="editcourse"),
   path("deletecourse/<int:id>",views.deleteCourse, name="deletecourse")
    
]