from django.contrib import admin
from blog.models import Post, Category


# Register your models here.




class PostAdmin(admin.ModelAdmin):
    list_display = ('Title','slug','jpublish', 'Author','Status','category_to_str')
    list_filter = ('Publish','Status')
    search_fields = ('Title','Description')
    ordering = ['-Publish']

    def category_to_str(self, obj):
        return '، '.join([Category.Title for Category in obj.category_published()])
    category_to_str.short_description = 'دسته بندی'

admin.site.register(Post,PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Position','Title','slug','Status')
    list_filter = (['Status'])
    search_fields = ('Title','slug')




admin.site.register(Category,CategoryAdmin)
