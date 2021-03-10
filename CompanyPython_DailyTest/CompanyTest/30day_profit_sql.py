#coding=UTF-8
#remark=生成用户30天收益

import  pymysql,pytest
import random
from CompanyPython_DailyTest.CompanyTest.mysql_class import MysqlDB

class TestFrofit():

    @pytest.mark.parametrize(("user_id"), ["421422222"])
    def test_frofit(self,user_id):
        id = random.randint(90000000,99000000)
        print(id)
        db = MysqlDB('172.29.2.157', 'yjsdata', 'PtSjKmMkFwY666', 'yyfax_statistics', 3343, 'utf8')
        sql = "INSERT into tb_user_profit_statistics (id,etl_date,user_id,business_date,amount,insert_time,create_time,update_time)\
                VALUES(%d,now(),'%s','2020-05-03','21',now(),now(),now())" % (id, user_id)
        db.handle_db(sql)
        data = db.get_data_from_db("SELECT user_id from tb_user_profit_statistics WHERE id=id")
        print(data)


# id = random.randint(90000000,99000000)
# user_id='4343243'
# db = MysqlDB('172.29.2.157', 'yjsdata', 'PtSjKmMkFwY666', 'yyfax_statistics', 3343, 'utf8')
# sql = "INSERT into tb_user_profit_statistics (id,etl_date,user_id,business_date,amount,insert_time,create_time,update_time)VALUES(%d,now(),'%s','2020-05-03','21',now(),now(),now())" % (id,user_id)
# db.handle_db(sql)


