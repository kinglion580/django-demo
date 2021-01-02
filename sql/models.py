from django.db import models


class Board(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Board'


class Boardpersonnel(models.Model):
    boardid = models.ForeignKey(Board, models.DO_NOTHING, db_column='BoardId', blank=True, null=True)  # Field name made lowercase.
    personneltypeid = models.ForeignKey('Personneltype', models.DO_NOTHING, db_column='PersonnelTypeId', blank=True, null=True)  # Field name made lowercase.
    userinfoid = models.ForeignKey('Userinfo', models.DO_NOTHING, db_column='UserInfoId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BoardPersonnel'


class Partnumber(models.Model):
    boardid = models.ForeignKey(Board, models.DO_NOTHING, db_column='BoardId', blank=True, null=True)  # Field name made lowercase.
    partnumber = models.CharField(db_column='PartNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PartNumber'


class Personneltype(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    personneltype = models.CharField(db_column='PersonnelType', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PersonnelType'


class Userinfo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserInfo'
