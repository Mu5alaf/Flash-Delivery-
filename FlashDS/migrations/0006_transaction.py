# Generated by Django 4.2.7 on 2023-11-26 12:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FlashDS', '0005_request_distance_request_duration_request_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_request_payment_id', models.CharField(max_length=255, unique=True)),
                ('payment_amount', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('task_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FlashDS.request')),
            ],
        ),
    ]