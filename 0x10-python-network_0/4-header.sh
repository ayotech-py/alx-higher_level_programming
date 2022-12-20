#!/bin/bash
#This scripts takes in a url as an arg and sends a get request to it
curl -sd "{'X-School-User-Id': 98}" $1
