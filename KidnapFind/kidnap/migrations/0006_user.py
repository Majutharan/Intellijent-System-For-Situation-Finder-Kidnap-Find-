# Generated by Django 2.1.1 on 2018-11-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kidnap', '0005_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('work', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('mail_id', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
