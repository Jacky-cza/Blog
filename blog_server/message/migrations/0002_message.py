
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0001_initial'),
        ('user', '0001_initial'),
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=60, verbose_name='评论内容')),
                ('parent_message', models.IntegerField(verbose_name='回复的留言')),
                ('created_time', models.DateTimeField(verbose_name='创建时间')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserProfile')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic.Topic')),
            ],
            options={
                'db_table': 'message',
            },
        ),
    ]
