#!/usr/bin/python
import sys, getopt, os,argparse
import requests
import re
import logging

def Execute(mode):
    logging.debug('start execute')
    influxURL = 'http://localhost:8086/'
    db = 'appinstall'
    dataString = 'TIME=5/8/2020 18:28:12,FILENAME=nexus_cft2.zip'
    influxDB = influxURL + 'write?db=' + db
    
    response = requests.post(influxDB, dataString)
    
    logging.info("        > WriteInflux: influxDB : " + tableName + ":"+ influxDB)
    logging.info("        > WriteInflux: dataString : " + tableName + ":"+ dataString)
    
    if response.status_code == 400:
        logging.info("        > WriteInflux: Error: 400: Bad Request (" + tableName +"," + db +")")
    elif response.status_code == 404:
        logging.info("        > WriteInflux: Error: 404: Not Found(" + tableName +"," + db + ")")
    elif response.status_code == 200:
        logging.info("        > WriteInflux: 200: OK")
    elif response.status_code == 204:
        logging.info("        > WriteInflux: 204 : OK (No Content)(" + tableName +"," + db + ")")
    else:
        logging.info("        > WriteInflux: " + response.status_code + "(" + tableName +"," + db + ")")



def main(argv):
    FORMAT = "%(asctime)-15s %(message)s"
    logging.basicConfig(level=logging.DEBUG,format=FORMAT)
    
    parser = argparse.ArgumentParser(description='Grafana monitor service',
                                     usage='./monitor.py')
    parser.add_argument('-m', '--Mode', type=str, nargs='?', help='Mode [s:service, t:test-mode]', required=True)
    
    args = parser.parse_args()
    Execute(Mode = args.Mode)

if __name__ == "__main__":
    main(sys.argv[1:])

# !-------- logging levels --------! #
#DEBUG
#INFO
#WARNING
#ERROR
#CRITICAL