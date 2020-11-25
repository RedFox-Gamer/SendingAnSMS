#pip install twilio
from twilio.rest import Client

#Authentication. You can get your's from twilio.com/console
account_sid = 'Your SID here'
auth_token = 'Your Token here'

client = Client(account_sid, auth_token)

#"from_" is the number you created on twilio.com/console
#"body" is the text you want to send
#"to" is the number you registered with
client.messages.create(from_ = '+16672001342', body = "Text goes Here", to = "Your number")