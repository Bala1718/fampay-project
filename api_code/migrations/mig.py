from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtubevideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=1000)),
                ('unique_id', models.CharField(max_length=100)),
                ('published_at', models.CharField(max_length=1000)),
            ],
        ),
    ]