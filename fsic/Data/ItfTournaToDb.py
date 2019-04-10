import psycopg2

f = open("ITF_tournaments.txt","r")
# m = open("Test.txt","w")

months  = {'January': '01' ,'February':'02','March':'03','April':'04','May':'05','June':'06','July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}
def month_to_int(mon):
    for k in months:
        if k == mon:
            mon  = months[k]
            return mon


conn = psycopg2.connect(database="fsc_database", user="postgres",host='127.0.0.1', password="test123",port=5432)
cur = conn.cursor()
for lines in f:
    lst = [None]*9
    for index in range(9):

        a = f.readline()
        # print(a)
        if a!='\n':
            if a.startswith('N'):
                # print(a)
                b=a.split(':')
                c=b[1].rstrip('\n')
                lst[0]=c
            elif a.startswith('H'):
                # print(a)
                b=a.split(':')
                c=b[1].rstrip('\n')
                lst[1]=c
            elif a.startswith('D'):
                # print(a)
                b=a.split(':')
                c=b[1].rstrip('\n')
                startDate,endDate = c.split("-")
                startDateDay,startDateMonth = startDate.split() ### different date formats for use in the flutter app
                endDateDay,endDateMonth,Year = endDate.split()
                STM = month_to_int('{}'.format(startDateMonth))
                ETM = month_to_int('{}'.format(endDateMonth))
                startDateInt = Year + STM + startDateDay
                endDateInt = Year + ETM + endDateDay    
                lst[2]=startDateInt
                lst[3]=endDateInt
            elif a.startswith('C'):
                # print(a)
                b=a.split(':')
                c=b[1].rstrip('\n')
                lst[4]=c
            elif a.startswith('S'):
                # print(a)
                b=a.split(':')
                c=b[1].rstrip('\n')
                lst[5]=c
            elif a.startswith('V'):
                # print(a)
                b=a.split(':')
                c=b[1].rstrip('\n')
                lst[6]=c
            elif a.startswith('u'):
                # print(a)
                b=a.split('l :')
                c=b[1].rstrip('\n')
                lst[8]=c
            elif a.startswith('W'):
                # print(a)
                b=a.split('e:')
                c=b[1].rstrip('\n')
                lst[7]=c
            else:
                print('Error '+ a)

            # print('new line')
        else:
            # print('++++++++')
            d=f.readline()
            # print(d)
            break

    cur.execute("INSERT INTO tournaments_tournamentitf(name,host_nation,grade,start_date,end_date,surface,venue,website,link) VALUES (%s, %s,%s,%s, %s,%s,%s, %s,%s)",(lst[0],lst[1],lst[4],lst[2],lst[3],lst[5],lst[6],lst[7],lst[8]))
    conn.commit()
    # print(lst)
    # m.write("{} \n".format(lst))

        


# m.close()
cur.execute("SELECT * FROM tournaments_tournamentitf;")

cur.fetchone()
conn.commit()
cur.close()
conn.close()
