
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='publisher',
        ),
        migrations.AlterField(
            model_name='message',
            name='parent_message',
            field=models.IntegerField(verbose_name='回复的留言的id'),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
