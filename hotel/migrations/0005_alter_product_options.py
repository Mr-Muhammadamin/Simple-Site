# Generated by Django 4.2.7 on 2023-12-15 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_alter_comment_likes_alter_comment_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['price']},
        ),
    ]
