#coding=UTF-8
#remark=操作数据库的方法

import  pymysql

class MysqlDB(object):

    def __init__(self,Host,User,Passwd,DB,Port,Charset):
        self.Host = Host
        self.User = User
        self.Passwd = Passwd
        self.DB = DB
        self.Port = Port
        self.Charset = Charset

    # 连接数据库
    def connect_db(self):
        self.db = pymysql.connect(
            host = self.Host,
            user = self.User,
            passwd = self.Passwd,
            db = self.DB,
            port = self.Port,
            charset= self.Charset
        )
        self.cursor = self.db.cursor()

    # 增删改
    def  handle_db(self,insert_sql):
        self.connect_db()
        self.cursor.execute(insert_sql)
        self.db.commit()
        self.close_db()

    # 读取并返回数据
    def get_data_from_db(self,select_sql):
        # fetchone()这种方法每次只取一条数据
        # fetchmany()一次多条数据，括号内填入要读取的数据条数。不填则为1条数据，如果读数超过实际条数，只显示实际条数。
        # fetchall()一次读取全部数据，如果管道内没有数据，则返回空元组或空列表。
        self.connect_db()
        self.cursor.execute(select_sql)
        data = self.cursor.fetchall()
        return data

    # 关闭数据库关闭游标
    def close_db(self):
        self.cursor.close()
        self.db.close()

# mysql = MysqlDB('172.29.3.197','yjsdata','PtSjKmMkFwY666','yyfax_galaxy',3306,'utf8')
# mysql.handle_db("INSERT INTO tb_auth_register_info VALUES(2560927980335736236,'YZT','312342354','000018','UP4343432838','15760090988','dasfasgfe','王二小','1',NOW(),NOW(),'python操作数据')")
# mysql.handle_db("DELETE from tb_auth_register_info WHERE remark='python操作数据'")
# data = mysql.get_data_from_db("SELECT * from tb_auth_register_info WHERE remark='python操作数据'")
# print(data)






