<template>
  <q-card class="">
    <q-img :src="data.img" height="300px">
      <q-chip v-if="data.chip" :class="data.chip_class" :color="data.chip_color" :label="data.chip"></q-chip>
    </q-img>

    <q-card-section>
      <div class="text-h6">
        {{ data.title }}
      </div>
      <div class="text-subtitle3 text-justify q-mt-sm">
       <span v-html="data.caption"></span>

      </div>
      <div class="row justify-end ">
        <span class="text-h6 float-right">
          <q-btn label="Vedi CQ settimanali" rounded color="secondary" outline @click="gotoDetail"></q-btn>
        </span>
      </div>
    </q-card-section>



  </q-card>
</template>


<script setup>
import {ref} from 'vue'
import {useRouter} from "vue-router";
const router = useRouter()
const props = defineProps(['data'])

  const gotoDetail = ()=>{
    console.log("GOTO DETAIL OF MAMMO with ID: ",props.data.id)
    router.push({name: 'mammoqc',params: {impianto_id: props.data.id}})
  }

</script>

<style scoped>

</style>
