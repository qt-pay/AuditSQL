# Generated by Django 2.0.2 on 2018-02-02 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InceptionHostConfig',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('user', models.CharField(max_length=30, verbose_name='用户名')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
                ('host', models.CharField(max_length=32, verbose_name='ip地址')),
                ('port', models.IntegerField(verbose_name='端口')),
                ('comment', models.CharField(max_length=128, verbose_name='主机描述')),
            ],
            options={
                'verbose_name': 'inception连接数据库配置',
                'verbose_name_plural': 'inception连接数据库配置',
                'db_table': 'sqlaudit_inception_hostconfig',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='InceptionSqlOperateRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键id')),
                ('op_uid', models.IntegerField(default=0, verbose_name='操作用户uid')),
                ('op_user', models.CharField(max_length=30, verbose_name='操作用户')),
                ('step_id', models.IntegerField(default=1, verbose_name='inception输出顺序ID')),
                ('workid', models.CharField(max_length=128, verbose_name='工单号')),
                ('dst_host', models.CharField(max_length=30, verbose_name='操作目标数据库主机')),
                ('dst_database', models.CharField(max_length=80, verbose_name='操作目标数据库')),
                ('stage', models.CharField(default='', max_length=128, verbose_name='inception检测阶段')),
                ('stagestatus', models.CharField(default='', max_length=1024, verbose_name='inception检测阶段状态')),
                ('errlevel', models.IntegerField(default=0, verbose_name='inception输出错误级别')),
                ('errormessage', models.TextField(default='', verbose_name='inception输出错误信息')),
                ('op_sql', models.TextField(default='', verbose_name='执行的SQL')),
                ('affected_rows', models.IntegerField(default=0, verbose_name='影响的行数')),
                ('sequence', models.CharField(default='', max_length=1024, verbose_name='备份记录id，inception生成的sequence')),
                ('backup_dbname', models.CharField(default='', max_length=1024, verbose_name='inception生成的备份的库名')),
                ('execute_time', models.CharField(default='0.000', max_length=128, verbose_name='inception执行时间')),
                ('op_time', models.DateTimeField(auto_now_add=True, verbose_name='用户操作时间')),
            ],
            options={
                'verbose_name': 'inception操作结果记录表',
                'verbose_name_plural': 'inception操作结果记录表',
                'db_table': 'sqlaudit_inception_sql_operate_record',
                'default_permissions': (),
            },
        ),
    ]