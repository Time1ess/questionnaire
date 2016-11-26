#!/usr/bin/env python
# coding=utf-8
from playhouse.pool import PooledMYSQLDatabase
from playhouse.shortcuts import RetryOptionalError
from conf import mysql_conf

class RetyPooledMysqlDB(RetryOptionalError, PooledMYSQLDatabase):
    pass

questionDB = RetyPooledMysqlDB(
    database=mysql_conf.question_db_name,
    host=mysql_conf.question_db_host,
    port=mysql_conf.question_db_port,
    user=mysql_conf.question_db_user,
    password=mysql_conf.question_db_password,
)
