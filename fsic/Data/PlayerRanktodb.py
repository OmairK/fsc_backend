import psycopg2
import json

conn = psycopg2.connect(database="mydatabase_phase1", user="postgres",host='127.0.0.1', password="test123",port=5432)
curr = conn.cursor()



playerR = open('PlayerRanks.json' , 'r')
playerJs = json.load(playerR)

for lines in playerJs:
    a = lines['Rank']
    b = lines['Player']
    c = lines['Movement']
    e = lines['DOB']
    f = lines['Events']
    g = lines['Points']
    h = lines['Age Group']
    d = lines['Type'] 
    curr.execute("INSERT INTO tournaments_playerrankingsms(name,rank,movement,dob,events,points,agegroup,category) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",(b,a,c,e,f,g,h,d))
    conn.commit()

print('Player Rank To DB : CODE 200')

curr.close()
conn.close()