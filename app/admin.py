from django.contrib import admin

# Register your models here.
from app.models import *

class customizeWebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    list_display_links=['name']
    list_editable=('url',)
    search_fields=['name']
    list_filter=['url','name']
    list_per_page=2
class customizeAccessRecord(admin.ModelAdmin):
    list_display=['name','date','author']
    list_display_links=['author']
    list_editable=('date',)
    search_fields=['author']
    list_filter=['author','date']
    list_per_page=2

admin.site.register(Topic)
admin.site.register(Webpage,customizeWebpage)
admin.site.register(AccessRecord,customizeAccessRecord)
