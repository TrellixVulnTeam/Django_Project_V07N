# Generated by Django 3.0.3 on 2020-08-06 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200806_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='accounts.Tag'),
        ),
    ]
