from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField
from django.db.models import permalink


from managers import PublicManager

class FeaturedAlbum(models.Model):
    """Image gallery for slider"""
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u'Featured Album'
        verbose_name_plural = u'Featured Albums'

    def __unicode__(self):
        return self.name
        
class FeaturedSlide(models.Model):
    """
    (Featured description)
    """
    STATUS_CHOICES = (
        (0, _('Private')),
        (1, _('Draft')),
        (2, _('Public')),
    )
    name = models.CharField(max_length=150)
    album = models.ForeignKey(FeaturedAlbum)
    caption = models.CharField(_('caption'), blank=True, max_length=255)
    description = models.TextField(_('description'), blank=True)
    image  = ImageField(_('picture'), upload_to='teasers', blank=True)
    link    = models.URLField(blank=True)
    status  = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
    # position field
    position = models.PositiveSmallIntegerField("Position", default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = PublicManager()
    
    class Meta:
        verbose_name = u'Featured Slide'
        verbose_name_plural = 'Featured Slides'
        ordering = ('position',)
    
    def __unicode__(self):
        if self.name:
            name = self.name
        else:
            try:
                name = self.image.file.name.split("/")[-1]
            except:
                name = unicode(self.image)
        return "%s"  % name
