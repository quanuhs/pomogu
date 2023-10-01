<template>
    <div class="therapist-card shadow-card">
        <label>
            <img class="therapist-image" :src="avatar">
        </label>
    
        <div class="therapist-card-content">

            <div class="therapist-methods text-small bold">
                <label v-for="method in methods">{{ method.name }}</label>
            </div>
            
            <h2 class="bold">{{ name }}</h2>

            <div class="therapist-work">
                <label v-if = "tags == undefined || tags.length == 0">Пока пусто</label>
                <ul v-else class="therapist-work-grid text-small">
                    <li v-for="tag in tags">{{ tag.name }}</li>
                </ul>
            </div>

            <label class="therapist-description" v-if = "description == undefined || description.length == 0">Терапевт пока не заполнил описание</label>
            <label class="therapist-description" v-else>{{ description }}</label>
            <h2 class="therapist-price bold">{{ price }} ₽</h2>
            <div class="therapist-btn-group">

                <a v-if="authorised" class="btn btn-primary bold" :href=therapist_sign_link target="_blank">Записаться</a>
                <a v-else class="btn btn-primary bold" @click.prevent()>Записаться</a>
                <a class="btn btn-secondary bold" :href=therapist_link>Подробнее</a>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import {authorised} from '../api.js'

const props = defineProps({
    id: {type: String, required: true},
    methods: {type: Array<String>, required: true},
    tags: {type: Array<String>, required: true},
    name: {type: String, required: true},
    description: {type: String, required: true},
    price: {type: Number, required: true},
    avatar: {type: String, required: true}
})

const therapist_sign_link = ref("/sign/"+props.id)
const therapist_link = ref("/profile/"+props.id)


</script>

<style scoped>

.therapist-work{
    height: 100px;
    background-color: var(--gray-color);

    border-radius: 10px;
    padding: 10px 20px 10px 20px;
    text-align: justify;
    justify-content: center;
    align-items: center;
    display: flex;
    flex-direction: column;

    overflow-wrap: break-word;
    overflow: hidden;


}


.therapist-work-grid{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 7px;
    width: 100%;
}


.therapist-card{
    min-width: 200px;
    width: 100%;
    max-height: 860px;
    background-color: white;
    border-radius: 10px;
    overflow: hidden;
    padding-bottom: 35px;
    height: fit-content;
}

.therapist-image{
    width: 100%;
    height: 250px;
    object-fit: cover;
    object-position: center;
    background-color: var(--primary-light-color);
}

.therapist-card-content{
    padding: 20px;
    text-align: justify;
    display: flex;
    flex-direction: column;
    gap: 27px;
}

.therapist-methods{
    display: flex;
    flex-direction: row;
    gap: 7px;
    flex-wrap: wrap;
    max-height: 24px;
    height: 24px;
    align-items: center;
    overflow: hidden;
}

.therapist-methods > label{
    border: 1;
    padding: 2px 16px;
    border: 1px solid #171717;
    border-radius: 40px;
}

.therapist-price{
    align-self: center;
    text-align: center;
}

.therapist-btn-group{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 10px;
}

.therapist-btn-group > a{
    width: 80%;

}

.therapist-description{
    height: 140px;
    max-height: 140px;
    overflow-y:hidden;
    text-overflow: ellipsis;
    line-height: 20px;
}

.therapist-work > li {
    list-style-type: none; /* Убираем маркеры */
}

.therapist-work > ul {
    margin-left: 0; /* Отступ слева в браузере IE и Opera */
    padding-left: 0; /* Отступ слева в браузере Firefox, Safari, Chrome */
    list-style-type: none;
}

</style>