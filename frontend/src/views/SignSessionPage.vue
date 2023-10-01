<script setup lang="ts">
import { defineAsyncComponent } from 'vue';

const Calendar = defineAsyncComponent(() => import('../components/Calendar.vue'))
const Timetable = defineAsyncComponent(() => import('../components/Timetable.vue'))



</script>

<template>
    <div class="search-card shadow-card">
        <div class="calendar-card">
            <h2 class="bold">Выберите день</h2>
            <Calendar allow_today="true"></Calendar>
        </div>
        <div class="search">
            <h2 class="bold">Выберите время</h2>
            <Timetable multiple="true"></Timetable>
            <a class="btn btn-secondary btn-search bold">Поиск</a>
        </div>
        
    </div>
</template>


<style scoped>
.calendar-card{
    width: 100%;
    background-color: white;
    padding: 25px;
}
.search{
    width: 100%;
    padding: 25px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 25px;
}

.search-card{
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    background-color: var(--primary-light-color);
    
    border-radius: 10px;
    overflow:hidden;
}

.btn-search{
    background-color: white;
    border-color: transparent;
}


@media all and (max-width: 1000px) {
    .search-card{
        flex-direction: column;
    }
    .search{
        text-align: center;
        width: auto;
        padding: 10px;
    }
    .calendar-card{
        width: auto;
        text-align: center;
        padding: 10px;
    }
}


@media all and (max-width: 580px){
}



</style>