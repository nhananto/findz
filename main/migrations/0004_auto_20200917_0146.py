# Generated by Django 3.1.1 on 2020-09-16 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200912_0105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='tutorial_type',
            new_name='pricing',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='level',
            field=models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], default='default--', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutorial',
            name='medium',
            field=models.CharField(choices=[('video', 'Video'), ('blog', 'Blog'), ('book', 'Book')], default='default', max_length=50),
            preserve_default=False,
        ),
    ]
