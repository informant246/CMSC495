# Generated by Django 4.0.3 on 2022-03-24 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BugTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bug_title', models.CharField(max_length=200)),
                ('project_name', models.CharField(max_length=100)),
                ('date_occured', models.DateField()),
                ('bug_description', models.TextField()),
                ('date', models.DateTimeField()),
                ('bug_risk', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Low', max_length=7)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]