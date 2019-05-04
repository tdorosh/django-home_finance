# Generated by Django 2.2 on 2019-05-04 10:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Назва')),
                ('amount', models.DecimalField(decimal_places=2, default='00000,00', max_digits=11, verbose_name='Залишок')),
                ('notes', models.TextField(verbose_name='Додаткові відомості')),
                ('create_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата створення')),
                ('is_default', models.BooleanField(verbose_name='За замовчуванням')),
            ],
            options={
                'verbose_name': 'Рахунок',
                'verbose_name_plural': 'Рахунки',
                'ordering': ['amount'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5, verbose_name='Назва')),
                ('full_name', models.CharField(max_length=100, verbose_name='Повна назва')),
                ('is_default', models.BooleanField(verbose_name='За замовчуванням')),
            ],
            options={
                'verbose_name': 'Валюта',
                'verbose_name_plural': 'Валюти',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finance.Category', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Підкатегорія',
                'verbose_name_plural': 'Підкатегорії',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типи',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default='00000,00', max_digits=11, verbose_name='Сума')),
                ('create_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата здійснення')),
                ('notes', models.TextField(verbose_name='Додаткові відомості')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finance.Category', verbose_name='Категорія')),
                ('currencies', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finance.Currency', verbose_name='Валюта')),
                ('from_account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='from_account_set', to='finance.Account', verbose_name='З рахунку')),
                ('on_account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='on_account_set', to='finance.Account', verbose_name='На рахунок')),
                ('subcategories', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finance.Subcategory', verbose_name='Підкатегорія')),
                ('types', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finance.Type', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Трансакція',
                'verbose_name_plural': 'Трансакції',
                'ordering': ['-create_datetime'],
            },
        ),
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finance.Type', verbose_name='Тип'),
        ),
    ]