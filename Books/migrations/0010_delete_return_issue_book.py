# Generated by Django 5.0.3 on 2024-03-20 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0009_alter_return_issue_book_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Return_Issue_Book',
        ),
    ]
