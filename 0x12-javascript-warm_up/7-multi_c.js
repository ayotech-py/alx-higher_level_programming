#!/usr/bin/node

const { argv } = require('process');
const num = parseInt(argv[2]);

if (Number.isInteger(num)) {
	for (let a = 0; a < num; a++) {
		console.log('C is fun');
	}
} else {
	console.log('Missing number of occurrences');
}
