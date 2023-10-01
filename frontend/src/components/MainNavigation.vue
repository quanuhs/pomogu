<script setup lang="ts">
  import { defineAsyncComponent } from 'vue';
  import { onMounted, reactive, ref } from 'vue';
  import {authorised} from '../api'
  
  const CloudIcon = defineAsyncComponent(() => import('./icons/IconCloud.vue'));
  const emit = defineEmits(['openAuth'])



</script>

<template>
  <nav class="nav text-small bold normal-display">
        <div class="logo">
            <a href="/">
                <div class="logo-image">
                    <CloudIcon/>
                </div>
                <div class="logo-text">помогу</div>
            </a>
        </div>

        <div class="menu">
          <a class="nav-link" href="/">О нас</a>
          <a class="nav-link" href="search">Каталог</a>
          <a v-if="!authorised" class="nav-link nav-auth" href="auth" @click.prevent="emit('openAuth')">
            
            <span><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-shift-fill" viewBox="0 0 16 16">
              <path d="M7.27 2.047a1 1 0 0 1 1.46 0l6.345 6.77c.6.638.146 1.683-.73 1.683H11.5v3a1 1 0 0 1-1 1h-5a1 1 0 0 1-1-1v-3H1.654C.78 10.5.326 9.455.924 8.816L7.27 2.047z"/>
            </svg></span>
          Вход</a>
          <a class="nav-link" v-if="authorised" href="/me">Профиль</a>
        </div>

    </nav>

</template>
<style scoped>

.nav-link{
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  gap: 2px;
  min-width: 100px;
  height: 40px;
  border: 0px solid transparent;
  border-color: transparent;
  box-sizing: border-box;
  transition: border 0.2s;
}

.nav-link:hover:not(.nav-auth){
  box-sizing: border-box;
  border-bottom: 5px solid var(--primary-light-color);
  transition: border 0.2s;
}

.nav{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 15px;
    margin-bottom: 50px;
}

.nav-auth > span{
  position: absolute;
  left: -5%;
  color: transparent;
  rotate: 90deg;
  
  display: flex;
  justify-content: center;
  align-items: flex-start;
  


}

.nav-auth:hover > span{
  position: absolute;
  left: -20%;
  color: black;
  transition: color 0.8s;

}

.nav-auth{
  position: relative;
  background-color: var(--primary-color);;
  box-sizing: border-box;
  border: 0px solid transparent;
  border-color: var(--primary-color);
  border-radius: 25px;
  transition: 0.5s;
  overflow: hidden;
}

.nav-auth:hover{
  border-left: 30px solid var(--primary-color);
  transition:0.5s;
  
  overflow: unset;
}


.menu {
    display: inline-flex;
    flex-wrap: wrap;
    gap: 5px;
    align-items: space-evenly;
    justify-content: center;
    
}

.logo{
    display: flex;
    flex-grow: 1;
}

.logo > a{
    display: flex;
    flex-direction: row;
    text-align: center;
    align-items: center;
    gap: 10px;
    outline: none;
    text-decoration: none;
    color: inherit;
    width: 120px;
}

.logo-image{
    width: 55px;
    height: 36px;
}


@media all and (max-width: 777px){

    .logo{
      align-items: center;
      flex-grow: 0;
    }

    .logo > a{
      flex-direction: column;
      gap: 2px;
    }


    .nav{
      justify-content: center;
      flex-direction: column;
      gap: 25px;
      margin-bottom: 25px;
    }

}

</style>