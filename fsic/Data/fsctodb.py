import psycopg2
import json

conn = psycopg2.connect(database="fsc_database", user="postgres",host='127.0.0.1', password="test123",port=5432)
curr = conn.cursor()

curr.execute("truncate table tournaments_tournamentfsc")
conn.commit()
playerR = open('FSCMock.json','r')
playerJs = json.load(playerR)

for lines in playerJs:
    a = lines['coordinator_name']
    b = lines['age_group']
    c = lines['tournament_venue']
    d = lines['date']
    e = lines['tournament_description']
    f = lines['coordinator_name']
    g = lines['coordinator_contact_number']
    h = lines['coordinator_email']
    i = lines['event_location_url']
    curr.execute("INSERT INTO tournaments_tournamentfsc(tournament_name,age_group,tournament_venue,date,tournament_description,coordinator_name,coordinator_contact_number,coordinator_email,event_location_url) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(a,b,c,d,e,f,g,h,i))
    conn.commit()

print('FSC TO DB : CODE 200')

curr.close()
conn.close()
