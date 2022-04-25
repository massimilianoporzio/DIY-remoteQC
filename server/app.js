var express = require('express');
var resquel = require('resquel');

// Create the Express.js application.
var app = express();

// Load the configuration.
var config = require('./config.json');
console.log(config.routes)
// Include the resquel library.
app.use(resquel(config));

// Listen to port.
app.listen(config.port, () => console.log('Listening to port ' + config.port))