# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-27 19:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity', models.CharField(max_length=100)),
                ('TypeAct', models.CharField(max_length=20)),
                ('Activity_Query_Label', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='activity_plan_values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypeAct', models.CharField(max_length=20)),
                ('Activity', models.CharField(max_length=100)),
                ('SubActivity', models.CharField(max_length=150)),
                ('Metric', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='agreement_protect',
            fields=[
                ('Project_ID', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Sage_Elim', models.FloatField(default=0)),
                ('Ag_Conv', models.FloatField(default=0)),
                ('Improper_Graze', models.FloatField(default=0)),
                ('Infastructure', models.FloatField(default=0)),
                ('Energy_Development', models.FloatField(default=0)),
                ('Mining', models.FloatField(default=0)),
                ('Recreation', models.FloatField(default=0)),
                ('Urbanization_SubDevel', models.FloatField(default=0)),
                ('Date_Entered', models.DateTimeField()),
                ('User', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='batchupload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FolderName', models.CharField(max_length=200)),
                ('FileName', models.CharField(max_length=200)),
                ('LCMItem', models.CharField(max_length=50)),
                ('UploadStatus', models.CharField(max_length=20)),
                ('Upload_Date', models.DateTimeField(default=datetime.datetime(2018, 9, 27, 13, 5, 32, 893000))),
                ('Uploading_User', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='batchupload_groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Batch_Group_ID', models.IntegerField()),
                ('BatchUpload_ID', models.IntegerField()),
                ('Group_Designation', models.CharField(max_length=100)),
                ('Effort_ID_List', models.CharField(max_length=100)),
                ('Type_Act', models.CharField(max_length=30)),
                ('Group_Status', models.CharField(max_length=100)),
                ('Upload_Date', models.DateTimeField(default=datetime.datetime(2018, 9, 27, 13, 5, 32, 893000))),
                ('Uploading_User', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='collab_party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Entered', models.DateTimeField()),
                ('User', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='county',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('County', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='county_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Entered', models.DateTimeField()),
                ('User', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='documentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_ID', models.IntegerField()),
                ('File_Type', models.CharField(max_length=255)),
                ('Document_Description', models.CharField(max_length=255)),
                ('Document_Name', models.CharField(max_length=255)),
                ('Date_Entered', models.DateTimeField()),
                ('User', models.CharField(max_length=50)),
                ('LCMItem', models.CharField(max_length=50)),
                ('LCJason', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='documentation_values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File_Type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='fwsreview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_ID', models.IntegerField()),
                ('Threat', models.CharField(max_length=60)),
                ('Date_Certified', models.DateTimeField()),
                ('Certifier_Name', models.CharField(max_length=255)),
                ('Service_Assessment', models.CharField(max_length=255)),
                ('Service_Assessment_Explained', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='huc12',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HUC_12', models.CharField(max_length=50)),
                ('HUC12_Name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='huc12_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Entered', models.DateTimeField()),
                ('User', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='imp_party_values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Implementation_Party', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='implementation_info',
            fields=[
                ('Project_ID', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Prj_ID', models.IntegerField(default=0)),
                ('Project_Name', models.TextField()),
                ('Imp_Status', models.IntegerField(default=0)),
                ('Start_Date', models.DateField()),
                ('Finish_Date', models.DateField()),
                ('In_Perpetuity', models.BooleanField()),
                ('Effective_Determined', models.IntegerField(default=0)),
                ('Effective_Explained', models.TextField()),
                ('Reas_Certain', models.IntegerField(default=0)),
                ('Legal_Authority', models.IntegerField(default=0)),
                ('Staff_Available', models.IntegerField(default=0)),
                ('Regulatory_Mech', models.IntegerField(default=0)),
                ('Compliance', models.IntegerField(default=0)),
                ('Vol_Incentives', models.IntegerField(default=0)),
                ('Reduce_Threats', models.IntegerField(default=0)),
                ('Incremental_Objectives', models.IntegerField(default=0)),
                ('Quantifiable_Measures', models.IntegerField(default=0)),
                ('AD_Strategy', models.IntegerField(default=0)),
                ('Imp_and_Effect_Correct', models.IntegerField(default=0)),
                ('Imp_and_Effect_Cor_Explan', models.TextField()),
                ('Date_Entered', models.DateTimeField()),
                ('User', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='location_check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(max_length=2)),
                ('County', models.CharField(max_length=50)),
                ('HUC12', models.CharField(max_length=50)),
                ('Pop_Name', models.CharField(max_length=50)),
                ('WAFWA_Zone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='location_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Loc_Type', models.CharField(max_length=50)),
                ('Loc_Value', models.CharField(max_length=100)),
                ('Date_Entered', models.DateTimeField()),
                ('User', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Metric', models.CharField(max_length=100)),
                ('Text', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='metrics',
            fields=[
                ('Project_ID', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('BreedingNestingAcres', models.FloatField()),
                ('BroodRearingAcres', models.FloatField()),
                ('WinterAcres', models.FloatField()),
                ('TotalAcres', models.FloatField()),
                ('BreedingNestingMiles', models.FloatField()),
                ('BroodRearingMiles', models.FloatField()),
                ('WinterMiles', models.FloatField()),
                ('TotalMiles', models.FloatField()),
                ('BreedingNestingNumberBirds', models.FloatField()),
                ('BroodRearingNumberBirds', models.FloatField()),
                ('WinterNumberBirds', models.FloatField()),
                ('TotalNumberBirds', models.FloatField()),
                ('BreedingNestingNumberRemoved', models.FloatField()),
                ('BroodRearingNumberRemoved', models.FloatField()),
                ('WinterNumberRemoved', models.FloatField()),
                ('TotalNumberRemoved', models.FloatField()),
                ('BreedingNestingNumberKilled', models.FloatField()),
                ('BroodRearingNumberKilled', models.FloatField()),
                ('WinterNumberKilled', models.FloatField()),
                ('TotalNumberKilled', models.FloatField()),
                ('BreedingNestingEquids', models.FloatField()),
                ('BroodRearingEquids', models.FloatField()),
                ('WinterEquids', models.FloatField()),
                ('TotalEquids', models.FloatField()),
                ('Target_Species', models.CharField(max_length=75)),
                ('Date_Entered', models.DateTimeField()),
                ('User', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ownership_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Entered', models.DateTimeField()),
                ('User', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ownership_values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Owners', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='population_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Entered', models.DateTimeField()),
                ('User', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='population_values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Populations', models.CharField(max_length=50)),
                ('Pop_Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='project_info',
            fields=[
                ('Project_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Project_Name', models.CharField(max_length=75, unique=True)),
                ('Entry_Type', models.IntegerField(default=0)),
                ('Shapefile', models.CharField(max_length=255)),
                ('Metadata', models.CharField(max_length=255)),
                ('Location_Info', models.CharField(max_length=255)),
                ('Location_Desc', models.TextField()),
                ('TypeAct', models.CharField(max_length=30)),
                ('Activity', models.CharField(max_length=75)),
                ('SubActivity', models.CharField(max_length=100)),
                ('seeding_type', models.CharField(max_length=60)),
                ('post_fire', models.IntegerField()),
                ('Start_Date', models.DateField()),
                ('End_Date', models.DateField()),
                ('Objectives_Desc', models.TextField()),
                ('Effects_Desc', models.TextField()),
                ('Implementing_Party', models.TextField()),
                ('Metric', models.CharField(max_length=10)),
                ('Metric_Value', models.IntegerField(default=0)),
                ('GIS_Acres', models.FloatField(default=0)),
                ('Office', models.CharField(max_length=100)),
                ('Created_By', models.CharField(max_length=50)),
                ('Date_Created', models.DateTimeField(default=datetime.datetime(2018, 9, 27, 13, 5, 32, 893000))),
                ('User_Phone_Number', models.CharField(max_length=12)),
                ('User_Email', models.CharField(max_length=100)),
                ('Project_Status', models.IntegerField(default=0)),
                ('Last_Updated', models.DateTimeField(default=datetime.datetime(2018, 9, 27, 13, 5, 32, 893000))),
                ('Updating_User', models.CharField(max_length=50)),
                ('Approved', models.IntegerField(default=0)),
                ('Approving_Official', models.CharField(max_length=50)),
                ('Date_Approved', models.DateTimeField()),
                ('PageLoc', models.CharField(default=b'None', max_length=15)),
                ('LCMItem', models.CharField(max_length=50)),
                ('LC_Zoom', models.IntegerField(default=7)),
                ('LC_Center_X', models.FloatField(default=0)),
                ('LC_Center_Y', models.FloatField(default=0)),
                ('Notes', models.TextField()),
                ('Agreement_Length', models.IntegerField(default=0)),
                ('Agreement_Penalty', models.IntegerField(default=0)),
                ('Mark_For_Deletion', models.BooleanField(default=False)),
                ('Wobble_GIS', models.BooleanField(default=False)),
                ('Batch_Upload', models.BooleanField(default=False)),
                ('Wobbled_GIS', models.BooleanField(default=False)),
                ('Ag_Conversion_Explain', models.TextField()),
                ('Conifer_Encroach_Explain', models.TextField()),
                ('Oil_Gas_Explain', models.TextField()),
                ('Feral_Equids_Explain', models.TextField()),
                ('Infrastructure_Explain', models.TextField()),
                ('Mining_Explain', models.TextField()),
                ('Recreation_Explain', models.TextField()),
                ('Urban_Devel_Explain', models.TextField()),
                ('Fire_Explain', models.TextField()),
                ('Improper_Grazing_Explain', models.TextField()),
                ('Isolated_Explain', models.TextField()),
                ('Invasives_Explained', models.TextField()),
                ('Sagebrush_Loss_Explain', models.TextField()),
                ('Fire_Break_Width_ft', models.IntegerField(default=0)),
                ('CCAA_Num_Permit_Holders', models.IntegerField(default=0)),
                ('Type_of_Powerline', models.TextField()),
                ('BatchUploadFileName', models.TextField()),
                ('BatchUploadFolderName', models.TextField()),
                ('BatchUploadOBJECTID', models.IntegerField(default=0)),
                ('Prj_ID', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='project_query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_ID', models.IntegerField()),
                ('Project_Name', models.CharField(max_length=75)),
                ('User', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(max_length=2)),
                ('StateName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='state_county',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(max_length=2)),
                ('County', models.CharField(max_length=50)),
                ('Cnty_St', models.CharField(max_length=52)),
            ],
        ),
        migrations.CreateModel(
            name='state_county_huc12_values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(max_length=2)),
                ('County', models.CharField(max_length=50)),
                ('HUC12', models.CharField(max_length=50)),
                ('HUC12_Cnty_State', models.CharField(max_length=60)),
                ('Cnty_St', models.CharField(max_length=52)),
            ],
        ),
        migrations.CreateModel(
            name='state_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Entered', models.DateTimeField()),
                ('User', models.CharField(max_length=50)),
                ('Project_ID', models.ForeignKey(db_column=b'Project_ID', on_delete=django.db.models.deletion.PROTECT, to='ced_main.project_info')),
                ('State_Value', models.ManyToManyField(db_column=b'State', to='ced_main.state')),
            ],
        ),
        migrations.CreateModel(
            name='subactivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubActivity', models.CharField(max_length=100)),
                ('Activity', models.CharField(max_length=100)),
                ('TypeAct', models.CharField(max_length=20)),
                ('SubActivity_Query_Label', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='subactivity_effectiveness_rating_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity', models.CharField(max_length=100)),
                ('SubActivity', models.CharField(max_length=100)),
                ('Effectiveness_Rating', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='subactivity_effectiveness_statement_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity', models.CharField(max_length=100)),
                ('SubActivity', models.CharField(max_length=100)),
                ('Effectiveness_Statement', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='subactivity_methods_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity', models.CharField(max_length=100)),
                ('SubActivity', models.CharField(max_length=100)),
                ('Method', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='subactivity_objectives_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity', models.CharField(max_length=100)),
                ('SubActivity', models.CharField(max_length=100)),
                ('Objective', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='threat_values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Threats', models.CharField(max_length=75)),
                ('TypeAct', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='threats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Entered', models.DateTimeField()),
                ('User', models.CharField(max_length=50)),
                ('Project_ID', models.ForeignKey(db_column=b'Project_ID', on_delete=django.db.models.deletion.PROTECT, to='ced_main.project_info')),
                ('Threat', models.ManyToManyField(db_column=b'Threats', to='ced_main.threat_values')),
            ],
        ),
        migrations.CreateModel(
            name='typeact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypeAct', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='wafwa_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Entered', models.DateTimeField()),
                ('User', models.CharField(max_length=50)),
                ('Project_ID', models.ForeignKey(db_column=b'Project_ID', on_delete=django.db.models.deletion.PROTECT, to='ced_main.project_info')),
            ],
        ),
        migrations.CreateModel(
            name='wafwa_zone_values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WAFWA_Zone', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='wafwa_info',
            name='WAFWA_Value',
            field=models.ManyToManyField(db_column=b'WAFWA_Zone', to='ced_main.wafwa_zone_values'),
        ),
        migrations.AddField(
            model_name='population_info',
            name='Population_Value',
            field=models.ManyToManyField(db_column=b'Populations', to='ced_main.population_values'),
        ),
        migrations.AddField(
            model_name='population_info',
            name='Project_ID',
            field=models.ForeignKey(db_column=b'Project_ID', on_delete=django.db.models.deletion.PROTECT, to='ced_main.project_info'),
        ),
        migrations.AddField(
            model_name='ownership_info',
            name='Owner_Value',
            field=models.ManyToManyField(db_column=b'Owners', to='ced_main.ownership_values'),
        ),
        migrations.AddField(
            model_name='ownership_info',
            name='Project_ID',
            field=models.ForeignKey(db_column=b'Project_ID', on_delete=django.db.models.deletion.PROTECT, to='ced_main.project_info'),
        ),
        migrations.AddField(
            model_name='location_info',
            name='Project_ID',
            field=models.ForeignKey(db_column=b'Project_ID', on_delete=django.db.models.deletion.PROTECT, to='ced_main.project_info'),
        ),
        migrations.AddField(
            model_name='huc12_info',
            name='HUC12_Value',
            field=models.ManyToManyField(db_column=b'HUC12_Cnty_State', to='ced_main.state_county_huc12_values'),
        ),
        migrations.AddField(
            model_name='huc12_info',
            name='Project_ID',
            field=models.ForeignKey(db_column=b'Project_ID', on_delete=django.db.models.deletion.PROTECT, to='ced_main.project_info'),
        ),
        migrations.AddField(
            model_name='county_info',
            name='County_Value',
            field=models.ManyToManyField(db_column=b'Cnty_St', to='ced_main.state_county'),
        ),
        migrations.AddField(
            model_name='county_info',
            name='Project_ID',
            field=models.ForeignKey(db_column=b'Project_ID', on_delete=django.db.models.deletion.PROTECT, to='ced_main.project_info'),
        ),
        migrations.AddField(
            model_name='collab_party',
            name='Collab_Party',
            field=models.ManyToManyField(db_column=b'Implementation_Party', to='ced_main.imp_party_values'),
        ),
        migrations.AddField(
            model_name='collab_party',
            name='Project_ID',
            field=models.ForeignKey(db_column=b'Project_ID', on_delete=django.db.models.deletion.PROTECT, to='ced_main.project_info'),
        ),
    ]
