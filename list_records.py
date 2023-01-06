#!/usr/bin/env python3
"""Simple script that lists the DNS records for the spesified domain
    Needs yourdomain.no as parameter
    Use according to LICENCE file"""

from domeneshop import Client
import sys

if __name__ == "__main__":

    token = ""
    secret = ""
    with open('/srv/domeneshop/api_key') as keyfile:
        token = keyfile.readline()
        secret = keyfile.readline()
    token = token[:-1]
    secret = secret[:-1]

    client = Client(token, secret)

    if not len(sys.argv) == 2:
        exit("Wrong number of arguments. Needs: 'yourdomain.no'")

    domains = client.get_domains()
    if not domains:
        exit("No domains found!")

    test = False
    selected_domain = {}
    for domain in domains:
        if domain["domain"] == sys.argv[1]:
            selected_domain = domain
            test = True
            print("DNS records for {0}:".format(domain["domain"]))

    for record in client.get_records(selected_domain["id"]):
        print(record["id"], record["host"], record["type"], record["data"])
