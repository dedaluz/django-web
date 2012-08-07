from django.contrib import admin
from web.models import FeaturedAlbum, FeaturedSlide
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail


class FeaturedSlideInline(AdminImageMixin, admin.TabularInline):
    model = FeaturedSlide
    fields = ('position', 'image', 'status', )
    # define the sortable
    sortable_field_name = "position"

class FeaturedAlbumAdmin(admin.ModelAdmin):
    list_display = ('name', )
    inlines = [FeaturedSlideInline]
    
class FeaturedSlideAdmin(AdminImageMixin, admin.ModelAdmin):
    """docstring for FeaturedSlide"""
       
    list_display = ('name', 'position', 'status',)
    pass
        

admin.site.register(FeaturedAlbum, FeaturedAlbumAdmin)

admin.site.register(FeaturedSlide, FeaturedSlideAdmin)