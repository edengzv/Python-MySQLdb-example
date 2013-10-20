Python-MySQLdb-example
======================

Python-MySQLdb-example

引言：本文主要介绍通过MySQLdb实现Python对MySQL数据库的访问和操作。
一、MySQLdb安装：
1）windows下直接下载 MySQL-python-1.2.4b4.win32-py2.7.exe 安装 
2）linux下
>>> import sys
>>> sys.version
'2.7.2 (default, Jun 24 2011, 12:21:10) [MSC v.1500 32 bit (Intel)]'
>>> import MySQLdb
>>>
导入MySQLdb时没有报错，则MySQLdb成功安装

二、MySQLdb的使用大致包括四个步骤：

1）导入MySQLdb模块  import
2）建立连接 connect
3）操作数据库 update、insert、delete、create、select...
4）关闭连接 close

下面以一个简单的例子演示之：
>>> import MySQLdb
>>> conn = MySQLdb.connect(host='localhost',user='root',passwd='gnefgnehz')
>>> cursor = conn.cursor()
>>> cursor.execute("SELECT VERSION()")
1L
>>> row = cursor.fetchone()
>>> print 'mysql version:',row[0]
mysql version: 5.1.41
>>> cursor.close()
>>> conn.close()
>>>

备注：execute 把一条查询语句发送给mysql服务器，这里有两种情况：
1）CREATE、INSERT、DELETE、UPDATE、DROP等没有返回结果的情况，语句直接被执行。
2）对于SELECT等有返回结果的情况，用cursor.fetchone()、cursor.fetchmany(n)、cursor.fetchall()获取返回的结果，结果集的每一行作为一个元组（tuple）返回。
