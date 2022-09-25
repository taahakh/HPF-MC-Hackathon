from django.contrib import admin
from proj.models import DonorTransactions, Address, Donor, Project, DonorList, ProjectTransactions, FacilityList
# Register your models here.

admin.site.register(DonorTransactions)
admin.site.register(DonorList)
admin.site.register(Address)
admin.site.register(Donor)
admin.site.register(Project)
admin.site.register(ProjectTransactions)
admin.site.register(FacilityList)