#!/usr/bin/env python3
import ipaddress

#ipchk= '192.168.0.1'
ipchk=input('apply an ip: ')
try:
    ipaddress.ip_address(ipchk)
        if ipchk=='192.168.0.1':
        print('ip address was set:' + ipchk + 'this not reco')

    else ipchk:
        print('looks lik ip was set'+ipchk)
        

    #else:
     #   print('u did not put an input')
