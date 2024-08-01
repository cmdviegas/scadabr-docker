#!/bin/bash

# Start ModbusTCP server
nohup python /root/modbus-server.py &> /dev/null &

# Start TOMCAT
./tomcat/bin/catalina.sh run
