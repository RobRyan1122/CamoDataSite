from django.contrib import admin

# Register your models here.
# myapp/admin.py

from django.contrib import admin
from .models import Post, Image, Question
from import_export import resources
from import_export.admin import ExportMixin

# Define the import-export resource for the Question model
class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_id', 'animal_type', 'animal_present', 'image_title', 'image_file')

@admin.register(Question)
class QuestionAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = QuestionResource
    list_display = ('question_id', 'animal_type', 'clicked_at', 'session_num', 'ap_correct', 'at_correct', 'image')
 