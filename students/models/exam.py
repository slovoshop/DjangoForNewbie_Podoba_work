

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Exam(models.Model):
    """Exam Model"""
    
    class Meta(object):
        verbose_name = _(u"Exam")
        verbose_name_plural = _(u"Exams")
        
    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_(u"Subject"))
        
    date = models.DateTimeField(
        blank=False,
        verbose_name=_(u"Date/Time"),
        null=True)
        
    teacher = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_(u"Teacher"))
        
    exam_group = models.ForeignKey('Group',
        verbose_name=_(u"Group"),
        blank=False,
        null=True)
    def __unicode__(self):
        return u"%s %s" % (self.exam_group.title, self.title)
