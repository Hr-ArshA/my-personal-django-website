from django.contrib import admin
from blog.models import Post, Category

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('Title','slug','jpublish', 'Author','Status','category_to_str')
    list_filter = ('Publish','Status')
    search_fields = ('Title','Description')
    prepopulated_fields = {'slug':('Title',)}
    ordering = ['-Publish']

    def category_to_str(self, obj):
        return '، '.join([Category.Title for Category in obj.category_published()])


admin.site.register(Post,PostAdmin)
admin.site.register(Category)