from django.contrib import admin

# Register your models here.
from .models import Farmer
from .models import Farm
from .models import Pig
from .models import Immunization
from .models import Past_Farm_Record

admin.site.register(Farmer)
#admin.site.register(Farm)
#admin.site.register(Immunization)
#admin.site.register(Past_Farm_Record)

class ImmInline(admin.StackedInline):
    model = Immunization
    extra = 0
    
class RecInline(admin.StackedInline):
    model = Past_Farm_Record
    extra = 0

@admin.register(Pig)
class PigAdmin(admin.ModelAdmin):
    inlines = [ImmInline, RecInline]




class PigInline(admin.StackedInline):
    model = Pig
    extra = 0
    show_change_link = True


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    inlines = [PigInline]

