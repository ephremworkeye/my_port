# Generated by Django 3.2.4 on 2021-06-24 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(blank=True, max_length=250)),
                ('message', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150)),
                ('image', models.ImageField(blank=True, upload_to='portfolio/%Y/%m/%d')),
                ('is_published', models.BooleanField(default=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('website_link', models.URLField(blank=True, max_length=250)),
                ('github_link', models.URLField(blank=True, max_length=350)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('age', models.PositiveIntegerField(blank=True)),
                ('country', models.CharField(blank=True, max_length=120)),
                ('city', models.CharField(blank=True, max_length=120)),
                ('address', models.CharField(blank=True, max_length=250)),
                ('zipcode', models.CharField(blank=True, max_length=120)),
                ('photo', models.ImageField(blank=True, upload_to='portfolio/%Y/%m/%d')),
                ('website', models.URLField(blank=True, max_length=250)),
                ('github', models.URLField(blank=True, max_length=250, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resume')),
                ('profession', models.CharField(blank=True, max_length=100, null=True)),
                ('education', models.CharField(blank=True, max_length=100)),
                ('experience', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('rate', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('body', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('profession', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='testimonial/%Y/%m/%d')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='port.portfolio')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='port.skill')),
            ],
        ),
        migrations.AddField(
            model_name='portfolio',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='port.profile'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='skill',
            field=models.ManyToManyField(blank=True, through='port.PortfolioSkill', to='port.Skill'),
        ),
    ]
