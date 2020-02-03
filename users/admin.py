"""User admin classes."""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Register your models here.

# One way to register a model:
    # admin.site.register(Profile)

# Other way:
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    # lista que determina que atributos se ven en el admin
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    
    # lista que dice que atributos son clickeables
    list_display_links = ('pk', 'user')

    # lista que dice que atributos se pueden editar sin entrar a los detalles del perfil
    list_editable = ('website',)

    # lista que dice que atributos serán criterios de busqueda
    search_fields = (
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    # lista que dice por que atributos se va a filtrar los registros
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),)
        }),
        ('Extra Info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata',{
            'fields': (('created', 'modified'),)
        })
    )

    readonly_fields = ('created', 'modified',)


class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profile
    can_delete  = False
    verbose_name_plural = 'Profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile to base user admin"""

    inlines = (ProfileInline, )
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)