
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50, verbose_name='评论内容')),
                ('created_time', models.DateTimeField(verbose_name='创建时间')),
                ('parent_message', models.IntegerField(verbose_name='父留言')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserProfile')),
            ],
        ),
    ]
