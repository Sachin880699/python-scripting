import pandas as pd
import mysql.connector



mydb = mysql.connector.connect(user='db_user', password='sachin',
                              host='127.0.0.1',
                              database='user')




mycursor = mydb.cursor ( )






df = pd.read_csv('user.csv')

first_name = df['First Name']
last_name = df['Last Name']
email = df['Email Address']
phone = df['Phone Number']
company = df['Company']
hired_date = df['Date Hired']

'''print(first_name)
print(last_name)
print(phone)
print(company)
print(hired_date)'''
print(email)
for email in email:




  mycursor.execute(("""INSERT INTO data (email) VALUES ('%s')""" % (email)))

#mycursor.execute ('INSERT INTO data (email) VALUES %s (',email,');')








'''myresult = mycursor.fetchall ( )


for result in myresult:
  for data in result:
    print(data)'''
mydb.commit()
print('okkkkkk')
