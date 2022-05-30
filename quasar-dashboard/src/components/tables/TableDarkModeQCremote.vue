<template>

<!--    <q-card-section>-->
<!--      <div class="text-h6 text-white">-->
<!--        Dark Mode-->
<!--        <q-btn label="Export" color="blue" class="float-right text-capitalize  shadow-3" icon="person"/>-->
<!--      </div>-->
<!--    </q-card-section>-->
    <q-separator color="white" class="q-mt-sm"/>
    <q-card-section class="q-pa-none">
      <q-table dark :rows="apiData" row-key="id" title="Remote QC"  :rows-per-page-options="[5,10,15]"
               :pagination="{'rowsPerPage':10}"
      :visible-columns="['date','datetimeJava','signal','esito' ,'SNR','SDNR','MTF50','MTF20','MTF10','D03']"
      :columns="columns">
       <template v-slot:header="props">
         <q-tr>
           <q-th colspan="1">Date</q-th>
           <q-th colspan="1">Analysis datetime</q-th>
           <q-th colspan="1">Signal</q-th>
         </q-tr>
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
    name: 'signal',
    align: 'center',
    label: 'PV (Signal)',
    field: row => row.SIGNAL
  },
  {
    name: 'esito',
    align: 'center',
    label: 'QC outcome',
    field: row => row.esito
  }
]

onMounted(()=>{
  console.log("MOUNTED TABLE DARK")
  tabledata.value = props.apiData.map(obj => ({ ...obj,
    esito: true}))

  console.log("tableData: ",tabledata.value)
})


</script>


<style lang="css">

</style>
