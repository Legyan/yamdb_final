from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Title, Category, Genre

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    """Админка для юзеров."""

    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'bio',
        'role',
        'confirmation_code',
    )
    list_editable = ('role',)
    search_fields = ('bio',)
    list_filter = ('username',)
    empty_value_display = '-пусто-'


class TitleAdmin(admin.ModelAdmin):
    """Админка для произведения."""

    list_display = ('id', 'name', 'year')
    list_filter = ('genre', 'category', 'year')
    search_fields = ('name', 'description')
    empty_value_display = '-пусто-'


class CategoryAdmin(admin.ModelAdmin):
    """Админка для категории."""

    list_display = ('pk', 'name', 'slug')
    search_fields = ('name', )
    empty_value_display = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    """Админка для жанра."""

    list_display = ('pk', 'name', 'slug', )
    search_fields = ('name', )
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
