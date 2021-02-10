# Generated by Django 3.1.6 on 2021-02-10 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubCategory', models.CharField(max_length=50)),
                ('Parent_Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.cat')),
            ],
        ),
        migrations.CreateModel(
            name='WorkHour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Worked', models.DateField()),
                ('Hours', models.SmallIntegerField(default=0)),
                ('Minutes', models.IntegerField(default=0)),
                ('Work_Description', models.CharField(max_length=200)),
                ('Rework', models.BooleanField()),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.employee')),
                ('Task_Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.subcat')),
            ],
        ),
    ]
