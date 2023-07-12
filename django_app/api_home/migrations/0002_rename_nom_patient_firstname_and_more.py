from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='nom',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='prenom',
            new_name='lastname',
        ),
        migrations.AlterField(
            model_name='patient',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
