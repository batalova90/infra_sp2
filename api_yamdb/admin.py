from django.contrib import admin
from .reviews import Review, Comment
from .categories import Genres, Categories, Titles, TitilesGenres


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'author', 'score')
    search_fields = ('title', )
    list_filter = ('title', )
    empty_value_display = ('-empty-')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'review', 'text', 'author', 'pub_date')
    search_fields = ('review', )
    list_filter = ('review', )
    empty_value_display = ('-empty-')


class GenresAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name', )
    list_filter = ('name', )
    empty_value_display = ('-empty-')


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name', )
    list_filter = ('name', )
    empty_value_display = ('-empty-')


class TitlesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'description', 'category', 'genre', 'rating')
    search_fields = ('name',)
    list_filter = ('name', )
    empty_value_display = ('-empty-')


class TitlesGenresAdmin(admin.ModelAdmin):
    list_display = ('pk', 'genre', 'title')
    search_fields = ('genre', )
    list_filter = ('genre', )
    empty_value_display = ('-empty-')


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Genres, GenresAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Titles, TitlesAdmin)
admin.site.register(TitlesGenres, TitlesGenresAdmin)

