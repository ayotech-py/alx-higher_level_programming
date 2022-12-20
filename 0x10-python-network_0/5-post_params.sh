#!/bin/bash
#This script takes in a url as a arg and sends a post request
curl -sX POST -d 'email=test@gmail.com&subject:I' $1
