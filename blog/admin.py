from django.contrib import admin

# Register your models here.

from .models import Article, Categorie, Comment

#====================================================================================
class ArticleAdmin(admin.ModelAdmin):

	""" Model Article in admininistration backoffice  """

	list_display = ('titre', 'auteur', 'categorie', 'date', 'is_visible', )
	list_filter = ('categorie', )
	search_fields = ('title', 'auteur', )

	prepopulated_fields = {'slug': ('titre', )}

#====================================================================================
class CommentAdmin(admin.ModelAdmin):

	""" Model Comment in admininistration backoffice """

	list_display = ('pseudo', 'email', 'article', 'date', 'is_visible', )
	list_filter = ('article','pseudo', )
	search_fields = ('pseudo', 'email','article', )

#====================================================================================
admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie)
admin.site.register(Comment, CommentAdmin)
