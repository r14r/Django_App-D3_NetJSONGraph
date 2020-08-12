# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 12:25
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsongraph', '0005_snapshot'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snapshot',
            options={'verbose_name_plural': 'snapshots'},
        ),
        migrations.AlterField(
            model_name='topology',
            name='parser',
            field=models.CharField(choices=[('netdiff.OlsrParser', 'OLSRd (txtinfo/jsoninfo)'), ('netdiff.BatmanParser', 'batman-advanced (jsondoc/txtinfo)'), ('netdiff.BmxParser', 'BMX6 (q6m)'), ('netdiff.NetJsonParser', 'NetJSON NetworkGraph'), ('netdiff.CnmlParser', 'CNML 1.0'), ('netdiff.OpenvpnParser', 'OpenVPN')], help_text='Select topology format', max_length=128, verbose_name='format'),
        ),
    ]
