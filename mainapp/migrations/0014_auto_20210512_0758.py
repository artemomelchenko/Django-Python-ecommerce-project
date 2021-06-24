from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20210512_0705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(blank=True, max_length=1024, null=True)),
                ('status', models.CharField(choices=[('new', 'New Order'), ('in_progress', 'In Progress'), ('is_ready', 'Is Ready'), ('completed', 'Completed')], default='new', max_length=100, verbose_name='Status')),
                ('buying_type', models.CharField(choices=[('self', 'Self'), ('delivery', 'Delivery')], default='self', max_length=100, verbose_name='Type')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created at')),
                ('order_date', models.DateField(default=django.utils.timezone.now, verbose_name='Order Date')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_orders', to='mainapp.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(related_name='related_customer', to='mainapp.Order', verbose_name='Customers Orders'),
        ),
    ]
