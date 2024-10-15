from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('login-seeker',views.login_seeker,name='login_seeker'),
    path('login-recruiter',views.login_recruiter,name='login_recruiter'),
    path('register-seeker',views.reg_seeker,name='reg_seeker'),
    path('register-recruiter',views.reg_recruiter,name='reg_recruiter'),
    path('recruiter-home',views.recruiter_home,name='rec_home'),
    path('seeker-home/<int:pk>',views.seeker_home,name='sek_home'),
    path('hiring-seekers',views.hiring_seekers,name='hir_sek'),
    path('view-job-post/<int:pk>',views.view_job_post,name='view_job_post'),
    path('jobpost-history',views.jobpost_history,name='jp_history'),
    path('remove-post/<int:pk>',views.removed_post,name='removd_pst'),
    path('edit-reg-seeker/<int:pk>',views.edit_profile,name='edt_rg_sek'),
]