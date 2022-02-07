from django.contrib import admin
from django_summernote.admin import Summ
from news.models import News, Category, Tag, Comments

class NewsAdmin(SummernotModulAdmin):
    summer_note_fields = ("text_min", "text")

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Tag)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "new", "created", "moderation")



admin.site.register(Comments, CommentAdmin)
