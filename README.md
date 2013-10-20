Python-MySQLdb-example
======================

Python-MySQLdb-example

本文主要介绍通过MySQLdb实现Python对MySQL数据库的访问和操作。

备注：execute 把一条查询语句发送给mysql服务器，这里有两种情况：
1）CREATE、INSERT、DELETE、UPDATE、DROP等没有返回结果的情况，语句直接被执行。
2）对于SELECT等有返回结果的情况，用cursor.fetchone()、cursor.fetchmany(n)、cursor.fetchall()获取返回的结果，结果集的每一行作为一个元组（tuple）返回。
