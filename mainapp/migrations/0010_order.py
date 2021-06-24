from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20210510_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, )),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255, )),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=1024, null=True)),
                ('buying_type', models.CharField(choices=[('self', 'Self'), ('delivery', 'Delivery')], default='self', max_length=30, verbose_name='Type')),
                ('status', models.CharField(choices=[('new', 'New Order'), ('in_progress', 'In Progress'), ('ready', 'Ready'), ('completed', 'Completed')], default='new', max_length=40, verbose_name='Status')),
                ('comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='Comment')),
                ('carts', models.ManyToManyField(to='mainapp.Cart')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Customer')),
            ],
        ),
    ]
