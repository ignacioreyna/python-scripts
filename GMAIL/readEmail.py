from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from os import environ
import datetime
import requests
import re

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

GMAIL_DIR = environ['HOME'] + '/GMAIL'
TODAY = datetime.datetime.today().date()
FILTER = 'from:mensajes.visahome@visa.com.ar after:{} subject:Nuevos consumos de sus tarjetas Visa'.format(TODAY)

def get_daily_expenses():

    daily_expenses=list()
   
    store = file.Storage(GMAIL_DIR + '/token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(GMAIL_DIR + '/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    results = service.users().messages().list(userId='me',labelIds = ['INBOX'], q=FILTER).execute()
    messages = results.get('messages', [])

    if not messages:
        print ("No messages found.")
    else:
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()['snippet']
            
            store = re.findall('establecimiento (.*) por', msg)[0]
            amount = re.findall('por (.*) ,', msg)[0].replace('.', ',')
            
            daily_expenses.append((store, amount))
    
    return daily_expenses

def notify(daily_expenses):
    if(daily_expenses):
        bot = environ["BOT_TOKEN"]
        chat_id = "CHAT_ID"
        text = build_string(daily_expenses)
        url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&parse_mode=HTML&text={}".format(
            bot, chat_id, text
        )
        r = requests.get(url)
        pass

def build_string(daily_expenses):
    text = 'Tus consumos de hoy fueron: \n\n'
    for t in daily_expenses:
        store = t[0]
        amount = t[1]
        #Remove URLs in message. PAYU sends store as query string in the URL
        text = text + '<b>· </b>'+ re.findall('(.*)\.', store.replace('PAYU.COM.AR/', ''))[0] + ': ' + amount + '\n'
    return text + '\n<b>No te excedas!</b>'

def main():
    notify(get_daily_expenses())

if __name__ == '__main__':
    main()