<template>
    <div class="timetable">
        <button v-for="t in 24" :key="t"
        @click.prevent="selectTime(t-1)"
        class="btn text"
        :class="{'selected': selected_time[t-1] == true}">{{t-1}}:00</button>
        
    </div>

</template>

<script setup lang="ts">
import {ref} from 'vue'

const props = defineProps({
    multiple: {type: Boolean, required: true, default: false},
    sessions: {type: Array<any>, required: false, default: []},
})


let selected_time = ref({})

async function selectTime(t:number){


    if (selected_time.value[t] == undefined){
        if (!props.multiple){
            selected_time.value = {}
        }

        selected_time.value[t] = true
    }else{
        delete selected_time.value[t]
    }

    
    console.log(selected_time.value)
}

</script>

<style>


.timetable{
    width: 100%;
    display: grid;
    grid-template-columns: repeat(auto-fill, 62px);
    gap: 15px;
    text-align: center;
    justify-content: center;
    align-items: center;
}

.timetable > button{
    background-color: white;
    width: 100%;
    border-radius: 10px;
    cursor: pointer;
    height: auto;
    aspect-ratio: 1/1;
    border: 0;
    border-color: transparent;
}

.selected{
    background-color: var(--primary-color) !important;
    box-sizing: border-box;
    padding: auto;
    filter: drop-shadow(-2px 2px 2px rgba(0, 0, 0, 0.25));
}

</style>