import smtplib

sender_email = "secretsanta2020.510@gmail.com"
rec_email = "drojas@ucdavis.edu"
password = input(str("Please enter your passwor : " ))


server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender_email,password)
print("Success")
header = 'To:' + rec_email + '\n' + 'From: ' + sender_email + '\n' + 'Subject: Secret Santa!!! \n'
print (header)
msg = header + '\n this is test msg from Diego Rojas  \n\n'
server.sendmail(sender_email,rec_email, msg)
print("Email has been sent to ", rec_email)
server.quit()



