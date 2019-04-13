import psycopg2
import json

conn = psycopg2.connect(database="fsc_database", user="postgres",host='127.0.0.1', password="test123",port=5432)
curr = conn.cursor()

eventR = open('ITFMock.json','r')
eventJs = json.load(eventR)

for lines in eventJs:
    lst = [None]*9
    lst[0] = lines['tournament_name']
    lst[1] = lines['host_nation']
    lst[2] = lines['host_nation'][:3]
    lst[3] = lines['start_date']
    lst[4] = lines['end_date']
    lst[5] = lines['surface']
    lst[6] = lines['grade']
    lst[7] = lines['link']
    lst[8] = lines['website']


    curr.execute("INSERT INTO tournaments_tournamentitf(tournament_name,host_nation,venue,start_date,end_date,surface,grade,link,website) VALUES (%s, %s,%s,%s, %s,%s,%s, %s,%s)",
    (lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8]))
    conn.commit()

print('ITF TO DB : CODE 200')

curr.close()
conn.close()