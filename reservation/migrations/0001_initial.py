# Generated by Django 5.1.6 on 2025-02-23 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='نام و نام خانوادگی خود را وارد کنید', max_length=100, verbose_name='نام کامل')),
                ('email', models.EmailField(help_text='example@domain.com', max_length=254, verbose_name='آدرس ایمیل')),
                ('phone', models.CharField(help_text='شماره تماس با پیشوند کشور مثلاً 00989123456789', max_length=15, verbose_name='شماره تماس')),
                ('number_of_people', models.IntegerField(choices=[(1, '1 نفر'), (2, '2 نفر'), (3, '3 نفر'), (4, '4 نفر'), (5, '5+ نفر')], default=2, verbose_name='تعداد نفرات')),
                ('date', models.DateField(help_text='تاریخ مورد نظر برای رزرو', verbose_name='تاریخ رزرو')),
                ('time', models.TimeField(help_text='زمان مورد نظر برای رزرو', verbose_name='زمان رزرو')),
                ('special_request', models.TextField(blank=True, help_text='درخواست\u200cهای خاص مانند میز VIP، جشن تولد و...', null=True, verbose_name='درخواست ویژه')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('is_confirmed', models.BooleanField(default=False, verbose_name='تأیید شده')),
            ],
            options={
                'verbose_name': 'رزرواسیون',
                'verbose_name_plural': 'رزرواسیون\u200cها',
                'ordering': ['-date', '-time'],
            },
        ),
    ]
