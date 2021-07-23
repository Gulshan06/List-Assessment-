import smtplib
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login("gulshan062132@gmail.com","Gullu@2132")
message="hello everyone"
connection.sendmail("gulshan062132@gmail.com","chedivya1998@gmail.com",message)
connection.quit()