# Generated by Django 5.0.3 on 2024-03-20 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0010_delete_return_issue_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
