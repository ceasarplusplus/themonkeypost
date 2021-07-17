from django.contrib import admin
import admin_thumbnails
from mptt.admin import DraggableMPTTAdmin
from .models import VideoCategory, Videos, Breadcrumb, Setting, Nextmatch, Subscribe, Portfolio, PortfolioImages, Audios, Gallery, ContactMessage, Faqs


class VideoCategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_videos_count', 'related_videos_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = VideoCategory.objects.add_related_count(
            qs,
            Videos,
            'category',
            'videos_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = VideoCategory.objects.add_related_count(qs,
                                                Videos,
                                                'category',
                                                'videos_count',
                                                cumulative=False)
        return qs

    def related_videos_count(self, instance):
        return instance.videos_count
    related_videos_count.short_description = 'Related video (for this specific category)'

    def related_videos_cumulative_count(self, instance):
        return instance.videos_cumulative_count
    related_videos_cumulative_count.short_description = 'Related video (in tree)'




class VideosAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'link', 'image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    prepopulated_fields = {'slug': ('title',)}




@admin_thumbnails.thumbnail('image')
class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImages
    readonly_fields = ('id',)
    extra = 1






class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_type', 'host', 'image_tag']
    # list_filter = ['project_type']
    readonly_fields = ('image_tag',)
    inlines = [PortfolioImageInline]
    prepopulated_fields = {'slug': ('title',)}











admin.site.register(Portfolio, PortfolioAdmin)




# admin.site.register(Color, ColorAdmin)
# admin.site.register(Size, SizeAdmin)
# admin.site.register(Variants, VariantsAdmin)
admin.site.register(VideoCategory, VideoCategoryAdmin2)
admin.site.register(Videos)
admin.site.register(Audios)
# Register your models here.





admin.site.register(Setting)
admin.site.register(ContactMessage)
admin.site.register(Subscribe)

admin.site.register(Faqs)
admin.site.register(Gallery)
admin.site.register(Breadcrumb)
admin.site.register(Nextmatch)



