from django.contrib import admin

# Register your models here.

# from .models import Book

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'publication_date')

# admin.site.register(Book, BookAdmin)



from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')

admin.site.register(BlogPost, BlogPostAdmin)

