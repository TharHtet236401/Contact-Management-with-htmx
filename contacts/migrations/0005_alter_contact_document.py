# Generated by Django 5.1.3 on 2025-04-21 03:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_alter_contact_document_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='contact_docs/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'doc', 'txt', 'ppt', 'pptx'])]),
        ),
    ]
