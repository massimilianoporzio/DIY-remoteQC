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
          <q-btn label="Vedi CQ settimanali" rounded color="secondary" outline></q-btn>
        </span>
      </div>
    </q-card-section>



  </q-card>
</template>

<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "CardProduct",

  props: ['data']
})
</script>

<style scoped>

</style>
