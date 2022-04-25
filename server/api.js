const client = require('./connection.js')
const express = require('express');
const app = express();
app.use(function (req, res, next) {

        // Website you wish to allow to connect
        res.setHeader('Access-Control-Allow-Origin', 'http://localhost:8080');

        // Request methods you wish to allow
        res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');

        // Request headers you wish to allow
        res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');

        // Set to true if you need the website to include cookies in the requests sent
        // to the API (e.g. in case you use sessions)
        res.setHeader('Access-Control-Allow-Credentials', true);

        // Pass to next layer of middleware
        next();
    });


app.listen(3000, ()=>{
    console.log("Sever is now listening at port 3000");
})

client.connect();
const bodyParser = require("body-parser");
app.use(bodyParser.json());
app.get('/results', (req, res)=>{
    client.query(`SELECT * FROM public."dailyQC_dailyqc" ORDER BY date ASC;`, (err, result)=>{
        if(!err){
            res.send(result.rows);
        }
    });
    client.end;
})

