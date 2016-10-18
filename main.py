#!/usr/local/bin/python

import os
import argparse
import logging

from apiai_client import APIAIClient

token = {
    "developer": "APIAI_DEV_TOKEN",
    "client": "APIAI_CLIENT_TOKEN",
}


def parse_args():
    parser = argparse.ArgumentParser(description='I Talk and I Know Things.')
    parser.add_argument('-q', '--query',
                        dest='query', type=str,
                        default="",
                        help='Query for API.AI')
    parser.add_argument('-d', '--developer',
                        dest='developer', action='store_true',
                        help='Sets developer mode')

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    token_name = token["developer"] if args.developer else token["client"]
    token = os.getenv(token_name, None)
    if not token:
        logging.error("Environmental Variable Not Set: '%s'" % token_name)
        exit(1)

    client = APIAIClient(token)
    print client.run_query(args.query)



