from django.contrib import admin
from webapp.models import Genre, CastMember, Title


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_adult')


class CastMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age')


class Titledmin(admin.ModelAdmin):
    list_display = ('name', 'release_date',
                    'added_on', 'rating')


# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(CastMember, CastMemberAdmin)
admin.site.register(Title, Titledmin)
