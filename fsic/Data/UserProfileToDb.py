import psycopg2
import json

conn = psycopg2.connect(database="fsc_database", user="postgres",host='127.0.0.1', password="test123",port=5432)
curr = conn.cursor()

curr.execute("truncate table users_userprofile")
conn.commit()

playerR = open('UserProfileMock.json' , 'r')
playerJs = json.load(playerR)

for lines in playerJs:
    a,b,c,d,e,f,g,h,i,j,k,l = (None,)*12
    a = lines['backhand_style']
    b = lines['backhand_style'][:3]
    c = lines['achievements']
    e = lines['city']
    f = lines['name']
    g = lines['home_club']
    h = lines['date_of_birth']
    i = lines['profession']
    j = lines['user_email']
    k = lines['role_model']
    l = lines['profile_photo']
	
 
    # print(a,b,c,d,e,f,g,h,i,j,k,l)
    curr.execute("INSERT INTO users_userprofile(strong_hand,backhand_style,achievements,city,name,home_club,date_of_birth,profession,user_email,role_model,profile_photo) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(a,b,c,e,f,g,h,i,j,k,l))
    conn.commit()

print('User Profile To DB : CODE 200')

curr.close()
conn.close()
