# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

VAL_TYPES = (
    ('none', 'none'),
    ('bool', 'bool'),
    ('datetime', 'datetime'),
    ('int', 'int'),
    ('str', 'str'),
)

class AppState(models.Model):
    name = models.TextField(primary_key=True, blank=True)
    dtype = models.CharField(max_length=10, choices=VAL_TYPES, default='none')
    t_string = models.TextField(null=True, blank=True, default=None)
    t_int = models.IntegerField(null=True, blank=True, default=None)
    t_bool = models.NullBooleanField(null=True, blank=True, default=False)
    t_datetime = models.DateTimeField(null=True, blank=True, default=datetime.now)

    def __unicode__(self):
        return '%s - %s' % (self.name, self.dtype)

    class Meta:
        db_table = 'app_states'

class Torrent(models.Model):

    STATES = (
        ('init', 'init'),
        ('ready', 'ready'),
        ('active', 'active'),
        ('done', 'done'),
        ('cancelled', 'cancelled'),
    )

    id = models.IntegerField(primary_key=True, blank=True)
    name = models.TextField(unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    state = models.CharField(max_length=9, choices=STATES, default='init')
    retry_count = models.IntegerField(null=True, blank=True, default=0)
    failed = models.NullBooleanField(null=True, blank=True, default=False)
    error_msg = models.TextField(null=True, blank=True, default=None)
    invalid = models.NullBooleanField(null=True, blank=True, default=False)
    purged = models.NullBooleanField(null=True, blank=True, default=False)

    def __unicode__(self):
        return '%s' % (self.id)

    class Meta:
        db_table = 'torrents'

class MediaFile(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    filename = models.TextField(blank=True)
    file_ext = models.TextField(blank=True)
    file_path = models.TextField(blank=True, default=None)
    size = models.IntegerField(null=True, blank=True, default=0)
    compressed = models.NullBooleanField(null=True, blank=True, default=False)
    synced = models.NullBooleanField(null=True, blank=True, default=False)
    missing = models.NullBooleanField(null=True, blank=True, default=False)
    skipped = models.NullBooleanField(null=True, blank=True, default=False)
    error_msg = models.TextField(null=True, blank=True, default=None)
    total_time = models.FloatField(null=True, blank=True, default=0)
    torrent = models.ForeignKey(Torrent)

    def __unicode__(self):
        return '%s - %s - %s - %s' % (self.id, self.filename, self.file_ext, self.torrent)

    class Meta:
        db_table = 'media_files'

