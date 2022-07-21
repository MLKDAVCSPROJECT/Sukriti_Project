import mysql.connector as sql
import math,random
conn=sql.connect(host='localhost',user='root',passwd='1234',database='project')
c1=conn.cursor()

if conn.is_connected():
            print('### SS THEATRE BOOKING (AC & NON AC)###')
            print('Sign Up Complete')
            print('Log In Complete')
            
            query =input('Enter the query:')
            if query=='book ticket':
                print('Enter your theatre choice as 1,2,3 and 4')
                def v_id():
                    digits="1234567890"
                    id=""
                    for i in range(6):
                        id += digits[math.floor(random.random()*10)]

                    return id
                print('Your UserId is:',v_id())

                ch=int(input('Enter your Theatre choice:'))
                if ch==1:
                      vp_id = int(input('Enter your User Id:'))
                      v_mname = input('Enter the movie name:')
                      v_tic = int(input('Enter total tickets:'))
                      v_name = input('Enter your name:')
                      v_seat = input('Preferred seating(front,middle,back):')
                      v_ins = "insert into theatre1(vp_id,v_mname,v_tic,v_name,v_seat) values({},'{}',{},'{}','{}')".format(vp_id,v_mname,v_tic,v_name,v_seat)
                      c1.execute(v_ins)
                      conn.commit()
                      print('Tickets booked!!!')
                      print('Thank you for visiting our theatre')
                      print('     ENJOY YOUR MOVIE!!! HAVE FUN!!!    ')

                          
                elif ch==2:
                      print('WELCOME TO BOX OFFICE (AC)')
                      vp_id = int(input('Enter your User Id:'))
                      v_mname = input('Enter the movie name:')
                      v_tic =int(input('Enter total tickets:'))
                      v_name = input('Enter your name:')
                      v_seat = input('Preferred seating(front,middle,back):')
                      v_ins = "insert into theatre2(vp_id,v_mname,v_tic,v_name,v_seat) values({},'{}',{},'{}','{}')".format(vp_id,v_mname,v_tic,v_name,v_seat)
                      c1.execute(v_ins)
                      conn.commit()
                      print('Tickets booked!!!')
                      print('Thank you for visiting our theatre')
                      print('     ENJOY YOUR MOVIE!!! HAVE FUN!!!    ')
                     
                      
                elif ch==3:
                      print('WELCOME TO 1ST CLASS BOOKING')
                      vp_id = int(input('Enter your User Id:'))
                      v_mname = input('Enter the movie name:')
                      v_tic =int(input('Enter total tickets:'))
                      v_name = input('Enter your name:')
                      v_seat = input('Preferred seating(front,middle,back):')
                      v_ins = "insert into theatre3(vp_id,v_mname,v_tic,v_name,v_seat) values({},'{}',{},'{}','{}')".format(vp_id,v_mname,v_tic,v_name,v_seat)
                      c1.execute(v_ins)
                      conn.commit()
                      print('Tickets booked!!!')
                      print('Thank you for visiting our theatre')
                      print('     ENJOY YOUR MOVIE!!! HAVE FUN!!!    ')
                      
                      
                elif ch==4:
                      print('WELCOME TO 2ND CLASS BOOKING')
                      vp_id = int(input('Enter your User Id:'))
                      v_mname = input('Enter the movie name:')
                      v_tic =int(input('Enter total tickets:'))
                      v_name = input('Enter your name:')
                      v_seat = input('Preferred seating(front,middle,back):')
                      v_ins = "insert into theatre4(vp_id,v_mname,v_tic,v_name,v_seat) values({},'{}',{},'{}','{}')".format(vp_id,v_mname,v_tic,v_name,v_seat)
                      c1.execute(v_ins)
                      conn.commit()
                      print('Tickets booked!!!')
                      print('Thank you for visiting our theatre')
                      print('     ENJOY YOUR MOVIE!!! HAVE FUN!!!    ')

                      
                else:
                     print('Given theatre does not exist')              
            
                
                    
            elif query=='cancel ticket':
                name=input('Enter your name:')
                v=int(input('Enter the theatre choosed:'))
                if v==1:
                    a=int(input('Enter your User Id:'))
                    v_ins="delete from theatre1 where vp_id={}".format(a)
                    c1.execute(v_ins)
                    conn.commit()
                    print('Your tickets are cancelled successfully')
                elif v==2:
                    a=int(input('Enter your User Id:'))
                    v_ins="delete from theatre2 where vp_id={}".format(a)
                    c1.execute(v_ins)
                    conn.commit()
                    print('Your tickets are cancelled successfully')
                elif v==3:
                    a=int(input('Enter your User Id:'))
                    v_ins="delete from theatre3 where vp_id={}".format(a)
                    c1.execute(v_ins)
                    conn.commit()
                    print('Your tickets are cancelled successfully')
                elif v==4:
                    a=int(input('Enter your User Id:'))
                    v_ins="delete from theatre4 where vp_id={}".format(a)
                    c1.execute(v_ins)
                    conn.commit()
                    print('Your tickets are cancelled successfully')
                else:
                    print('Given theatre does not exist')
                
                

            else:
                print('INVALID INPUT')

         
                
