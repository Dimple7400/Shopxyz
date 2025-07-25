# Generated by Django 5.1.4 on 2025-05-13 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('Camera', 'Camera'), ('Men', 'Men'), ('Women', 'Women'), ('Goggle', 'Goggles'), ('Shoes', 'Shoes'), ('Mobile', 'Mobiles'), ('Watch', 'Watches'), ('Bag', 'Bags')], max_length=200)),
                ('product_name', models.CharField(max_length=200)),
                ('discount_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('discription', models.TextField()),
                ('brand', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
