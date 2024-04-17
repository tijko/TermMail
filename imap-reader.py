#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import imaplib
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from google.auth.exceptions import RefreshError


def get_access_token(credential_file):
    creds = service_account.Credentials.from_service_account_file(
        credential_file, scopes=scopes)
    try:
        creds.refresh(Request())
        return creds.token
    except RefreshError as e:
        print("Error refreshing access token:", e)
        return None

def login_imap(username, access_token):
    try:
        # Establish IMAP connection
        imap_conn = imaplib.IMAP4_SSL('imap.gmail.com')
        imap_conn.authenticate('XOAUTH2', lambda x: 'user={}\1auth=Bearer {}\1\1'.format(username, access_token))
        return imap_conn
    except Exception as e:
        print("Error connecting to IMAP:", e)
        return None

if __name__ == "__main__":
    credential_file = 'imap_client_secret.json'
    scopes = ['https://mail.google.com/']
    username = "konick781@gmail.com"
    access_token = get_access_token(credential_file)
    print(access_token)
    sys.exit(0)
    if access_token:
        imap_conn = login_imap(username, access_token)
        if imap_conn:
            print("Successfully logged in!")
        else:
            print("Failed to establish IMAP connection.")
    else:
        print("Failed to obtain access token.")