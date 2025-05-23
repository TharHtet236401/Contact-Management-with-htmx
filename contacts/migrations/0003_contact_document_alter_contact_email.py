# Generated by Django 5.1.3 on 2025-04-07 17:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='contact_docs/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'docx', 'txt'])]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
