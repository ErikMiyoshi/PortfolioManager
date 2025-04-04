# Generated by Django 5.1.7 on 2025-03-24 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_type',
            field=models.CharField(choices=[('savings', 'Savings'), ('fixed_income BR', 'Fixed Income BR'), ('stock_br', 'Stock BR'), ('real_state_br', 'Real State (BR)'), ('stock_us', 'Stock US'), ('long_time_inv', 'Long Time Investiment'), ('fixed_income US', 'Fixed Income US'), ('real_state_us', 'Real State (US)'), ('emergency_fund', 'Emergency Fund'), ('crypto', 'Cryptocurrency')], max_length=20),
        ),
        migrations.AlterField(
            model_name='asset',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='rate_type',
            field=models.CharField(blank=True, choices=[('prefixed', 'Prefixed'), ('post_fixed', 'Post Fixed'), ('hybrid', 'Hybrid')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='expire_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
