#DB 연동 파이썬에서 로그인 기능 구현






import pymysql #py mysql 패키지 

conn=pymysql.connect(host ='localhost', user = 'root', password='25722357', db='2client', charset='utf8')
cursor = conn.cursor()


#로그인 실패 횟수
cnt = 0

try :
    while True:

        #ID, PW 입력받기
        id = input('ID 입력:')
        pw = input('PW 입력:')

        #DB ID 확인
        sql = "SELECT EXISTS (SELECT * FROM clientinfo WHERE id = %s) AS SUCCESS"
        cursor.execute(sql, (id))
        result = cursor.fetchone() 
            
        if result[0] == 1:
            
            #DB의 (ID, PW) input값 비교
            sql ="SELECT id, pw FROM clientinfo WHERE id = %s"
            cursor.execute(sql, (id))
            result = cursor.fetchone()
            if result [0] == id and result[1] ==pw:   
                print('\n로그인 성공!')
                break            
            else :
                cnt += 1
                print("******** 로그인 3회 실패 시 자동 종료됩니다 ********")
                print(f'로그인 {cnt}회 실패')
                print("****************************************************","\n")
            
            if cnt >= 3:

                print("보안을 위해 로그인 시스템을 종료합니다!")
                break

        else:
            print("\n##################################")
            print("ID가 존재하지 않습니다!!")
            print("##################################","\n")
            
            # Mini 회원가입 기능
            ans = input("아이디를 만드시겠습니까? [y/n]:")
            while True:
                if ans == 'y':
                    tmp1 = input("I D: >>>")
                    tmp2 = input("PWD: >>>")

                # DB(ID,PWD)에 실수로 공백이 들어가는 것을 방지
                if tmp1 == ' ' :
                        print("\n만드실 ID를 입력하지 않았습니다.")
                        print("다시 입력해주세요!")
                        continue
                if tmp2 == ' ' :
                        print("\n만드실 Password를 입력하지 않았습니다.")
                        print("다시 입력해주세요!")
                        continue
                    
                # DB에 넣어주기
                sql = "INSERT INTO clientinfo(id,pw) VALUES(%s, %s)"
                cursor.execute(sql, (tmp1, tmp2))
                conn.commit()

                # 제대로 들어갔는지 확인
                sql = "SELECT * FROM clientinfo WHERE id = %s"
                cursor.execute(sql, tmp1)
                check_DB = cursor.fetchone()
                print("######################################")
                print(f"ID:{check_DB[1]}, PWD:{check_DB[2]}\n")
                print("회원가입이 정상적으로 완료되었습니다!")
                print("######################################\n")
                break
                
            else:
                print("\n시스템을 종료합니다!")
                    
                    # 이중 LOOP를 탈출하기 위해서 일부러 에러 만들기
                    # raise NotImplementedError
                    

except NotImplementedError as e:
    print("----------------------------------")
    print("시스템 종료...")
    print("----------------------------------")

except Exception as e:
    print("############ 에러발생 ############")
    print(type(e))
    print(e)
    print("##################################")

finally:
    conn.close()