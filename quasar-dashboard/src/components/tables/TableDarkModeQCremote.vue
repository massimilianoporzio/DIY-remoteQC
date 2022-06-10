<template>

<!--    <q-card-section>-->
<!--      <div class="text-h6 text-white">-->
<!--        Dark Mode-->
<!--        <q-btn label="Export" color="blue" class="float-right text-capitalize  shadow-3" icon="person"/>-->
<!--      </div>-->
<!--    </q-card-section>-->
<!--    <q-separator color="white" class="q-mt-sm"/>-->
    <q-card-section class="q-pa-none" id="cardTable">
      <q-table virtual-scroll title="QC Results"
       dark :rows="apiData" row-key="id"   :rows-per-page-options="[5,10,15]"
               :pagination="{'rowsPerPage':10}"
      :visible-columns="['date','datetimeJava','kVp','mAs' ,'esito','esitoSIGNAL' ,'esitoSNR','esitoSDNR','esitoMTF50',
                          'esitoD03','esitoD4',
                          'SDNR','SNR','SIGNAL','MTF50','MTF20','MTF10']"
      :columns="columns">
         <template v-slot:body="props">
        <q-tr  :props="props">
          <q-td auto-width>
            <q-btn dense flat icon="add" @click="props.expand = !props.expand">

            </q-btn>

          </q-td>

          <!-- METTERE TUTTE LE DEFINIZIONI DI COLONNA QUI -->
          <q-td auto-width key="date" :props="props">
            {{format(parseJSON(props.row.date),'dd/MM/yyyy')}}
          </q-td>
          <q-td auto-width key="datetimeJava" :props="props">
            {{format(parseJSON(props.row.datetimeJava) ,'dd/MM/yyyy hh:mm:ss')}}
          </q-td>
           <q-td auto-width key="kVp" :props="props">
             {{props.row.kV}}
           </q-td>
          <q-td auto-width key="mAs" :props="props">
             {{props.row.mAs}}
           </q-td>
          <q-td auto-width key="esito" :props="props" style="border-right: 1px solid rgb(92,92,92)">
            <q-icon name="lightbulb" :style="{color: getColorFromEsito(getOverallEsito(props.row))}" size="2em"></q-icon>
          </q-td>
          <q-td auto-width key="esitoSDNR" :props="props" style="">
            <q-icon name="lightbulb" :style="{color: getColorFromEsito(getEsito(props.row.esitoSDNR))}" size="1.5em"></q-icon>
          </q-td>
           <q-td auto-width key="esitoSNR" :props="props" style="">
            <q-icon name="lightbulb" :style="{color: getColorFromEsito(getEsito(props.row.esitoSNR))}" size="1.5em"></q-icon>
          </q-td>
           <q-td auto-width key="esitoSIGNAL" :props="props" style="border-right: 1px solid rgb(92,92,92)">
            <q-icon name="lightbulb" :style="{color: getColorFromEsito(getEsito(props.row.esitoSIGNAL))}" size="1.5em"></q-icon>
          </q-td>
          <q-td auto-width key="esitoMTF50" :props="props" style="border-right: 1px solid rgb(92,92,92)">
            <q-icon name="lightbulb" :style="{color: getColorFromEsito(getEsito(props.row.esitoMTF50))}" size="1.5em"></q-icon>
          </q-td>
          <q-td auto-width key="esitoD03" :props="props" style="">
            <q-icon name="lightbulb" :style="{color: getColorFromEsito(getEsito(props.row.esitoD03))}" size="1.5em"></q-icon>
          </q-td>
          <q-td auto-width key="esitoD4" :props="props" style="">
            <q-icon name="lightbulb" :style="{color: getColorFromEsito(getEsito(props.row.esitoD4))}" size="1.5em"></q-icon>
          </q-td>
        </q-tr>
        <q-tr v-show="props.expand" :props="props" style="border-bottom: 1px solid rgb(92,92,92)">
          <q-td auto-width colspan="2">
            <div class="text-left"><q-img :src="getImageSrcFromRow(props.row)"></q-img></div>
          </q-td>
          <q-td auto-width colspan="1">
            <div class="text-left">
              <div class="text-subtitle2">Exposure params</div>
              EI={{props.row.EI}}<br>
              DI={{props.row.DI}}<br>
              EI<sub>t</sub>={{props.row.EIt}}<br>
              DAP={{props.row.DAP}} µGy cm² <br>

            </div>
          </q-td>
          <q-td auto-width colspan="1">
            <div class="text-subtitle2">MTF values</div>
            MTF<sub>50</sub>= {{props.row.MTF50}}<br>
            MTF<sub>20</sub>= {{props.row.MTF20}}<br>
            MTF<sub>10</sub>= {{props.row.MTF10}}
          </q-td>
          <q-td auto-width colspan="2" style="border-right: 1px solid rgb(92,92,92)">
            <div class="text-subtitle2">Contrast and Signal values</div>
            Signal (Al target)={{props.row.SIGNAL}}<br>
            Contast: {{props.row.CONTRAST}} %<br>
            SNR: {{props.row.SNR}}<br>
            SDNR: {{props.row.SDNR}}

          </q-td>
          <q-td auto-width colspan="4">
            <div class="text-subtitle2 text-center">Variations from baseline<br>&Delta; (%)</div>
            <div class="row q-pt-md">
              <div class="col text-left">
                &Delta;SDNR= {{props.row.deltaSDNR}}<br>
                &Delta;SNR= {{props.row.deltaSNR}}<br>
                &Delta;SIGNAL= {{props.row.deltaSIGNAL}}<br>
                &Delta;CONTRAST= {{props.row.deltaCONTRAST}}<br>
              </div>

              <div class="col text-left">
                &Delta;d' (0.3 mm) = {{props.row.deltaD03}}<br>
                &Delta;d' (4 mm) = {{props.row.deltaD4}}<br>
              </div>

            </div>
            <div class="row q-mt-sm">

                <div class="col text-left">
                  &Delta;MTF<sub>50</sub>= {{props.row.deltaMTF50}}<br>
                  &Delta;MTF<sub>20</sub>= {{props.row.deltaMTF20}}<br>
                  &Delta;MTF<sub>10</sub>= {{props.row.deltaMTF10}}
                </div>
              <div class="col text-left">
                  &Delta; mAs = {{props.row.deltaMAS}}<br>
                  &Delta; EI = {{props.row.deltaEI}}<br>
                  &Delta; DI = {{props.row.deltaDI}}<br>

                </div>
            </div>
          </q-td>
          <q-td auto-width colspan="2">
             <div class="text-subtitle2 text-center">Comments</div>

              <q-input dark
                 v-model="props.row.comments"
                  filled
                  :autogrow="props.expand"
                />
              <div class="row justify-between q-mt-lg">
                <q-btn color="warning" icon-right="mail" size="1em" label="Edit" />
                <q-btn color="secondary" icon-right="mail" size="1em" label="Send" />
              </div>



          </q-td>

        </q-tr>
      </template>

       <template v-slot:header="props">
         <q-tr>
           <q-th colspan="1" rowspan="2"></q-th>
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

const textComments = ref('')
const tabledata = ref([])

const getImageSrcFromRow = (row)=>{
  return 'data:image/jpeg;base64,'+row.signal_image
}
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
