# Generated by Django 2.0.4 on 2018-04-24 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a goods name', max_length=200)),
                ('description', models.CharField(help_text='Short descriptions for goods(300 sym)', max_length=300)),
                ('gvls', models.BooleanField(default=False, help_text='Is GVLS')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_present', models.BooleanField(default=False, help_text='Is item on the stock')),
                ('amount', models.PositiveIntegerField(help_text='amount of goods')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('exp_date', models.DateField(help_text='date of expiration')),
                ('num_of_series', models.PositiveSmallIntegerField(help_text='Number of series of goods')),
                ('goods', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.Goods')),
            ],
            options={
                'ordering': ['goods'],
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of Supplier', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('payment_delay', models.PositiveSmallIntegerField(blank='True', default=0, help_text='delay of payment for supplier')),
                ('enabled', models.BooleanField(default=True, help_text='Is cooperation enabled')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.Supplier'),
        ),
    ]
