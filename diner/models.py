# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class MbBpm(models.Model):
    recid = models.AutoField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    value = models.CharField(max_length=62, blank=True, null=True)
    parent_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'MB_BPM'


class MbCdtitle(models.Model):
    recid = models.AutoField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    value = models.CharField(max_length=62)
    parent_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'MB_CDTitle'


class MbComposer(models.Model):
    recid = models.AutoField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    value = models.CharField(max_length=62)
    parent_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'MB_Composer'


class MbDesigner(models.Model):
    recid = models.AutoField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    value = models.CharField(max_length=62)
    parent_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'MB_Designer'


class MbFeaturedinstrument(models.Model):
    recid = models.AutoField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    value = models.CharField(max_length=62)
    parent_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'MB_FeaturedInstrument'


class MbLibrary(models.Model):
    recid = models.AutoField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    value = models.CharField(max_length=62)
    parent_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'MB_Library'


class MbManufacturer(models.Model):
    recid = models.AutoField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    value = models.CharField(max_length=62)
    parent_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'MB_Manufacturer'


class MbPathname(models.Model):
    recid = models.AutoField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    value = models.CharField(max_length=62)
    parent_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'MB_Pathname'


class MbPublisher(models.Model):
    recid = models.AutoField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    value = models.CharField(max_length=62)
    parent_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'MB_Publisher'


class MbShortid(models.Model):
    recid = models.AutoField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    value = models.CharField(max_length=62)
    parent_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'MB_ShortID'


class MbShow(models.Model):
    recid = models.AutoField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    value = models.CharField(max_length=62)
    parent_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'MB_Show'


class MbFlatcategory(models.Model):
    recid = models.AutoField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    value = models.CharField(max_length=62)
    parent_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'MB__FlatCategory'


class Artwork(models.Model):
    recid = models.AutoField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    hash = models.TextField()
    picture = models.TextField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'artwork'


class Assets(models.Model):
    track_id = models.IntegerField()
    asset_key = models.CharField(max_length=32)

    class Meta:
        managed = True
        db_table = 'assets'


class Counter(models.Model):
    counter_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'counter'


class DinerAppLog(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    filename = models.CharField(max_length=31, blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    fullname = models.TextField(blank=True, null=True)
    activation_code = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'diner_app_log'


class Links(models.Model):
    playlistnamerecid = models.IntegerField(db_column='playlistNameRecID')  # Field name made lowercase.
    metadatarecid = models.IntegerField(db_column='metadataRecID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'links'


class Metadata(models.Model):
    recid = models.AutoField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    filename = models.CharField(db_column='Filename', max_length=255)  # Field name made lowercase.
    pathname = models.CharField(db_column='Pathname', max_length=255)  # Field name made lowercase.
    filepath = models.TextField(db_column='FilePath')  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=10)  # Field name made lowercase.
    filetype = models.CharField(db_column='FileType', max_length=4)  # Field name made lowercase.
    creationdate = models.DateField(db_column='CreationDate')  # Field name made lowercase.
    modificationdate = models.DateField(db_column='ModificationDate')  # Field name made lowercase.
    totalframes = models.IntegerField(db_column='TotalFrames')  # Field name made lowercase.
    entrydate = models.FloatField(db_column='EntryDate')  # Field name made lowercase.
    popularity = models.IntegerField(db_column='Popularity')  # Field name made lowercase.
    split = models.IntegerField(db_column='Split')  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating')  # Field name made lowercase.
    samplerate = models.IntegerField(db_column='SampleRate')  # Field name made lowercase.
    channels = models.IntegerField(db_column='Channels')  # Field name made lowercase.
    bitdepth = models.IntegerField(db_column='BitDepth')  # Field name made lowercase.
    channellayout = models.CharField(db_column='ChannelLayout', max_length=31)  # Field name made lowercase.
    field_flatcategory = models.CharField(db_column='_FlatCategory', max_length=255)  # Field name made lowercase. Field renamed because it started with '_'.
    field_waveformlink = models.IntegerField(db_column='_WaveformLink')  # Field name made lowercase. Field renamed because it started with '_'.
    field_picturelink = models.IntegerField(db_column='_PictureLink')  # Field name made lowercase. Field renamed because it started with '_'.
    field_umid = models.CharField(db_column='_UMID', max_length=64)  # Field name made lowercase. Field renamed because it started with '_'.
    time = models.TimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=100)  # Field name made lowercase.
    track = models.IntegerField(db_column='Track', blank=True, null=True)  # Field name made lowercase.
    index = models.IntegerField(db_column='Index', blank=True, null=True)  # Field name made lowercase.
    field_dirty = models.IntegerField(db_column='_Dirty', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    lyrics = models.TextField(db_column='Lyrics', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=62, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=62, blank=True, null=True)  # Field name made lowercase.
    subcategory = models.CharField(db_column='SubCategory', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    fxname = models.CharField(db_column='FXName', max_length=128, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    show = models.CharField(db_column='Show', max_length=62, blank=True, null=True)  # Field name made lowercase.
    library = models.CharField(db_column='Library', max_length=62, blank=True, null=True)  # Field name made lowercase.
    rectype = models.CharField(db_column='RecType', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    shortid = models.CharField(db_column='ShortID', max_length=31, blank=True, null=True)  # Field name made lowercase.
    longid = models.CharField(db_column='LongID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    recmedium = models.CharField(db_column='RecMedium', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    keywords = models.CharField(db_column='Keywords', max_length=255, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    microphone = models.CharField(db_column='Microphone', max_length=62, blank=True, null=True)  # Field name made lowercase.
    composer = models.CharField(db_column='Composer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    arranger = models.CharField(db_column='Arranger', max_length=128, blank=True, null=True)  # Field name made lowercase.
    conductor = models.CharField(db_column='Conductor', max_length=128, blank=True, null=True)  # Field name made lowercase.
    publisher = models.CharField(db_column='Publisher', max_length=255, blank=True, null=True)  # Field name made lowercase.
    performer = models.CharField(db_column='Performer', max_length=128, blank=True, null=True)  # Field name made lowercase.
    bpm = models.CharField(db_column='BPM', max_length=31, blank=True, null=True)  # Field name made lowercase.
    key = models.CharField(db_column='Key', max_length=15, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=62, blank=True, null=True)  # Field name made lowercase.
    designer = models.CharField(db_column='Designer', max_length=62, blank=True, null=True)  # Field name made lowercase.
    tracktitle = models.CharField(db_column='TrackTitle', max_length=128, blank=True, null=True)  # Field name made lowercase.
    cdtitle = models.CharField(db_column='CDTitle', max_length=62, blank=True, null=True)  # Field name made lowercase.
    cddescription = models.CharField(db_column='CDDescription', max_length=128, blank=True, null=True)  # Field name made lowercase.
    featuredinstrument = models.CharField(db_column='FeaturedInstrument', max_length=128, blank=True, null=True)  # Field name made lowercase.
    scene = models.CharField(db_column='Scene', max_length=31, blank=True, null=True)  # Field name made lowercase.
    take = models.CharField(db_column='Take', max_length=31, blank=True, null=True)  # Field name made lowercase.
    tape = models.CharField(db_column='Tape', max_length=31, blank=True, null=True)  # Field name made lowercase.
    mood = models.CharField(db_column='Mood', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=31, blank=True, null=True)  # Field name made lowercase.
    bwdescription = models.CharField(db_column='BWDescription', max_length=255)  # Field name made lowercase.
    bworiginator = models.CharField(db_column='BWOriginator', max_length=62)  # Field name made lowercase.
    bworiginatorref = models.CharField(db_column='BWOriginatorRef', max_length=62)  # Field name made lowercase.
    bwtimestamp = models.IntegerField(db_column='BWTimeStamp')  # Field name made lowercase.
    bwtime = models.CharField(db_column='BWTime', max_length=8)  # Field name made lowercase.
    bwdate = models.CharField(db_column='BWDate', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'metadata'


class Playlists(models.Model):
    recid = models.AutoField(db_column='RecID', primary_key=True)  # Field name made lowercase.
    playlistname = models.CharField(db_column='playlistName', max_length=62)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'playlists'


class PostingAssets(models.Model):
    posting_id = models.IntegerField(blank=True, null=True)
    track_id = models.IntegerField(blank=True, null=True)
    longid = models.CharField(db_column='longID', max_length=16, blank=True, null=True)  # Field name made lowercase.
    album = models.CharField(max_length=255, blank=True, null=True)
    order_position = models.IntegerField(blank=True, null=True)
    filename = models.TextField(blank=True, null=True)
    filepath = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'posting_assets'


class PostingLogs(models.Model):
    date_logged = models.DateTimeField()
    src = models.CharField(max_length=255)
    posting_account = models.CharField(max_length=255)
    share_id = models.IntegerField(blank=True, null=True)
    posting_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=8, blank=True, null=True)
    asset = models.TextField()
    ip = models.CharField(max_length=40)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'posting_logs'


class PostingShares(models.Model):
    date_shared = models.DateTimeField()
    posting_id = models.IntegerField()
    from_email = models.CharField(max_length=255)
    from_name = models.CharField(max_length=255, blank=True, null=True)
    to_email = models.CharField(max_length=255)
    cc_email = models.CharField(max_length=255, blank=True, null=True)
    clicked = models.CharField(max_length=3, blank=True, null=True)
    played = models.CharField(max_length=3, blank=True, null=True)
    forwarded = models.CharField(max_length=3, blank=True, null=True)
    hash = models.CharField(max_length=8)

    class Meta:
        managed = True
        db_table = 'posting_shares'


class Postings(models.Model):
    state = models.CharField(max_length=6, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    artwork = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    slug = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'postings'


class RecessToolsClasses(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    parentid = models.IntegerField(db_column='parentId', blank=True, null=True)  # Field name made lowercase.
    packageid = models.IntegerField(db_column='packageId', blank=True, null=True)  # Field name made lowercase.
    doccomment = models.TextField(db_column='docComment', blank=True, null=True)  # Field name made lowercase.
    file = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'recess_tools_classes'


class RecessToolsPackages(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    parentid = models.IntegerField(db_column='parentId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'recess_tools_packages'


class Schema(models.Model):
    schema = models.CharField(max_length=30)
    version = models.IntegerField(blank=True, null=True)
    version_min = models.IntegerField(blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'schema'


class TtLicenses(models.Model):
    date = models.DateTimeField()
    name = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    track = models.CharField(max_length=128, blank=True, null=True)
    short_id = models.CharField(max_length=40, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tt_licenses'


class Uuid(models.Model):
    field_umid = models.TextField(db_column='_UMID')  # Field name made lowercase. Field renamed because it started with '_'.

    class Meta:
        managed = True
        db_table = 'uuid'
