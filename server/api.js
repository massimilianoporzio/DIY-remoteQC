const client = require('./connection.js')
const express = require('express');
const app = express();
const db = require('./queries')

app.use(function (req, res, next) {

        // Website you wish to allow to connect
        // res.setHeader('Access-Control-Allow-Origin', 'http://localhost:8080');
        res.setHeader('Access-Control-Allow-Origin', '*');

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
    client.query(`SELECT id, date, "datetimeJava", "SIGNAL", "SNR", "SDNR", "MTF50", "MTF20", "MTF10", "D03", "D4", "mAs",
baseline, "DI", "EI", "EIt", encode(signal_image, 'base64') as signal_image,
    "mAs", "DAP","CONTRAST",
    comments, "esitoCONTRAST", "esitoD03", "esitoD4", "esitoMTF50", "esitoSDNR", "esitoSIGNAL", "esitoSNR",
     "kV", "deltaCONTRAST", "deltaD03", "deltaD4", "deltaDAP", "deltaDI", "deltaEI", "deltaMAS", "deltaMTF50", 
     "deltaSDNR", "deltaSIGNAL", "deltaSNR", "diffKV", "deltaMTF10", "deltaMTF20"
FROM public."dailyQC_dailyqc" ORDER BY date ASC;`, (err, result)=>{
        if(!err){
            res.send(result.rows);
        }
    });
    client.end;
})

app.get('/resultsDIY',db.getDIYresults)
app.get('/esitoMammo/:id/:anno?',db.getEsitiCQ_MammoByImpianto)

app.get('/mammografi',db.getMammografi)

app.put('/updateQC/:id',db.updateComments)



