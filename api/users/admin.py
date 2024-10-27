from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'is_staff']
    labels = {
        'telegram_id': 'id',
        'is_staff': 'Админ'
    }

    fields = ['telegram_id']

