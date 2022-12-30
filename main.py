import yagmail
import os
import pandas


sender = 'mmmm@gmail.com'
receiver = 'nnn@gmail.com'

subject = 'This is the subject'

yag = yagmail.SMTP(user=sender, password=os.getenv("PASSWORD"))
# # First select Tools/Secrets; Give name to the key, then go to your gmail and apply apps password
# # Uses getenv to prevent the vialization of password from other users.

df = pandas.read_csv('contacts.csv')
# print(df)

for index, row in df.iterrows():
  content = f"Hello, {row['name']}, Here is the content of the email"

  yag.send(to=row['email'], subject=subject, contents=content)
  print('Email is sent')
