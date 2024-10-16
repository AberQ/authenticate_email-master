from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from users.forms import UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    add_form = UserCreationForm

from .models import State

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'author')  # Поля, которые будут отображаться в списке
    search_fields = ('title',)  # Поиск по заголовку