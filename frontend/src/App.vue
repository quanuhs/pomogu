<script setup lang="ts">
import {RouterView, useRoute} from 'vue-router'
import { defineAsyncComponent, ref } from 'vue';
import Navigation from './components/MainNavigation.vue'

import {authorised} from './api'

const Menu = defineAsyncComponent(() => import('./components/MenuBar.vue'))
// const Navigation = defineAsyncComponent(() => import('./components/MainNavigation.vue'))

const Authentication = defineAsyncComponent(() => import('./components/Authentication.vue'))



let authentication_window: any = ref(null)

async function openAuth(event: any) {
  authentication_window.value.showModal()
}

async function closeAuth(event: any) {
  authentication_window.value.close()
}

const router = useRoute();

</script>

<template>
  
  <div v-if="router.name == 'videocall' || router.name == 'not-found'">
    <Suspense>
      <router-view/>
    </Suspense>
  </div>

  <div v-else style="height: 100%">
    <div class="normal-menu"> <Navigation @openAuth="openAuth"></Navigation> </div>

    <dialog class="auth" v-if="!authorised" ref="authentication_window">
      <Authentication @onExit="closeAuth"></Authentication>
    </dialog>

    <Suspense>
      <router-view/>
    </Suspense>

    <div class="mobile-menu"> <Menu @openAuth="openAuth"></Menu> </div>

  </div>


</template>

<style>

.auth{
  border: none;
  background-color: transparent;  
  width: min(600px, 100%);
  padding: 0;

}

.auth::backdrop{
  background-color: rgba(0, 0, 0, 0.6);
  transition: all 2s;
}

.footer{
  height: 80px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.normal-menu{
  display: block;
}

.mobile-menu{
  display: none;
}

.content{
  padding-bottom: 30px;
}

@media all and (max-width: 777px){
  .mobile-menu{
    display: block;
  }

  .normal-menu{
    display: none;
  }

  .content{
    margin-top: 25px;
    padding-bottom: 80px;
  }

}

</style>

