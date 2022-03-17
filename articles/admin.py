from django.contrib import admin
from .models import Article, comment

# Register your models here.
class CommentInLine(admin.TabularInline):
    model = comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]


admin.site.register(Article, ArticleAdmin)
admin.site.register(comment)