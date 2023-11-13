# Generated by Django 3.2 on 2023-11-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_forms', '0016_auto_20231108_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileuploadfieldplugin',
            name='invalid_extension_message',
            field=models.TextField(blank=True, help_text='Error message displayed if extensions are constrained and the file fails that validation.Default: "File extension [extension] is not allowed for this field.".', null=True, verbose_name='Extension validation error message'),
        ),
        migrations.AddField(
            model_name='imageuploadfieldplugin',
            name='invalid_extension_message',
            field=models.TextField(blank=True, help_text='Error message displayed if extensions are constrained and the file fails that validation.Default: "File extension [extension] is not allowed for this field.".', null=True, verbose_name='Extension validation error message'),
        ),
        migrations.AlterField(
            model_name='formsubmission',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='option',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
