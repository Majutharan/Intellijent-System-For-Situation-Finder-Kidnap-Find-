# Generated by Django 2.1.1 on 2018-11-14 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kidnap', '0008_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
