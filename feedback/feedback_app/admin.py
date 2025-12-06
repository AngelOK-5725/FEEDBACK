from django.contrib import admin

# Register your models here.
from .models import Feedback
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user_name','review_text' ,'rating',)
admin.site.register(Feedback, FeedbackAdmin)