#!/bin/bash
#This script list out alll  the suported methods of http
curl -sI -X OPTIONS $1 | grep "Allow:" | cut -d " " -f 2-
