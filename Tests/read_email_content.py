from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient import errors
import user_credentials as user

service = 'https://accounts.google.com/o/oauth2/auth'
user_id = user.user_email_method()
label_ids = 'UNREAD'
messageBody = None

def login():
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    creds = None
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)
    return creds

    #  Call the Gmail API
def test_getUnreadMsgID():
    creds = login()
    service = build('gmail', 'v1', credentials=creds)
    try:
        unreadMesages = service.users().messages().list(userId=user_id,
                                                labelIds=label_ids, maxResults=1).execute()
        messageID =unreadMesages['messages'][0]['id']
        if messageID != 0:
            return messageID
        else:
            print('UNSUCCEES!!')
    except errors.HttpError as error:
        print (f'An error occurred: %s' % error)
        return None

def getMsgValue():
    creds = login()
    messageID = test_getUnreadMsgID()
    service = build('gmail', 'v1', credentials=creds)
    try:
        
        message = service.users().messages().get(userId=user_id, id=messageID, format='metadata', metadataHeaders='From').execute()
        if message['payload']['headers'][0]['value'] == "notify@bot.dozorro.org":
            messageBody = message['snippet']
            return messageBody
        else:
            print('UNSUCCEES!!')
    except errors.HttpError as error:
        print (f'An error occurred: %s' % error)
        return None

# if __name__ == '__main__':
#     Gmail_API().getMsgValue()