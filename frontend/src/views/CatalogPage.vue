<script lang="ts">

import { defineAsyncComponent } from 'vue';


import GirlIcon from '../components/icons/IconGirlAdult.vue'
import BoyIcon from '../components/icons/IconBoyChild.vue'

import FamilyIcon from '../components/icons/IconFamily.vue'
import SoloIcon from '../components/icons/IconSolo.vue'

import TherapistCard from '../components/TherapistCard.vue'

const Calendar = defineAsyncComponent(() => import('../components/Calendar.vue'))
const Timetable = defineAsyncComponent(() => import('../components/Timetable.vue'))

</script>

<template>
    <div class="content">
        <!-- <form> -->
        <div class="card shadow-card">
            <h2 class="bold">Подбор психолога</h2>
            <div class="fields">
                <div class="group">
                    <label>Возраст</label>
                    <div class="choice">
                        <label>
                            <input id="age-adult" @change="onChange($event)" @focus="onChange($event)" @focusout="onChange($event)" type="checkbox" name="age" value="adult">
                            <label for="age-adult" class="text-small bold">Взрослые</label>
                            <GirlIcon/>
                            
                        </label>

                        <label>
                            <input id="age-young" @change="onChange($event)" @focus="onChange($event)" @focusout="onChange($event)" type="checkbox" name="age" value="child">
                            <label for="age-young" class="text-small bold">Дети</label>
                            <BoyIcon/>
                        </label>
                    </div>

                </div>
                <div class="group">
                    <label>Формат</label>
                    <div class="choice">
                        <label>
                            <input id="format-solo" @change="onChange($event)" @focus="onChange($event)" @focusout="onChange($event)" type="checkbox" name="format" value="solo">
                            <label for="format-solo" class="text-small bold">Индивидуально</label>
                            <SoloIcon/>

                        </label>

                        <label>
                            <input id="format-family" @change="onChange($event)" @focus="onChange($event)" @focusout="onChange($event)" type="checkbox" name="format" value="family">
                            <label for="format-family" class="text-small bold">Пары<br>Семьи</label>
                            <FamilyIcon/>
                        </label>
                    </div>

                </div>
            </div>
            <div class="fields">
                <div class="group">
                    <label class="bold">Методы</label>
                    <select multiple class="text-small" name="methods">
                        <option value="all" selected disabled hidden>Все</option>
                        <option v-for="opt in methods_options" :value="opt.code">{{opt.name}}</option>
                    
                    </select>

                </div>

                <div class="group">
                    <label class="bold">Специализация</label>
                    <select multiple class="text-small chosen-select" placeholder="test" name="speciality">
                        <option value="all" selected disabled hidden>Все</option>
                        <option v-for="opt in speciality_options" :value="opt.code">{{opt.name}}</option>
                    </select>
                </div>
            </div>

            <div class="price" style="display: none">
                <label>Цена</label>
                <input type="range" step="1">
                <div class="price-vars">
                    <div>
                        <label>от</label>
                        <input value="0" class="text-small input-price" type="number">
                        <label>₽</label>
                    </div>

                    <div>
                        <label>до</label>
                        <input value="5000" class="text-small input-price" type="number">
                        <label>₽</label>
                    </div>
                </div>
            </div>
        </div>

        <div class="search-card shadow-card">
            <div class="calendar-card">
                <h2 class="bold">Выберите день</h2>
                <Calendar></Calendar>
            </div>
            <div class="search">
                <h2 class="bold">Выберите время</h2>
                <Timetable></Timetable>
                <button class="btn btn-secondary btn-search bold text" @click="">Поиск</button>
            </div>
            
        </div>
    <!-- </form> -->

        <div v-if="therapists.length > 0 " class="therapists-results">
            <TherapistCard v-for="therapist in therapists"
            :id="therapist.id"
            :name="therapist.name"
            :description="therapist.description"
            :tags = "therapist.tags"
            :price = "therapist.price"
            :methods="therapist.methods"
            :avatar="therapist.avatar_url"
            />
        </div>

        <div v-else style="padding: 50px; text-align: center;">
            <h2 class="bold">По вашему запросу специалисты не найдены</h2>
        </div>

    </div>
</template>




<script setup lang="ts">

import { defineComponent, ref, reactive} from 'vue';
import {getTherapists, getMethonds, getSpeciality} from '../api';
import {useRouter} from 'vue-router'


let __therapists = await getTherapists()
console.log(__therapists)
let therapists = ref(__therapists)
const router = useRouter()

let methods_options = ref( await getMethonds() )

let speciality_options = ref( await getSpeciality() )


function onChange(event: Event){

    let target: any = event.currentTarget;
    let parent: any = target.parentElement;

    if (event.type == "change"){

        if (target.checked){
            parent.classList.add("bg-primary-light", "shadow-card")
        }else{
            parent.classList.remove("bg-primary-light", "shadow-card")
        }

        // router.push({path:"/search", query:{'age': target.value}})


    }

    if (event.type == "focus"){
        parent.classList.add("shadow-card")
    }

    if (event.type == "focusout"){
        parent.classList.remove("shadow-card")
    }
    
}

</script>


<style scoped>

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

.content{
    display: flex; 
    flex-direction: column; 
    gap: 18px;
}


.choice{
    display: flex;
    justify-content: space-between;
    gap: 10px;
    
}

.choice > label{
    width: 50%;
    min-height: 48px;
    max-height: 68px;
    height: 68px;
    overflow: hidden;
    background-color: var(--gray-color);
    display: flex;
    border-radius: 10px;
    justify-content: space-between;
    position: relative;
    
    transition: 0.1s;
    
}

.choice > label > label{
    margin-top: 10px;
    margin-left: 10px;
}


input[type="radio"] {
    position: fixed;
    opacity: 0;
    pointer-events: none;
}

input[type="checkbox"] {
    position: fixed;
    opacity: 0;
    pointer-events: none;
}


.fields{
    display: flex;
    flex-direction: row;
    gap: 50px;
}


.price-vars{
    display: inline-flex;
    justify-content: space-between;
}

.input-price{
    height: 8px;
    background-color: transparent;
    border-color: var(--gray-color);
    border-bottom: 3px solid var(--gray-color);
    width: 48px;
    text-align: center;
}

.input-price:focus{

    border-color: inherit;
    border-bottom: 3px solid var(--gray-color);
    outline: none;
    
}

.price{
    display: flex;
    flex-direction: column;
}

.group > select:focus{
    outline: none !important;
}

.group > select > option{
    background-color: inherit;
}


.therapists-results{
    width: 100%;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 7px;
    overflow: hidden;
    padding-bottom: 25px;
    flex-wrap: wrap;
    justify-content: space-evenly;

}

.calendar-card{
    width: 100%;
    background-color: white;
    padding: 25px;
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


@media all and (max-width: 725px){
    .fields{
        flex-direction: column;
        gap: 20px;
    }


}




@media all and (max-width: 425px){
    
    .choice{
        flex-direction: column;
    }

    .choice > label{
        width: 100%;
    }

    .therapists-results{
        grid-template-columns: repeat(1, 1fr);
    }

}

</style>