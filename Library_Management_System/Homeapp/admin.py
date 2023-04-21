from django.contrib import admin
from Homeapp.models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display=['name','isbn','description']
    
admin.site.register(Book,BookAdmin)
