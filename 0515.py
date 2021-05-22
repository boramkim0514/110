# 회원정보 (ID, Name) 5명분 받아서
# 아이디 오름차순 정렬
# ID, Name 표시

"""MainCode1"""
import pymysql as 

con = pymysql.connect(host='localhost', user='root', password='25722357', db='acedb', charset='utf8')
c = con.cursors()

#순번 확인
totalCount = 1
print("********* 코드 실행 *********")

try:
    #회원 정보 (ID, Name) 5회 입력 
    for user in range(0,5):
        tem1, tem2 = input("ID, Name: ") .split(',') 
        sql = "INSERT INTO user(ID, Name) VALUES(%s, %s)"
        c.execute(sql, (tem1, tem2))
        con.commit()

    # 입력 확인
    sql = "SELECT * FROM user"
    c.execute(sql)
    result = c.fetchall()
    print(f"****** 입력하신 ID는 {result[-1]} 입니다 ******")
    print(f"------{totalCount}번째 시도 로그인 성공******", "\n")
    totalCount += 1

except Exception as e:
    print("****** ID와 이름이 일치하지 않습니다 *******")
    print(type(e))
    print(e)
   
finally :
    #오름 차순 정렬
    sql = "SELECT ID, Name FROM user ORDER BY ID"
    c.execute(sql)
    result = c.fetchall() 
    print(members)

    con.close()


mem = []
print("******* input start *******")
for i in range(0, 3):
     msg = f"{i+1}번째 ID, Name :"
     id, name = input(msg).split(',')
     mem.append({'ID':ID, 'Name':Name})

     print(mem)
print("***************","\n")

print("#*******sort start #**********")
sorted_list = sorted([dic['id'] for dic in mem])

print(sorted_list)
print("*****************************","\n")


print("********* print start *************")
for id in sorted_list:
     for original_ID in mem:
         if original_ID['id'] == id:
             print(f"{id}, {original_ID['name']}")
print("*********************************")

