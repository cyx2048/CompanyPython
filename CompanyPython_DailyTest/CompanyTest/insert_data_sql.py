#coding=UTF-8
#remark=

# import pymysql
# import random
# NUM = 0
# db = pymysql.connect(host='IP', user='', passwd='', db='', port=, charset='utf8')
# cursor = db.cursor()
#
# for i in range(100):
#     Ageint = 20 + random.randint(0, 40)
#     IMCONME = 10000 + random.randint(0, 1000)
#     NUM += 1
#     NAME ='name'+str(NUM)
#     Nation ='CHINA', 'JAPAN', 'UK', 'USA', 'GERMAN', 'FRANCE', 'KOREA', 'BRAZIL'
#     Lastname = 'SMTH','KOBE', 'MICHEAEL', 'JASON', 'FUCK', 'STUPID'
#     Hobby = 'FOOTBALL', 'BASKETBALL', 'VOLLEBALL'
#     COME = random.choice(Nation)
#     LASTNAME = random.choice(Lastname)
#     HOBBY = random.choice(Hobby)
#     sql ="INSERT  test1y(id, firstname, middlename, lastname, comefrom, age, income, hobby) VALUES ('%d', '%s','%s','%s', '%s', '%d', '%d' ,'%s')"% (NUM, NAME, COME, LASTNAME, COME, Ageint, IMCONME,HOBBY)
#     cursor.execute(sql)
#     db.commit()
# cursor.close()
# db.close()


import pymysql
import random
db = pymysql.connect(host='172.29.3.197', user='yjsdata', passwd='PtSjKmMkFwY666', db='yyfax_galaxy', port=3306, charset='utf8')
cursor = db.cursor()

for i in range(1000):
    id = int('2020'+''.join(random.sample('1234567890', 6)) + ''.join(str(i) for i in random.sample(range(0, 9), 9)))
    service_code = 'YHT'
    user_id = 'u'+''.join(random.sample('1234567890', 5)) + ''.join(str(i) for i in random.sample(range(0, 9), 8))
    third_user_id = 'UP202' + ''.join(str(i) for i in random.sample(range(0, 9), 9))
    phone = '138' + ''.join(str(i) for i in random.sample(range(0, 9), 8))
    id_card_cip = ''.join(random.sample('QC1JLbpp+7Kt/0dBSwUswNEIPQhvzq2z0WYddFnby0Y=', 20))
    name = ''.join(random.sample('陈王孙李赵钱花园黑许徐金魏马伟唐汤', 1)) + ''.join(
        random.sample('创业公司研发中心负责人第二届大微信开发者主页学生微信小程序应用开发大赛全国三等奖项目第一作者', 2))
    create_time = '2020-05-09 00:00:00'
    update_time = '2020-05-09 00:00:00'
    remark = 'sql插入'
    sql = "INSERT into tb_auth_register_info (id,service_code,user_id,provider_code,third_user_id,phone,id_card_cip,name,status,create_time,update_time,remark)\
          VALUES(%d,'%s','%s','000018','%s','%s','%s','%s',1,NOW(),NOW(),'python插入')" % (
    id, service_code, user_id, third_user_id, phone, id_card_cip, name)
    cursor.execute(sql)
    db.commit()

cursor.close()
db.close()



