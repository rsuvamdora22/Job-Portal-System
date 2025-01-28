from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='HOME'),
    path('login-seeker',views.login_seeker,name='login_seeker'),
    path('login-recruiter',views.login_recruiter,name='login_recruiter'),
    path('register-seeker',views.reg_seeker,name='reg_seeker'),
    path('register-recruiter',views.reg_recruiter,name='reg_recruiter'),
    path('recruiter-home',views.recruiter_home,name='rec_home'),
    path('seeker-home/<int:jk>',views.seeker_home,name='sek_home'),
    path('hiring-seekers',views.hiring_seekers,name='hir_sek'),
    path('view-job-post/<int:pk>',views.view_job_post,name='view_job_post'),
    path('jobpost-history',views.jobpost_history,name='jp_history'),
    path('remove-post/<int:pk>',views.removed_post,name='removd_pst'),
    path('edit-reg-seeker/<int:jk>',views.edit_profile,name='edt_rg_sek'),
    path('posted-jobs/<int:jk>',views.posted_jobs,name='postd_jobs'),
    path('job-details/<int:pk>/<int:jk>',views.job_details,name='job_dtls'),
    path('applied-jobs',views.applied_jobs,name='appld_jobs'),
    path('profile-view/<int:vk>',views.profile_view,name='pro_view'),
    path('app-tracker/<int:vk>',views.app_tracker,name='app_tracker'),
]