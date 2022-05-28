<template>

<!--    <q-card-section>-->
<!--      <div class="text-h6 text-white">-->
<!--        Dark Mode-->
<!--        <q-btn label="Export" color="blue" class="float-right text-capitalize  shadow-3" icon="person"/>-->
<!--      </div>-->
<!--    </q-card-section>-->
    <q-separator color="white" class="q-mt-sm"/>
    <q-card-section class="q-pa-none">
      <q-table dark :rows="apiData" title="Remote QC" row-key="id"
      :visible-columns="['date','datetimeJava','SIGNAL','SNR','SDNR','MTF50','MTF20','MTF10','D03']">

      </q-table>
    </q-card-section>

</template>

<script setup>
import {ref, defineProps, onMounted} from 'vue'
const props = defineProps( {
    apiData: [],

  })

onMounted(()=>{
  console.log("dbData: ",props.apiData)
})


</script>


<style lang="css">

</style>
