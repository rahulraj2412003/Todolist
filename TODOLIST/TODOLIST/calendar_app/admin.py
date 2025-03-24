from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Task

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'phone_number', 'address', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'due_date', 'completed')
    list_filter = ('user', 'due_date', 'completed')
    search_fields = ('title', 'description', 'user__username')
    ordering = ('due_date',)

admin.site.register(Task, TaskAdmin)
