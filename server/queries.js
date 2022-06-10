const Pool = require('pg').Pool

const pool = new Pool({
    host: "localhost",
    user: "postgres",
    port: 5432,
    password: "massichiara07",
    database: "remoteQC"
})

const poolDjango = new Pool({
    host: "127.0.0.1",
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

const updateComments = (request,response)=>{
    const id = parseInt(request.params.id)
    const {comments} = request.body
    const query = "UPDATE public.\"dailyQC_dailyqc\"\n" +
        "SET comments=$1 WHERE id=$2"
    pool.query(
        query,[comments,id],
        (error, results)=>{
            if (error){throw error}
            response.status(200).send(`qc modified with ID: $(id)`)
        }
    )
}

const getMammografi = (request,response)=>{
    const query = 'SELECT imp.id, imp.marca, imp.modello,imp.photo, ospedale.name as nome_ospedale ,sala.name as nome_sala, MAX(cq.data) as data_ultimo_cq\n' +
        '\tFROM public.impianti_impiantosala impSala, public.ospedali_ospedale ospedale ,public.ospedali_sala sala,\n' +
        '\tpublic.impianti_impianto imp,  public.controlli_controllo cq\n' +
        '\tWHERE imp.tipologia = \'MAMMOGRAFO\' AND data_fine_insala IS  NULL\n' +
        '\t AND impSala.impianto_id = imp.id\n' +
        '\t AND ospedale.id=impSala.ospedale_id\n' +
        '\t AND sala.id = impSala.sala_id \n' +
        '\t AND cq.impianto_id = impSala.impianto_id\n' +
        '\t AND imp.data_fine IS NULL\n' +
        '\t GROUP BY imp.id,imp.marca, imp.modello,imp.photo, ospedale.name, sala.name'
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
    getMammografi,
    updateComments
}

