from django.contrib import admin

from .models import PoolResource,PoolCab,StoreResource,PoolFood
admin.site.register(PoolCab)
admin.site.register(PoolResource)
admin.site.register(StoreResource)
admin.site.register(PoolFood)