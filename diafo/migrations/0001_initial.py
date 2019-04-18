# Generated by Django 2.2 on 2019-04-18 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('view_id', models.CharField(default=uuid.uuid4, max_length=50, unique=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('requires_sign_in', models.BooleanField(blank=True, default=True)),
                ('collect_identity', models.BooleanField(blank=True, default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_type', models.CharField(choices=[('Short_answer', 'One Line Answer'), ('Paragraph', 'Multiple Line Answer'), ('Integer', 'Integer Answer'), ('ChoiceField', 'Choice'), ('MultipleChoiceField', 'Multiple-choice')], max_length=50, null=True)),
                ('question', models.CharField(max_length=1000, null=True)),
                ('question_choices', models.TextField(blank=True, help_text='make new line for new option', max_length=600, null=True)),
                ('required', models.BooleanField(default=True)),
                ('questionnaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diafo.Questionnaire')),
            ],
        ),
        migrations.CreateModel(
            name='FilledForm',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False, unique=True)),
                ('data', models.CharField(blank=True, max_length=30000, null=True)),
                ('timestamp', models.DateField(default=django.utils.timezone.now)),
                ('edit_time', models.DateField(default=django.utils.timezone.now, null=True)),
                ('applicant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filled_forms', to=settings.AUTH_USER_MODEL)),
                ('questionnaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diafo.Questionnaire')),
            ],
        ),
    ]
