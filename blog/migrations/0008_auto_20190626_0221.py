# Generated by Django 2.2.2 on 2019-06-26 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190626_0211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-updated', '-timestamp']},
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='update',
            new_name='updated',
        ),
    ]
