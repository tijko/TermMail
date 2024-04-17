#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import imaplib
from typing import List, Any

# mail_session.print_log()
# mail_session.ssl_context -> context_manager
# mail_session.debug -> int

# mail_session._check_bye
# mail_session._cmd_log

# mail_session.capabilities -> tuple
# mail_session.host -> str
# mail_session.capability() -> tuple(str, list)

# mail_session.select('InBox')
# mail_session.search('UnRead')

class TerminalMail():

    def __init__(self, usr: str, passwd: str) -> None:
        self.username = usr
        self.password = passwd
        self.session = self.create_session()
        if not self.session:
            print('Error: TerminalMail Failed to create mail session')
            sys.exit(-1)

    def create_session(self, port:int=993) -> imaplib.IMAP4_SSL:
        mail_session = imaplib.IMAP4_SSL('imap-mail.outlook.com', port)
        access = mail_session.login(self.username, self.password)
        if not access[0] == 'OK':
            return None
        return mail_session
        
    def trash_removal(self) -> List:
        trash = []
        try:
            trash = self.session.expunge()
            # cleanse data.... 
        except imaplib.IMAP4.error:
            # log?
            print('Error: TerminalMail Failed to clean trash')
        return trash 

    def get_mail(self) -> List[str]:
        self.session.select('inbox') # Use others...
        res, msg_ids = self.session.uid('search', None, '(UNSEEN)')
        # XXX error-handle
        messages = list()
        for msg_id in msg_ids[0].split():
            res, msg = self.session.uid('fetch', msg_id, '(RFC822)')
            if not res == 'OK':
                # log?
                print('Message {} Failed!'.format(msg_id))
            else:
                messages.append(msg)
        return ['None']

if __name__ == '__main__':
    email_address = sys.argv[1]
    password = sys.argv[2]
    terminal_mail = TerminalMail(email_address, password)
    #print(terminal_mail.retr) 