const {Client} = require('pg')

const client = new Client({
    host: "localhost",
    user: "postgres",
    port: 5432,
    password: "massichiara07",
    database: "remoteQC"
})



module.exports = client
