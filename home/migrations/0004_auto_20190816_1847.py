# Generated by Django 2.2.4 on 2019-08-16 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190816_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('summary', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('pub_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='first_name',
            field=models.CharField(default='Dmitry', max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='last_name',
            field=models.CharField(default='Shmelev', max_length=20),
        ),
    ]
