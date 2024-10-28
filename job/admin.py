from django.contrib import admin

from .models import Recruiter, Seeker, HiringSeekers, RemovedPost, ApplicantDetails
# Register your models here.
admin.site.register(Recruiter)
admin.site.register(Seeker)
admin.site.register(HiringSeekers)
admin.site.register(RemovedPost)
admin.site.register(ApplicantDetails)