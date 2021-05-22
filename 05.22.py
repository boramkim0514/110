
import pymysql

# DB 연동
con = pymysql.connect(host='localhost', user='root', password='25722357', db='acedb', charset='utf8')
c = con.cursor()

sql = "CREATE DATABASE users" 

c.execute(sql) 


con.commit() #실행 저장
con.close() # DB 연결 끊기

