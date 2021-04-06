from advanced_filters.admin import AdminAdvancedFiltersMixin
from rangefilter.filter import DateRangeFilter
from django.contrib import admin
from django.db import models
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ExportActionMixin

# from import_export import resources


# Register your models here.
from .models import Well, Monitor

# admin.site.register(Well)
# admin.site.register(Monitor)

# @admin.register(Well)
# class ProfileAdmin(ImportExportModelAdmin ):
#     list_filter = ('well_type', 'depth', 'provence', 'well_id')   # simple list filters
#     list_display = ("well_type", "depth", "provence")
#     resource_class = Well
    # specify which fields can be selected in the advanced filter
    # creation form
    # advanced_filter_fields = (
    #     'well_type',
    #     'depth',
    #     'provence',
    # )
# class BookAdmin(ImportExportModelAdmin):
#     resource_class = Monitor

@admin.register(Well)
class ProfileAdmin(AdminAdvancedFiltersMixin, ImportExportModelAdmin):
    # list_display=["well_type"]
    list_filter = ('well_type', 'depth', 'provence', 'well_id')   # simple list filters
    list_display = ("well_type", "depth", "provence")
    advanced_filter_fields = (
        'well_type',
        'depth',
        'provence',
    )
    pass
@admin.register(Monitor)
class ProfileAdmin2(AdminAdvancedFiltersMixin, ImportExportModelAdmin):
    list_filter = (('date', DateRangeFilter), )   # simple list filters
    list_display = ("well", "date", "temprature")

    # specify which fields can be selected in the advanced filter
    # creation form
    advanced_filter_fields = (
        'date',
        'PH',
    )
    pass





# admin.site.register(Well, ProfileAdmin)
# admin.site.register(Monitor, ProfileAdmin2)
# admin.site.register(Well, BookAdmin)


# @admin.register(Well)
# class MemberAdmin(ImportExportModelAdmin):
#     list_display = ("well_type", "depth", "provence")
#     pass