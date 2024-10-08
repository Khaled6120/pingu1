# Generated by Django 5.1 on 2024-09-02 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('reference', models.URLField(blank=True, null=True)),
                ('description', models.TextField()),
                ('rule_text', models.TextField()),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('tags', models.CharField(max_length=200)),
            ],
        ),
    ]
