"""
URL configuration for myProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from app01 import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", views.login, name="login"),
    path("login/register/", views.register),
    path("login/student_main/<str:user_account>/", views.student_main,name="student_main"),
    path("login/teacher_main/<str:user_account>/", views.teacher_main, name="teacher_main"),
    # path("create_course/<str:user_account>/", views.create_course),
    path("create_course/<str:user_account>/", views.create_course, name="create_course"),
    path("login/course_detail_student/<int:course_id>/<str:user_account>/", views.course_detail_student, name="course_detail_student"),
    path("login/course_detail_teacher/<int:course_id>/", views.course_detail_teacher, name="course_detail_teacher"),
    path("login/assignment_detail_student/<int:assignment_id>/<str:user_account>/", views.assignment_detail_student, name="assignment_detail_student"),
    path("login/assignment_detail_student/download_assignment/<int:assignment_id>/", views.download_assignment, name="download_assignment"),
    path("login/user_set/<str:user_account>/",views.user_set,name="user_set"),
    path("login/course_detail_teacher/submission_detail_teacher/<int:assignment_id>/",views.submission_detail_teacher,name="submission_detail_teacher"),
]
