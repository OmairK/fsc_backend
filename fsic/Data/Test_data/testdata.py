import psycopg2
import json

conn = psycopg2.connect(database="mydatabase_phase1", user="postgres",host='127.0.0.1', password="test123",port=5432)
cur = conn.cursor()

playerR = open('playerRank.json','r')
playerJs = json.load(playerR)

for lines in playerJs:
    a = lines['name']
    b = lines['rank']
    c = lines['movement']
    d = lines['dob']
    e = lines['events']
    f = lines['points']
    cur.execute("INSERT INTO tournaments_playerrankingsms(name,rank,movement,dob,events,points) VALUES (%s, %s,%s,%s,%s,%s)",(a,b,c,d,e,f))
    cur.execute("INSERT INTO tournaments_playerrankingsmd(name,rank,movement,dob,events,points) VALUES (%s, %s,%s,%s,%s,%s)",(a,b,c,d,e,f))
    conn.commit()


tournaments = open('tournaments.json','r')
tornjs = json.load(tournaments)

for lines in tornjs:
    a = lines['name']
    b = lines['venue']
    c = lines['start_date']
    d = lines['end_date']
    e = lines['surface']
    f = lines['grade']
    g = lines['link']
    h = lines['website']



    cur.execute("INSERT INTO tournaments_tournamentitf(name,venue,start_date,end_date,surface,grade,link,website) VALUES (%s, %s,%s,%s, %s,%s,%s,%s)",(a,b,c,d,e,f,g,h))
    conn.commit()


cur.close()
conn.close()