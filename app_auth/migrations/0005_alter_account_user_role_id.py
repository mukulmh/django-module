# Generated by Django 4.1 on 2022-09-15 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0004_userrole_alter_screen_screen_code_rolewise_screen'),
        ('app_auth', '0004_account_user_role_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_role_id',
            field=models.ForeignKey(default=3, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_admin.userrole'),
        ),
    ]