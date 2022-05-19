const Pool = require('pg').Pool

const pool = new Pool({
    host: "localhost",
    user: "postgres",
    port: 5432,
    password: "massichiara07",
    database: "remoteQC"
})

const poolDjango = new Pool({
    host: "10.69.24.203",
    user: "postgres",
    port: 5432,
    password: "massichiara07",
    database: "fisicasanitaria"
})


const getDIYresults = (request,response) => {
    pool.query('SELECT * FROM public."dailyQC_dailyqc" ORDER BY date ASC',(error,results)=>{
        if(error){
            throw error
        }
        response.status(200).json(results.rows)
    })
}

const getEsitiCQ_MammoByImpianto = (request,response)=>{
    const id = parseInt(request.params.id)
    const anno = Number(request.params.anno)
    console.log("CIAO MASSI: ",anno)



    poolDjango.query('SELECT * FROM public."mammoLungoTermine_esitolungotermine" WHERE impianto_id=$1 ORDER BY id ASC ',
        [id],
        (error,results)=>{
        if(error){
            throw error
        }

        let data = results.rows
        if(anno){
            data = data.filter(
            entity=>{
                const year = new Date(entity.data).getFullYear()
                return year === anno
            })
        }
        response.status(200).json(data)
        })
}

const getMammografi = (request,response)=>{
    const query = 'SELECT * FROM public.impianti_impianto WHERE tipologia=\'MAMMOGRAFO\' AND data_fine IS NULL'
    poolDjango.query(query,(error,results)=>{
        if(error){
            throw error
        }
        response.status(200).json(results.rows)
    })
}

module.exports = {
    getDIYresults,
    getEsitiCQ_MammoByImpianto,
    getMammografi
}

