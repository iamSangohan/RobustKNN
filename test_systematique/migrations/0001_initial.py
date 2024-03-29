# Generated by Django 5.0.3 on 2024-03-15 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb_input', models.IntegerField()),
                ('seuil_poisoning', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('falsification', models.IntegerField()),
                ('certificat', models.IntegerField()),
                ('inconnu', models.IntegerField()),
                ('temps_ecoulé', models.IntegerField()),
                ('dataset', models.CharField(choices=[('Iris', 'Iris'), ('Digits', 'Digits')], max_length=100)),
            ],
        ),
    ]
