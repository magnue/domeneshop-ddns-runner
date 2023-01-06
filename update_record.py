#!/usr/bin/env python3
"""Simple script that updates the named DNS records with the given IP.
    Parameters: update_record.py domainname.no dnsid ip
    List necessary parameters with list_record.py and use them here
    Some parameter validation is implemented
    Use according to LICENSE file"""


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
        exit("Wrong number of arguments. Needs: 'yourdomainname.no', 'DNS ID' and 'new IP'")

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
    updatedns = {}
    for record in client.get_records(domain_id):
        if record_id == record["id"]:
            test = True
            if ((record["type"] != "A") & (record["type"] != "AAA")):
                exit("DNS type is not A or AAA, aborting! Type is: " + record["type"])
            else:
                updatedns = record
                print("Updating: ", record["id"], record["host"], record["type"], "With IP: ", record["data"], " to IP: ", str(sys.argv[3]))

    if not test:
        exit("DNS ID not found {0}".format(record_id))

    updatedns["data"] = str(sys.argv[3])
    del updatedns["id"]

    client.modify_record(domain_id, record_id, updatedns)

    newrecord = client.get_record(domain_id, record_id)
    if not newrecord:
        exit("Could not get new record after update")

    print("Update success! New record is: ", record_id, newrecord["host"], newrecord["type"], newrecord["data"])
    exit(0)
