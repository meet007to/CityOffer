# Generated by Django 3.0.5 on 2020-06-05 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminsite', '0001_initial'),
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=100.0, max_digits=20)),
                ('chackedprise', models.DecimalField(decimal_places=2, default=50.0, max_digits=20)),
                ('description', models.CharField(default='It for a ...', max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products')),
                ('status', models.CharField(default='A', max_length=10)),
                ('catname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminsite.Category')),
                ('email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.ShopKeeper')),
                ('subname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminsite.SubCategory')),
            ],
        ),
    ]
