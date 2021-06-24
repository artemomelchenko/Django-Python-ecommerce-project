from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_somemodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SomeModel',
        ),
    ]
