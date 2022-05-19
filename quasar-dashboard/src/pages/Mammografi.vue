<template>
  <q-page class="q-pa-sm">

    <div>
      <q-card class="no-border no-shadow bg-transparent">
        <q-card-section class="q-pa-sm">
          <q-input rounded v-model="search" outlined placeholder="Search Product">
            <template v-slot:append>
              <q-icon v-if="search === ''" name="search"/>
              <q-icon v-else name="clear" class="cursor-pointer" @click="search = ''"/>
            </template>
          </q-input>
        </q-card-section>
      </q-card>
    </div>
    <div class="row q-col-gutter-sm">
      <div class="col-md-4 col-lg-4 col-sm-12 col-xs-12 flex" v-for="item, item_index in mammoData">
        <card-product :data="item"></card-product>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import {defineComponent, defineAsyncComponent, onMounted} from 'vue';
import {ref} from 'vue';
import {colors} from 'quasar'
import axios from "axios";
const search = ref('');
const {changeAlpha} = colors
const mammoData = ref([])
const emptyData = ref(false)
const data = [
  {
    title: 'Our Changing Planet',
    caption: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    rating: 2,
    amount: '$30',
    img: require('../assets/products/c-d-x-PDX_a_82obo-unsplash.jpg'),
    chip: 'Giorni dall\'ultimo sopralluogo: 150',
    chip_color: 'grey-4',
    chip_class: 'text-black absolute-top-left'
  },
  {
    title: 'Our Changing Planet',
    caption: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    rating: 4,
    amount: '$15',
    img: require('../assets/products/frankie-valentine-VghbBAYqUJ0-unsplash.jpg'),
  },
  {
    title: 'Our Changing Planet',
    caption: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    rating: 1,
    amount: '$50',
    img: require('../assets/products/giorgio-trovato-K62u25Jk6vo-unsplash.jpg'),
    chip: 'Sold Out',
    chip_color: 'grey-8',
    chip_class: 'text-white absolute-top-right'
  },
  {
    title: 'Our Changing Planet',
    caption: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    rating: 5,
    amount: '$70',
    img: require('../assets/products/jeroen-den-otter-iKmm0okt6Q4-unsplash.jpg'),
    chip: 'Discount 50%',
    chip_color: 'grey-4',
    chip_class: 'text-blue absolute-top-right'
  },
  {
    title: 'Our Changing Planet',
    caption: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    rating: 2,
    amount: '$50',
    img: require('../assets/products/john-fornander-m2WpKnlLcEc-unsplash .jpg'),
  },
  {
    title: 'Our Changing Planet',
    caption: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    rating: 4,
    amount: '$30',
    img: require('../assets/products/marek-szturc-0iIV1goIodE-unsplash.jpg'),
  },
];

 const requestData = ()=> {
      axios.get('http://localhost:3000/mammografi')
        .then(response => {
          console.log("USED AXIOS ",response.data)
          const dati = response.data.map(entry=>{
            return {
              title: entry.marca + ' '+entry.modello,
              caption: entry.nome_ospedale + '<br>' + entry.nome_sala,
              img: 'http://10.69.24.203/media/' + entry.photo
            }})
          console.log('DATI: ',dati)
          mammoData.value = dati
          console.log('mammoData: ',mammoData.value)
          if(!response.data.length){
            this.emptyData = true
            console.log("SORRY NO DATA FROM THE API")
          }

        }).catch(()=>{
          // this.loaded = false
      })
    }


const CardProduct = defineAsyncComponent(() => import('components/cards/CardMammografo'))
onMounted(async ()=>{
  requestData()
  console.log("MAMMOGRAFI MOUNTED")

})
</script>

<style scoped>

</style>
