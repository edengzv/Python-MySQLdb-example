#!/usr/bin/python
#coding=utf8
#author:kantian
#date:2013-10-20

import sys
import MySQLdb
#define the connection param
hostname='localhost'
username='root'
password='gnefgnehz'
dbname='test'
tbname='mytest'
port= 3306
charset='utf8'
try:
    conn = MySQLdb.connect(
        host=hostname,
        user=username,
        passwd=password,
        db=dbname,
        port=port,
        charset=charset,
        )
    cursor = conn.cursor()
    #如果表已经存在，则删除·
    cursor.execute("""DROP TABLE IF EXISTS %s""" % (tbname,))
    #创建表
    cursor.execute("""CREATE TABLE IF NOT EXISTS %s(
                        id int(11) not null auto_increment,
                        name char(20) not null,
                        PRIMARY KEY(id)
                        )ENGINE=MyISAM;
        """ % (tbname,))


    #向刚创建的表中插入数据
    cursor.execute("""
        INSERT INTO %s (name)
        VALUES
        ('Monday'),('Thesday'),('Wednesday'),('Thursday'),('Friday'),('Saturday'),('Sunday');
    """ % (tbname,))

    #获取所有查询结果
    print 'fetchall():'
    cursor.execute("""
        SELECT * FROM %s;
    """ % (tbname,))
    res = cursor.fetchall()
    for k in res:
        print 'id %d:%s' % (k[0],k[1])

    #获取3条查询结果
    print 'fetchmany():N=3'
    cursor.execute("""
        SELECT * FROM %s;
    """ % (tbname,))
    res = cursor.fetchmany(3)
    for k in res:
        print 'id %d:%s' % (k[0],k[1])

    #获取一条查询结果
    print 'fetchone()'
    cursor.execute("""
        SELECT * FROM %s;
    """ % (tbname,))
    res = cursor.fetchone()
    print res[0],res[1]
    print cursor.rowcount

    #删除一条数据
    cursor.execute("""
        DELETE FROM %s WHERE id = 1;
    """ % (tbname,))
    print cursor.rowcount


    #更新一条数据
    cursor.execute("""
        UPDATE %s SET name='Congratulations!' WHERE id=2
    """ % (tbname,))

    cursor.close()

    #创建一个字典型的游标，这样可以用名称访问，而不通过下表访问
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("""
        SELECT * FROM %s WHERE id = 5;
    """ % (tbname,))
    row = cursor.fetchone()
    print row['name']

    #关闭游标
    cursor.close()
    #关闭连接
    conn.close()
except MySQLdb.Error,e:
    print 'mysql error %d:%s',(e.args[0],e.args[1])
    sys.exit()

