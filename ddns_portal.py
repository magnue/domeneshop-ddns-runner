#!/usr/bin/env python3
"""Simple script that update the IP for the specified domain and DNS ID,
    if public IP does not match the dns entry at domeneshop.
    Usefull to keep dns for non static IP up to date (ddns).
    Parameters: ddns_portal.py yourdomainame.no dnsid
    Exits 0 if script runs without issues and there was an IP update,
    if else exits not 0.
    Use accordingly to LICENCE file"""

from requests import get
import sys
import subprocess

if __name__ == "__main__":

    public_ip = get('https://api.ipify.org').content.decode('utf8')

    if not len(sys.argv) == 3:
        exit("Wrong number of arguments for ddns_runner.py")

    srv_path = "/srv/domeneshop"
    exec_path = srv_path + "/check_record.py"
    ans = subprocess.call(['python3', exec_path, sys.argv[1], sys.argv[2], public_ip])

    if not ans == 0:
        exit("Exit code from " + exec_path + ": " + str(ans))

    exec_path = srv_path + "/update_record.py"
    ans = subprocess.call(['python3', exec_path, sys.argv[1], sys.argv[2], public_ip])

    if not ans == 0:
        exit("Exit code from " + exec_path + ": " + str(ans) + " see log output, dns update was attemptet, but failed")

    exit(0)
