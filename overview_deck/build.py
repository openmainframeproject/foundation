#!/usr/bin/env python3
#
# Copyright this project and it's contributors
# SPDX-License-Identifier: Apache-2.0
#
# encoding=utf8

from __future__ import print_function
import os.path
import requests

# The ID of a sample document.
documents = [
        {'id':'1Zk3REYGnE6mYIXl52QxzNbVW7XM2NPs_1w7YxscRXrk','mimeType':'application/pdf','filename':'open_mainframe_project_overview_deck.pdf'},
        {'id':'1Zk3REYGnE6mYIXl52QxzNbVW7XM2NPs_1w7YxscRXrk','mimeType':'application/vnd.openxmlformats-officedocument.presentationml.presentation','filename':'open_mainframe_project_overview_deck.pptx'},
        {'id':'1SW-JbXTQgwb_OczGeyo5jqc6GmK5CLmBTzg0pb0vMXs','mimeType':'application/pdf','filename':'Open Mainframe Project - Membership Overview.pdf'},
        ]

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
