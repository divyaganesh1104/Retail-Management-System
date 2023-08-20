# Generated by Django 4.2.1 on 2023-08-15 13:55

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_id', models.CharField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('custom_contact', models.IntegerField()),
                ('custom_add', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=100)),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_gen', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('emp_contact', models.IntegerField()),
                ('emp_add', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item_cls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_cls_id', models.CharField(max_length=100, unique=True)),
                ('item_cls_name', models.CharField(max_length=100)),
                ('packed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5)),
                ('same', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, null=True)),
                ('no_of_diff', models.IntegerField(blank=True, null=True)),
                ('qty', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_cls_id', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product_cls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_cls_id', models.CharField(max_length=100, unique=True)),
                ('product_cls_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_id', models.CharField(max_length=100)),
                ('supplier_id', models.CharField(max_length=100)),
                ('bill_no', models.CharField(max_length=100, unique=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_id', models.CharField(max_length=100, null=True)),
                ('purchase_item_cls', models.CharField(max_length=200, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_id', models.CharField(max_length=100, unique=True)),
                ('supplier_name', models.CharField(max_length=100)),
                ('supplier_phone', models.IntegerField()),
                ('supplier_email', models.EmailField(max_length=200, null=True)),
                ('supplier_add', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SaleEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_id', models.CharField(max_length=100, null=True)),
                ('sell_date', models.DateField(null=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_item_id', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.item_cls')),
                ('sale_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.saleentry')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=100, null=True, unique=True)),
                ('product_name', models.CharField(max_length=100)),
                ('product_product_cls', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productClass', to='myapp.product_cls')),
            ],
        ),
        migrations.CreateModel(
            name='ItemStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=100)),
                ('barcode', models.ImageField(blank=True, upload_to='images/')),
                ('sales_status', models.CharField(max_length=100)),
                ('purchase_rate', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('selling_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('image', models.CharField(default='image not found', max_length=100)),
                ('status_qty', models.IntegerField(null=True)),
                ('item_cls_status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.item_cls')),
                ('purchase_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.purchase')),
            ],
        ),
        migrations.CreateModel(
            name='ItemClsDiffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_cls_differ_id', models.CharField(max_length=100)),
                ('specification', models.CharField(max_length=100)),
                ('item_cls_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.item_cls')),
            ],
        ),
        migrations.AddField(
            model_name='item_cls',
            name='item_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.product'),
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is admin')),
                ('is_manager', models.BooleanField(default=False, verbose_name='Is manager')),
                ('is_salesperson', models.BooleanField(default=False, verbose_name='Is salesperson')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]