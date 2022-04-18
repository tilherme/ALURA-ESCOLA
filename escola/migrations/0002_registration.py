# Generated by Django 4.0.4 on 2022-04-15 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('M', 'Noturno')], default='M', max_length=1)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.aluno')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.course')),
            ],
        ),
    ]