# Generated by Django 3.2.9 on 2022-01-12 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outfit',
            old_name='number_clothes',
            new_name='number_items',
        ),
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('E', 'earring'), ('N', 'necklace'), ('B', 'bracelet'), ('W', 'watch'), ('H', 'hat'), ('S', 'scarf')], default='E', max_length=100)),
                ('formality', models.CharField(max_length=100)),
                ('outfit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.outfit')),
            ],
        ),
    ]