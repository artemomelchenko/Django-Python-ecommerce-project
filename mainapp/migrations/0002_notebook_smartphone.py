from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('diagonal', models.CharField(max_length=255)),
                ('display_type', models.CharField(max_length=255)),
                ('resolution', models.CharField(max_length=255)),
                ('accum_volume', models.CharField(max_length=255)),
                ('ram', models.CharField(max_length=255)),
                ('sd', models.BooleanField(default=True)),
                ('sd_volume_max', models.CharField(max_length=255)),
                ('main_cam_mp', models.CharField(max_length=255)),
                ('frontal_cam_mp', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('diagonal', models.CharField(max_length=255)),
                ('display_type', models.CharField(max_length=255)),
                ('processor_freq', models.CharField(max_length=255)),
                ('ram', models.CharField(max_length=255)),
                ('video', models.CharField(max_length=255)),
                ('time_without_charge', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
