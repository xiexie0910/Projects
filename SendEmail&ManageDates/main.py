import smtplib 
 
my_email = 'alexxienz02@gmail.com'
password = ''

connection = smtplib.SMTP('smtp.gmail.com') 

connection.starttls() # encrypts the email that we sending

connection.login(user=my_email,password=password)

connection.sendmail(from_addr=my_email,to_addr='zxie089@aucklanduni.ac.nz',msg='Hello my name is alex')

connection.close()
