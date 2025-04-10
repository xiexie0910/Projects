import smtplib 
 
my_email = ''
password = ''

connection = smtplib.SMTP('smtp.gmail.com') 

connection.starttls() # encrypts the email that we sending

connection.login(user=my_email,password=password)

connection.sendmail(from_addr=my_email,to_addr='',msg='Hello my name is alex')

connection.close()
