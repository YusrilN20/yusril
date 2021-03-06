# Generated by Django 4.0.5 on 2022-06-14 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateField(auto_created=True, auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to='flower_imgs/', verbose_name='image')),
                ('posting', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
