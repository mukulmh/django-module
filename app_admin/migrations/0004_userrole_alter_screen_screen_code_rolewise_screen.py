# Generated by Django 4.1 on 2022-09-14 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0003_alter_screen_screen_fa_icon_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=200, unique=True)),
                ('role_code', models.IntegerField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='screen',
            name='screen_code',
            field=models.IntegerField(unique=True),
        ),
        migrations.CreateModel(
            name='Rolewise_screen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add', models.BooleanField()),
                ('read', models.BooleanField()),
                ('destroy', models.BooleanField()),
                ('edit', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.userrole')),
                ('screen_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.screen')),
            ],
        ),
    ]
