#!/usr/bin/env python3
"""Simple script that checks the IP address for the specified domain and DNS ID.
    Usefull to check for change in global IP address for non static IP's.
    If the script runs without issues, but the IP on the dns entry does
    not match the public IP, it must be updated. In that case the
    script will return 0, if the check fails, or the IP is up to date,
    it wil return not 0.
    Parameters: list_record.py yourdomainame.no dnsid publicip
    Use accordingly to LICENCE file"""

import sys
from domeneshop import Client
from IPy import IP


if __name__ == "__main__":

    token = ""
    secret = ""
    with open('/srv/domeneshop/api_key') as keyfile:
        token = keyfile.readline()
        secret = keyfile.readline()
    token = token[:-1]
    secret = secret[:-1]

    client = Client(token, secret)

    if not len(sys.argv) == 4:
        exit("Wrong number of arguments. Needs: 'yourdomainname.no', 'DNS ID' and 'public IP'")

    domains = client.get_domains()
    if not domains:
        exit("No domains found!")

    test = False
    domain_id = 0
    for domain in domains:
        if sys.argv[1] == format(domain["domain"]):
            test = True
            domain_id = domain["id"]

    if not test:
        exit("Domainame specified does not exist")

    test = True
    record_id = 0
    try:
        record_id = int(sys.argv[2])
    except ValueError:
        test = False

    if not test:
        exit("DNS id argument is not a number: " + sys.argv[2])

    test = True
    try:
        IP(sys.argv[3])
    except ValueError:
        test = False

    if not test:
        exit("IP argument is not a IP: " + sys.argv[3])

    test = False
    check_dns = {}
    for record in client.get_records(domain_id):
        if record_id == record["id"]:
            test = True
            if not ((record["type"] == "A") | (record["type"] == "AAA")):
                exit("DNS type is not A or AAA, aborting! Type is: " + record["type"])
            else:
                check_dns = record

    if not test:
        exit("DNS ID not found {0}".format(record_id))

    if check_dns['data'] == str(sys.argv[3]):
        exit("The script ran normally but the IP address does not need to be updated. IP is: " + check_dns["data"])

    exit(0)
