<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          @click="toggleLeftDrawer"
          icon="menu"
          aria-label="Menu"
        />
        <q-toolbar-title>
          Remote QC dashboard
        </q-toolbar-title>
        <q-space/>
        <div class="q-gutter-sm row items-center no-wrap">
          <q-btn round dense flat color="white" :icon="$q.fullscreen.isActive ? 'fullscreen_exit' : 'fullscreen'"
                 @click="$q.fullscreen.toggle()"
                 v-if="$q.screen.gt.sm">
          </q-btn>

          <q-btn round dense flat color="white" icon="notifications">
            <q-badge color="red" text-color="white" floating>
              5
            </q-badge>
            <q-menu
            >
              <q-list style="min-width: 100px">
                <messages></messages>
                <q-card class="text-center no-shadow no-border">
                  <q-btn label="View All" style="max-width: 120px !important;" flat dense
                         class="text-indigo-8"></q-btn>
                </q-card>
              </q-list>
            </q-menu>
          </q-btn>
          <q-btn round flat>
            <q-avatar size="26px">
              <img src="https://cdn.quasar.dev/img/boy-avatar.png">
            </q-avatar>
          </q-btn>
        </div>
      </q-toolbar>
    </q-header>

<!--    <q-drawer-->
<!--      v-model="leftDrawerOpen"-->
<!--      show-if-above-->
<!--      bordered-->
<!--      class="bg-primary text-white"-->
<!--    >-->
<!--      <q-list>-->
<!--        <q-item to="/" active-class="q-item-no-link-highlighting">-->
<!--          <q-item-section avatar>-->
<!--            <q-icon name="dashboard"/>-->
<!--          </q-item-section>-->
<!--          <q-item-section>-->
<!--            <q-item-label>Mammografi</q-item-label>-->
<!--          </q-item-section>-->
<!--        </q-item>-->
<!--        <q-item to="/Charts" active-class="q-item-no-link-highlighting">-->
<!--          <q-item-section avatar>-->
<!--            <q-icon name="insert_chart"/>-->
<!--          </q-item-section>-->
<!--          <q-item-section>-->
<!--            <q-item-label>DIY ECMP 2022</q-item-label>-->
<!--          </q-item-section>-->
<!--        </q-item>-->
<!--      </q-list>-->
<!--    </q-drawer>-->

    <q-footer elevated>
        <q-toolbar>
          <q-toolbar-title>Remote QC</q-toolbar-title>
          <p class="text-caption q-pt-md">
            <a class="text-white transparent q-pa-none" target="_blank" href="https://icons8.com/icon/952/raggi-x">Raggi X </a> &nbsp;favicon by &nbsp;  <a class="text-white transparent q-pa-none" target="_blank" href="https://icons8.com">Icons8</a>
          </p>


<!--          <a class="text-white" href="https://www.flaticon.com/free-icons/radiology" title="radiology icons">Radiology icons created by Freepik - Flaticon</a>-->
        </q-toolbar>
      </q-footer>

    <q-page-container class="bg-grey-2">
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from 'components/EssentialLink.vue'
import Messages from "./Messages";

import { defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink,
    Messages
  },

  setup () {
    const leftDrawerOpen = ref(false)

    return {
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  }
})
</script>
