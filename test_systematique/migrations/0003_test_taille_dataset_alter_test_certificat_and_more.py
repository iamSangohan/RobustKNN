# Generated by Django 5.0.3 on 2024-03-15 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_systematique', '0002_alter_test_certificat_alter_test_falsification_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='taille_dataset',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='certificat',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='test',
            name='falsification',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='test',
            name='inconnu',
            field=models.IntegerField(default=0),
        ),
    ]
