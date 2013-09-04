from django.contrib import admin
from sba.models import Region,SearchTerm,Topic,Tweet

class RegionAdmin(admin.ModelAdmin):
    fields =  ['name']



class SearchTermInline(admin.StackedInline):
    model = SearchTerm
    fields = ['term']
    extra = 3

class TopicAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [SearchTermInline]
    
admin.site.register(Region,RegionAdmin)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Tweet)