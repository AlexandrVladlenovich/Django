# Generated by Django 4.2.4 on 2023-09-01 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_app', '0004_alter_product_add_day_alter_user_reg_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=None, upload_to='image/'),
        ),
    ]