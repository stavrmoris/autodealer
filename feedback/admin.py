from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'phone_number', 'contact_method', 'created_at')
    list_filter = ('contact_method', 'created_at')
    search_fields = ('user_name', 'phone_number')