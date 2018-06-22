#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" stripe_donor_logger.cgi

This scripts is to be run as a cgi on a public server.
By creating a webhook at stripe for the payments to qgis/QGIS this
script will be called, with the commit data as json (sent by striep).

Given this data the script will do the following:
- load the json and extract donationid, donorname and donordate
- log success and errors to /tmp/stripehook.log
- call the QGIS-Website/scripts/commit_donor.sh with the donorname as 1st arg
- that script will:
    - git pull --rebase the QGIS-Website source
    - call the perl script which adds the donorname to the donors.inc file
    - and commit this to github

There is a special linux user created for this: stripe@qgis2.

"""

import sys
import os
import io
import json
import time
from subprocess import Popen, PIPE


def log(msg):
    with open('/tmp/stripehook.log', 'a', encoding="utf-8") as f:
        f.write('{}\n'.format(msg))

def test():
    charge_success = '''{
      "object": {
        "id": "ch_1CUyLrBBMqjyXePiy9wBoSW1",
        "object": "charge",
        "amount": 200,
        "amount_refunded": 0,
        "application": null,
        "application_fee": null,
        "balance_transaction": "txn_1CUx4ewrr3DBBMqjyXePig0uuohxp",
        "captured": true,
        "created": 1527082306,
        "currency": "eur",
        "customer": "cus_Cumd7sadfdegPGPUoVU",
        "description": "QGIS Donation",
        "destination": null,
        "dispute": null,
        "failure_code": null,
        "failure_message": null,
        "fraud_details": {
        },
        "invoice": null,
        "livemode": true,
        "metadata": {
          "email": "richard@duif.net",
          "donorname": "אבלין李 克勤"
        },
        "on_behalf_of": null,
        "order": null,
        "outcome": {
          "network_status": "approved_by_network",
          "reason": null,
          "risk_level": "normal",
          "seller_message": "Payment complete.",
          "type": "authorized"
        },
        "paid": true,
        "receipt_email": null,
        "receipt_number": null,
        "refunded": false,
        "refunds": {
          "object": "list",
          "data": [
          ],
          "has_more": false,
          "total_count": 0,
          "url": "/v1/charges/ch_1CUx4dafaeeafABBMqjyXePi7Lu5EhcI/refunds"
        },
        "review": null,
        "shipping": null,
        "source": {
          "id": "card_1CUx3tBBMqjydafdXePiM6yo4onz",
          "object": "card",
          "address_city": null,
          "address_country": null,
          "address_line1": null,
          "address_line1_check": null,
          "address_line2": null,
          "address_state": null,
          "address_zip": null,
          "address_zip_check": null,
          "brand": "Visa",
          "country": "NL",
          "customer": "cus_Cumddfa7sgPGPUoVU",
          "cvc_check": "pass",
          "dynamic_last4": null,
          "exp_month": 12,
          "exp_year": 1920,
          "fingerprint": "MzssdxRNkG8GPuXIaP2",
          "funding": "credit",
          "last4": "4242",
          "metadata": {
          },
          "name": null,
          "tokenization_method": null
        },
        "source_transfer": null,
        "statement_descriptor": null,
        "status": "succeeded",
        "transfer_group": null
      },
      "previous_attributes": null
    }'''
    return charge_success

def sent_content(status, msg):
    # http://www.restpatterns.org/HTTP_Status_Codes
    print('Status: {}'.format(status))
    print('Content-Type: text/plain')
    print('')
    print('{}'.format(msg))


# THE ACTUAL CGI

# TO TEST: make method GET and take one of the jsons from test()
method = os.environ["REQUEST_METHOD"]

# TODO: check the 'secret' == if the Stripe-Signature contains our SECRET
SECRET='****'

try:
    # TO TEST: make method GET and take one of the jsons from test()
    if method == "GET":
        rawdata = test()
    elif method == "POST":
        # duh, sys.stdin.read guesses the encoding... and in case of french guesses ascii: wrong!
        # https://stackoverflow.com/questions/16549332/python-3-how-to-specify-stdin-encoding
        # so instead of reading directly from sys.stdin we read via iowrapper:
        #rawdata = sys.stdin.read()
        input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
        rawdata = input_stream.read()
    else:
        sent_content(400, 'Illegal request')
        sys.exit(400)

    log(rawdata) # don't think we should log this....
    data = json.loads(rawdata)
    # sometimes not only the charge object is sent, but also the evt object surrounding it:
    if data['object']=='event':
        log('event received instead of charge...')
        data = data['data']
    donationid = data['object']['id']
    donationtime = time.asctime(time.gmtime(data['object']['created']))
    donorname = data['object']['metadata']['donorname']
    if donorname is None or len(donorname)<1:
        # we promissed to only publish the donorname if it was given!
        pass
    else:
        # casting to Title case
        donorname = donorname.title()
        # have to sent bytes utf-8 encoded to command??
        #command = ['scripts/commit_donor.sh', donorname]
        command = ['scripts/commit_donor.sh', bytes(donorname, 'utf-8')]
        cwd = '/home/stripe/QGIS-Website'
        result = Popen(command, cwd=cwd, stdout=PIPE, stderr=PIPE)
        (status, error) = result.communicate()
        if result.poll() == 0:
            log('Succesfully add+commit of donation {} dd {} (UTC) by "{}" see https://dashboard.stripe.com/payments/{}'.format(donationid, donationtime, donorname, donationid))
        else:
            log('ERROR add+commit of donation {} dd {} (UTC) by "{}" see https://dashboard.stripe.com/payments/{}'.format(donationid, donationtime, donorname, donationid))
            log(error)
            sent_content(500, 'Some unexpected error occurred. Error text was: {}'.format(error))
            sys.exit(500)

    # all fine: sent 200 back to Stripe
    sent_content(200, 'Ok')

except Exception as error:
    log('ERROR in script: {}'.format(error))
    sent_content(500, 'Some unexpected error occurred. Error text was: {}'.format(error))
    sys.exit(500)
