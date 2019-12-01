from django.contrib import admin

# Register your models here.
from ZisakuZitenServer.models import Group, Ziten

# admin.site.register(Ziten)
# admin.site.register(Group)


@admin.register(Group)
class Group(admin.ModelAdmin):
    pass

@admin.register(Ziten)
class Ziten(admin.ModelAdmin):
    pass
