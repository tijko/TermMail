#!/usr/bin/env python
# -*- coding: utf-8 -*-

from imaplib import IMAP4_SSL
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


def authenticate():
    # Set up the OAuth2 flow
    flow = InstalledAppFlow.from_client_secrets_file(
        'imap_client_secret.json', SCOPES)
    credentials = flow.run_local_server(port=0)
    return credentials

def main():
    # Authenticate and get credentials
    credentials = authenticate()
    # Connect to the IMAP server
    imap_server = IMAP4_SSL('imap.gmail.com')
    imap_server.authenticate('XOAUTH2', lambda x: credentials.token)
    imap_server.select('inbox')  # Select the mailbox you want to access
    # Fetch emails or perform other operations
     typ, mail = imap_server.search(None, 'ALL')
     print(mail)
    imap_server.close()
    imap_server.logout()

if __name__ == "__main__":
    # Define OAuth2 scopes for IMAP
    SCOPES = ['https://mail.google.com/']
    main()