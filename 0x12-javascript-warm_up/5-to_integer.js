#!/usr/bin/node

const { argv } = require('process');

const num = parseInt(argv[2]) / 1;
if (num) {
	console.log('My number is: ' + num);
} else {
	console.log('Not a number');
}

