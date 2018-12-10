# Generated by Django 2.1.1 on 2018-11-14 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kidnap', '0009_auto_20181114_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('video', models.FileField(upload_to='upload/videos')),
            ],
            options={
                'db_table': 'videos',
            },
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]