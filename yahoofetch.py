#!/usr/bin/env python

import json
import urllib2

def testyahoo():

    call='http://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json'
    req=urllib2.Request(call)
    response=urllib2.urlopen(req)    
    json_object = json.load(response)

    olist=[]
    for each_resource in json_object['list']['resources']:
        olist.append(each_resource['resource']['fields']['name'])
    
    return olist

def main():
    
    resource_list=testyahoo()
    for each in resource_list:
        print each
        
    
if __name__=='__main__': main()