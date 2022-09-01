#!/usr/bin/env python3
#
# Copyright this project and it's contributors
# SPDX-License-Identifier: Apache-2.0
#
# encoding=utf8

from __future__ import print_function
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import requests

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# The ID of a sample document.
documents = [
        {'id':'1Zk3REYGnE6mYIXl52QxzNbVW7XM2NPs_1w7YxscRXrk','mimeType':'application/pdf','filename':'open_mainframe_project_overview_deck.pdf'},
        {'id':'1Zk3REYGnE6mYIXl52QxzNbVW7XM2NPs_1w7YxscRXrk','mimeType':'application/vnd.openxmlformats-officedocument.presentationml.presentation','filename':'open_mainframe_project_overview_deck.pptx'},
        {'id':'1KaPgj8AKudkfS7t2TvOxvwWpOb5uu-GP3YwA14su_vY','mimeType':'application/pdf','filename':'open_mainframe_project_host_project.pdf'},
        {'id':'1KaPgj8AKudkfS7t2TvOxvwWpOb5uu-GP3YwA14su_vY','mimeType':'application/vnd.openxmlformats-officedocument.presentationml.presentation','filename':'open_mainframe_project_host_project.pptx'},
        {'id':'1SW-JbXTQgwb_OczGeyo5jqc6GmK5CLmBTzg0pb0vMXs','mimeType':'application/pdf','filename':'Open Mainframe Project - Membership Overview.pdf'},
        ]

creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

# Retrieve the documents contents from the Docs service.
for document in documents:
    print("Getting file {}...".format(document['filename']))
    try:
        match document['mimeType']:
            case 'application/pdf':
                exportFormat = 'pdf'
            case 'application/vnd.openxmlformats-officedocument.presentationml.presentation':
                exportFormat = 'pptx'
            case _:
                continue
        contents = requests.get('https://docs.google.com/feeds/download/presentations/Export?id={docid}&exportFormat={exportFormat}'.format(docid=document['id'],exportFormat=exportFormat),stream=False)
        with open(document['filename'], 'wb') as f:
            f.write(contents.content)
    except HttpError as err:
        print(err.content)
