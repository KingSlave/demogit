# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('clave', models.IntegerField(serialize=False, primary_key=True)),
                ('ncompras', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='persona',
            fields=[
                ('idPersona', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cliente',
            name='idPersona',
            field=models.ForeignKey(to='ejemplo.persona'),
            preserve_default=True,
        ),
    ]
