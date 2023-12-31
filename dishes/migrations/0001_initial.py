# Generated by Django 4.0.6 on 2023-10-27 01:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dishe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('item_description', models.TextField()),
                ('stock', models.IntegerField()),
                ('image_url', models.ImageField(upload_to='static/dishes-image')),
            ],
        ),
        migrations.CreateModel(
            name='RecommendProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommend_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dishes.dishe')),
            ],
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('drinks', 'Drinks'), ('gurasa', 'Gurasa'), ('meat', 'Meats'), ('pizza', 'Pizza')], max_length=15)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_name', to='dishes.dishe')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('dishes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dishes.dishe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
