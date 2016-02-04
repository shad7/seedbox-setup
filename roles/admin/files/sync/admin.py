from django.contrib import admin
from sync.models import AppState, Torrent, MediaFile

#Torrents Control
class MediaFileInline(admin.TabularInline):
    model = MediaFile

class TorrentAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'invalid', 'purged', 'failed', 'retry_count', 'name')
    list_filter = ['state', 'failed', 'invalid', 'purged']
    search_fields = ['name']

    fieldsets = [
        ('Identification', {'fields': ['id', 'name']}),
        ('Status',         {'fields': ['state', 'invalid', 'purged']}),
        ('Failures',       {'fields': ['failed', 'retry_count', 'error_msg'], 'classes': ['collapse']}),
    ]

    inlines = [
        MediaFileInline,
    ]

admin.site.register(Torrent, TorrentAdmin)

#MediaFile Control
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'filename', 'file_ext', 'file_path', 'torrent', 'compressed', 'synced', 'missing', 'skipped')
    list_filter = ['compressed', 'synced', 'missing', 'skipped']
    search_fields = ['filename']

    fieldsets = [
        (None,                 {'fields': ['torrent']}),
        ('File Details',       {'fields': ['id', 'filename', 'file_ext', 'file_path', 'size', 'total_time'], 'classes': ['collapse']}),
        ('Processing Flags',   {'fields': ['compressed', 'synced', 'missing', 'skipped']}),
    ]

    actions = ['make_synced']

    def make_synced(self, request, queryset):
        rows_updated = queryset.update(synced=True)
        if rows_updated == 1:
            message_bit = "1 file was"
        else:
            message_bit= "%s files were" % rows_updated
        self.message_user(request, "%s successfully marked as synced." % message_bit)

    make_synced.short_description = "Mark selected file as synced"


admin.site.register(MediaFile, MediaFileAdmin)

#AppState Control
class AppStateAdmin(admin.ModelAdmin):
    list_display = ('name', 'dtype', 't_datetime', 't_string', 't_int', 't_bool')
    list_filter = ['t_datetime', 't_bool']
    search_fields = ['name']
    date_hierarchy = 't_datetime'

admin.site.register(AppState, AppStateAdmin)

