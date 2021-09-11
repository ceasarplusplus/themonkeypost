from django.contrib import admin
import admin_thumbnails
from mptt.admin import DraggableMPTTAdmin
from .models import Blog, BlogCategory, BlogComment, Gif, NewsSlide
# Register your models here.


# @admin_thumbnails.thumbnail('image')
class GifImageInline(admin.TabularInline):
    model = Gif
    readonly_fields = ('id',)
    extra = 1


class BlogCategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_blogs_count', 'related_blogs_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = BlogCategory.objects.add_related_count(
            qs,
            Blog,
            'category',
            'blogs_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = BlogCategory.objects.add_related_count(qs,
                                                Blog,
                                                'category',
                                                'blogs_count',
                                                cumulative=False)
        return qs

    def related_blogs_count(self, instance):
        return instance.blogs_count
    related_blogs_count.short_description = 'Related blog (for this specific category)'

    def related_blogs_cumulative_count(self, instance):
        return instance.blogs_cumulative_count
    related_blogs_cumulative_count.short_description = 'Related blog (in tree)'


class BlogAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'category', 'date']
    list_filter = ['author']
    inlines = [GifImageInline]
    prepopulated_fields = {'slug': ('title',)}


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment']

    # readonly_fields = ('comment', 'user')



admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin2)
admin.site.register(NewsSlide)

