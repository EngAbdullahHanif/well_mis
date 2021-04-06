#resources.py
from import_export import resources
from  .models import Well
 
class MemberResource(resources.ModelResource):
    resource_class = Well
    class Meta:
        model = Well