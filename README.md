Domeneshop ddns runner
=====================

Domeneshop 3'rd party Python3 ddns updater.

**Check:** https://github.com/domeneshop/python-domeneshop for more info.

Installation
------------

```
pip3 install domeneshop
pip3 install IPy
cd ~
git clone https://github.com/magnue/domeneshop-ddns-runner.git
sudo mkdir -p /srv
sudo ln -s `pwd`/domeneshop-ddns-runner /srv/domeneshop
```

**Note:** You need to update the scripts
* ~/domeneshop-ddns-runner/*api_key.example*
* ~/domeneshop-ddns-runner/*domeneshop-ddns-runner.example*

**Remove** the .example extensions after editing, and then
```
sudo cp ~/domeneshop-ddns-runner/domeneshop-ddns-runner /etc/cron.d/
```

Credentials
-----------

Use of these scripts requires Domeneshop API credentials.

See the [Domeneshop API](https://api.domeneshop.no/docs) documentation for more information.

Examples
--------
The top level script *ddns_portal.py* uses the script *check_record.py* and *update_record.py*
to see if the public IP of the server maches the DNS record in your domeneshop account "*check_record.py*",
and if not updates the IP with "*update_record.py*".

The *ddns_portal.py* scrip takes the yourdomain.no and the 'DNS ID' number as parameters. 
You can manually use the *list_records.py* with parameter yourdomain.no to get the 'DNS ID' for your host.

Listst DNS entries for yourdomain.no with DNS ID number

``python3 /srv/domeneshop/list_records.py yourdomain.no``

Checks if the current public IP is same as DNS entry, and updates if necessary

``python3 /srv/domeneshop/ddns_portal.py yourdomain.no <DNS ID>``

If you want to check if a IP is assignet to your host, you can directly use the *check_record.py* script.

``python3 /srv/domeneshop/check_record.py yourdomain.no <DNS ID> <IP to compare>``

If you want to directly update the IP for a host, you can use the *update_record.py* script.

``python3 /srv/domeneshop/update_record.py yourdomain.no <DNS ID> <IP to set>``

Endnote
-------
Hope you enjoy these scripts :)
Use accordingly to LICENSE file
