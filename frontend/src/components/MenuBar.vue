<script setup lang="ts">
  import CalendarIcon from './icons/IconCalendar.vue'
  import CatalogIcon from './icons/IconCatalog.vue'
  import ProfileIcon from './icons/IconProfile.vue'
  import HomeIcon from './icons/IconHome.vue'

  
  import {authorised} from '../api'
  const emit = defineEmits(['openAuth'])

</script>

<template>

  <nav class="small-display text-small">
    <a class="nav-link" href="/">
      <div><HomeIcon/></div>
      <div class="logo-text">Главная</div>
    </a>
    <a class="nav-link" href="/search">
      <div><CatalogIcon/></div>
      <div class="logo-text">Каталог</div>
    </a>
    <!-- <a class="nav-link" href="">
      <div><CalendarIcon/></div>
      <div class="logo-text">Календарь</div>
    </a> -->
    <a v-if="authorised" class="nav-link" href="/me">
      <div><ProfileIcon/></div>
      <div class="logo-text">Профиль</div>
    </a>
    <a v-else class="nav-link" @click.prevent="emit('openAuth')">
      <div><ProfileIcon/></div>
      <div class="logo-text">Войти</div>
    </a>
  </nav>
  
</template>

<style scoped>

.svg-icon-menu{
    width: 24px;
    height: 24px;
    display: block;
    margin: auto;
    display: flex;
    align-items: center;
    justify-content: center;
}

.nav-link{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.small-display > a{
  width: 128px;
}

.small-display{

  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  height: 40px;
  padding-top: 10px;
  padding-bottom: 10px;

  
  background-color: #FFDA83;
  opacity: 1;
  border-radius: 10% 10% 0 0;

  position: fixed; 
  bottom: 0;
  left: 0;
  width: 100%;
  opacity: 1;

  font-size: 12px !important;
  font-weight: bold;

  z-index: 2;

}

</style>
