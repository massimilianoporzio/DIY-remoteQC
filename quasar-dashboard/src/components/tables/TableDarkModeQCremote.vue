<template>

<!--    <q-card-section>-->
<!--      <div class="text-h6 text-white">-->
<!--        Dark Mode-->
<!--        <q-btn label="Export" color="blue" class="float-right text-capitalize  shadow-3" icon="person"/>-->
<!--      </div>-->
<!--    </q-card-section>-->
    <q-separator color="white" class="q-mt-sm"/>
    <q-card-section class="q-pa-none" id="cardTable">
      <q-table  virtual-scroll
       dark :rows="apiData" row-key="id" title="Remote QC"  :rows-per-page-options="[5,10,15]"
               :pagination="{'rowsPerPage':10}"
      :visible-columns="['date','datetimeJava','kVp','mAs' ,'esito','esitoSIGNAL' ,'esitoSNR','esitoSDNR','esitoMTF50',
                          'esitoD03','esitoD4',
                          'SDNR','SNR','SIGNAL','MTF50','MTF20','MTF10']"
      :columns="columns">
         <template v-slot:body="props">
        <q-tr :props="props">
          <q-td auto-width>
            <q-toggle v-model="props.expand" checked-icon="add" unchecked-icon="remove" />
          </q-td>

          <!-- METTERE TUTTE LE DEFINIZIONI DI COLONNA QUI -->
        </q-tr>
        <q-tr v-show="props.expand" :props="props">
          <q-td colspan="100%">
            <div class="text-left">This is expand slot for row above: {{ props.row.id }}.</div>
          </q-td>
        </q-tr>
      </template>

       <template v-slot:header="props">
         <q-tr>
           <q-th colspan="1" rowspan="2">Date</q-th>
           <q-th colspan="1" rowspan="2">Analysis<br>datetime</q-th>
           <q-th colspan="1" rowspan="2">kVp</q-th>
           <q-th colspan="1" rowspan="2">mAs</q-th>
           <q-th colspan="1" rowspan="2" style="border-right: 1px solid rgb(92,92,92)">Overall<br>outcome</q-th>
           <q-th colspan="6">Outcomes</q-th>
         </q-tr>
         <q-tr>
           <q-th colspan="1">SDNR</q-th>
           <q-th colspan="1">SNR</q-th>
           <q-th colspan="1" style="border-right: 1px solid rgb(92,92,92)">SIGNAL</q-th>
           <q-th colspan="1" style="border-right: 1px solid rgb(92,92,92)">MTF<sub>50</sub></q-th>
           <q-th colspan="1">d' (0.3 mm)</q-th>
           <q-th colspan="1">d' (4 mm)</q-th>


         </q-tr>
       </template>
        <template v-slot:body-cell-esito="props">
          <q-td :props="props" style="border-right: 1px solid rgb(92,92,92)">
            <q-icon name="lightbulb" :style="{color: getColorFromEsito(props.value)}" size="2em"></q-icon>
             <q-separator vertical style="width: 1px; color:red" />
          </q-td>

        </template>
        <template v-slot:body-cell-esitoSDNR="props">
          <q-td :props="props" style="">
            <q-icon name="lightbulb" :style="{color: getColorFromEsito(props.value)}" size="1.5em"></q-icon>
          </q-td>
        </template>
        <template v-slot:body-cell-esitoSNR="props">
          <q-td :props="props" style="">
            <q-icon name="lightbulb" :style="{color: getColorFromEsito(props.value)}" size="1.5em"></q-icon>
          </q-td>
        </template>
        <template v-slot:body-cell-esitoSIGNAL="props">
          <q-td :props="props" style="border-right: 1px solid rgb(92,92,92)">
            <q-icon name="lightbulb" :style="{color: getColorFromEsito(props.value)}" size="1.5em"></q-icon>
          </q-td>
        </template>
        <template v-slot:body-cell-esitoMTF50="props">
          <q-td :props="props" style="border-right: 1px solid rgb(92,92,92)">
            <q-icon name="lightbulb" :style="{color: getColorFromEsito(props.value)}" size="1.5em"></q-icon>
          </q-td>
        </template>
        <template v-slot:body-cell-esitoD03="props">
          <q-td :props="props" style="">
            <q-icon name="lightbulb" :style="{color: getColorFromEsito(props.value)}" size="1.5em"></q-icon>
          </q-td>
        </template>
        <template v-slot:body-cell-esitoD4="props">
          <q-td :props="props">
            <q-icon name="lightbulb" :style="{color: getColorFromEsito(props.value)}" size="1.5em"></q-icon>
          </q-td>
        </template>
        <template v-slot:body-cell-SIGNAL="props">
          <q-td :props="props" style="border-right: 1px solid rgb(92,92,92)">
            {{props.value}}
          </q-td>
        </template>
      </q-table>
    </q-card-section>

</template>

<script setup>
import { format, parseJSON ,fromUnixTime , parse, formatRelative, subDays } from 'date-fns'
import {ref, defineProps, onMounted} from 'vue'
const props = defineProps( {
    apiData: {},

  })
const tabledata = ref([])

const columns = [{
        name: 'date',
        align: 'center',
        label: 'Exposure date',
        // field: row=> format(row.date, 'dd/MM/yyyy')
        field: row => format(parseJSON(row.date),'dd/MM/yyyy')
        },
  {
    name: 'datetimeJava',
    align: 'center',
    label: 'QC execution datetime',
    field: row => format(parseJSON(row.datetimeJava) ,'dd/MM/yyyy hh:mm:ss')
    // field: row => row.datetimeJava
  },
{
    name: 'kVp',
    align: 'center',
    style: 'max-width: 20px; min-width: 20px',
    field: row => row.kV
  },
  {
    name: 'mAs',
    align: 'center',
    style: 'max-width: 20px; min-width: 20px',
    field: row => row.mAs
  },
  {
    name: 'esito',
    align: 'center',
    label: 'QC outcome',
    field: row => getOverallEsito(row)
  },
    {
    name: 'esitoSDNR',
    align: 'center',
    style: 'max-width: 10px; min-width: 10px',
    field: row => getEsito(row.esitoSDNR)
  },
    {
    name: 'esitoSNR',
    align: 'center',
    field: row => getEsito(row.esitoSNR)
  },
   {
    name: 'esitoSIGNAL',
    align: 'center',
    field: row => getEsito(row.esitoSIGNAL)
  },
  {
    name: 'esitoMTF50',
    align: 'center',
    field: row => getEsito(row.esitoMTF50)
  },
  {
    name: 'esitoD03',
    align: 'center',
    field: row => getEsito(row.esitoD03)
  },
  {
    name: 'esitoD4',
    align: 'center',
    field: row => getEsito(row.esitoD4)
  },


]

const getOverallEsito = (obj)=>{
  const allOK = obj.esitoD03 && obj.esitoD4 && obj.esitoMTF50 && obj.esitoSDNR && obj.esitoSNR && obj.esitoSIGNAL
  const allKO = !obj.esitoD03 && !obj.esitoD4 && !obj.esitoMTF50 && !obj.esitoSDNR && !obj.esitoSNR && !obj.esitoSIGNAL
  return allOK ? 'OK' : allKO ? 'KO' : 'WARNING'

}

const getEsito = (esito) => {
  return esito ? 'OK' :'KO'
}

const getColorFromEsito = (esito)=>{
  return esito === 'OK' ? '#21BA45' : esito === 'KO' ? '#C10015' : '#F2C037'
}

onMounted(()=>{
  console.log("MOUNTED TABLE DARK")
  tabledata.value = props.apiData.map(obj => ({ ...obj,
    esito: getOverallEsito(obj),
    esitoSDNR: getEsito(obj.esitoSDNR)}))

  console.log("tableData: ",tabledata.value)
})


</script>


<style lang="css">

</style>
