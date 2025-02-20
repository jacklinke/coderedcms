# Generated by Django 5.1.6 on 2025-02-17 15:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0094_alter_page_locale'),
        ('website', '0002_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='footers', to='wagtailcore.site'),
        ),
        migrations.AddField(
            model_name='navbar',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='navbars', to='wagtailcore.site'),
        ),
    ]
