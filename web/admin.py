from django.contrib import admin
from web.models import FeaturedAlbum, FeaturedSlide
from sorl.thumbnail.admin import AdminImageMixin
from sorl.thumbnail import get_thumbnail


class FeaturedSlideInline(AdminImageMixin, admin.TabularInline):
    model = FeaturedSlide
    fields = ('position', 'image', 'status', )
    # define the sortable
    sortable_field_name = "position"
    extra = 0

class FeaturedAlbumAdmin(admin.ModelAdmin):
    list_display = ('name', )
    inlines = [FeaturedSlideInline]
    
class FeaturedSlideAdmin(AdminImageMixin, admin.ModelAdmin):
    """docstring for FeaturedSlide"""

    def thumbnail(self, obj):
           im = get_thumbnail(obj.image, '60x60', quality=99)
           return u"<img src='%s'>" % im.url
    thumbnail.allow_tags = True
    
    class Media:
        js = [
            '/static/admin/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/path/to/your/tinymce_setup.js',
        ]
       
    list_display = ('name', 'position', 'status', 'thumbnail',)
    pass
        

admin.site.register(FeaturedAlbum, FeaturedAlbumAdmin)

admin.site.register(FeaturedSlide, FeaturedSlideAdmin)