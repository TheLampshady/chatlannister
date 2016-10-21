#!/usr/local/bin/python

import os
import argparse
import logging

from apiai_client import APIAIClient

token = {
    "developer": "APIAI_DEV_TOKEN",
    "client": "APIAI_CLIENT_TOKEN",
}

def socialize(client):
    chat = raw_input("%s: " % client.speech)
    if not chat:
        print "Don't be shy! Say something."
        return True

    client.run_query(chat)
    if client.action == 'quit':
        print client.speech or "Ciao"
        return False

    return True

def parse_args():
    parser = argparse.ArgumentParser(description='I Talk and I Know Things.')
    parser.add_argument('-d', '--developer',
                        dest='developer', action='store_true',
                        help='Sets developer mode')

    return parser.parse_args()

def run_thyself(client):
    try:
        return socialize(client)
    except KeyboardInterrupt as ki:
        print "\nNice chatting with you!\nExiting..."
        return False


if __name__ == "__main__":
    args = parse_args()
    token_name = token["developer"] if args.developer else token["client"]
    token = os.getenv(token_name, None)

    if not token:
        logging.error("Environmental Variable Not Set: '%s'" % token_name)
        exit(1)

    client = APIAIClient(token)

    print "Hello I am Chation Lannister",

    while run_thyself(client):
        pass

    exit(0)

