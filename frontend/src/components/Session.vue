<template>
    <div class="session shadow-card">
        <div class="session-header">
            <div class="session-time"><label class="bold text-small">{{dateAsText}}</label></div>

            <div class="session-header-description">
                <div class="session-format text-small">
                    <div class="session-icon-content">
                        <label>Выбранный формат</label>
                        <ul class="bold">
                            <li v-if="alone == true">Индивидуальный</li>
                            <li v-if="alone == false">Пары / Семьи</li>
                            <li v-if="adult == true">Взрослый</li>
                            <li v-if="young == true">Ребенок / Подросток</li>
                        </ul>
                    </div>
                </div>

                <div class="session-duration text-small">
                    <div class="session-icon-content">
                        <label>Длительность сеанса</label>
                        <ul class="bold">
                            <li>50 минут</li>
                        </ul>
                    </div>
                </div>
            </div>


        </div>
        <div class="session-body">
            <img class="session-avatar" draggable="false" :src="avatar_url" alt="avatar">
            <div class="session-body-description">
                <a :href="profile_url">
                    <h2 class="bold">{{name}}</h2>
                    <label class="text-small">психотеропевт</label>
                </a>

                <a v-if="status=='busy' && starts_at <= new Date()" class="btn btn-primary text bold" :href="connect_link">Подключиться</a>
                <button v-if="status == 'ended'"  class="btn btn-primary text bold" :href="sign_url">Повторить запись</button>
                <button v-if="status=='busy' && allow_cancel == true && starts_at >= new Date()"  class="btn btn-secondary text bold" @click.prevent="cancel_session()">Отменить запись</button>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'


const props = defineProps({
    name: {type: String, required: true},
    therapist_id: {type: String, required: true},
    avatar_url: {type: String, required: true},
    connect_link: {type: String, required: true},
    starts_at: {type: Date, required: true},
    alone: {type: Boolean, required: true},
    young: {type: Boolean, required: true},
    adult: {type: Boolean, required: true},
    status: {type: String, required: true},
    allow_cancel: {type: Boolean, required: true}
})



let profile_url = computed(() => {
    return "/profile/" + props.therapist_id
})

let sign_url = computed(() => {
    return "/sign/" + props.therapist_id
})

let dateAsText = computed(() => {
    let days_as_text = ['вс', 'пн', 'вт', 'ср', 'чт', 'пт', 'сб']
    let month_as_text = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа"]
    
    let date = props.starts_at.getDate()
    let month = props.starts_at.getMonth()
    let day = props.starts_at.getDay()
    let hours = props.starts_at.getHours()
    let minutes = props.starts_at.getMinutes()

    let hours_as_text = ("0"+hours).slice(-2);
    let minutes_as_text = ("0"+minutes).slice(-2);

    return `${date} ${month_as_text[month]} · ${days_as_text[day]} · ${hours_as_text}:${minutes_as_text}`
})


</script>

<style scoped>

.session{
    display: flex;
    flex-direction: row;
    overflow: hidden;
    border-radius: 10px;
    margin: 25px;
}

.session-header{
    background-color: var(--primary-light-color);
    padding: 25px;
    width: 300px;

    display: flex;
    flex-direction: column;
    gap: 20px;
}

.session-time{
    background-color: var(--primary-color);
    padding: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 10px;
}

.session-icon-content{
    display: flex;
    flex-direction: column;
}

.session-icon-content > ul{
    margin: 0px;
}

.session-body{
    flex-grow: 1;
    background: white;
    background: linear-gradient(130deg, rgba(255,231,173,1) 0%, rgba(255,255,255,1) 40%);
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 25px;
    gap: 35px;
}

.session-body-description{
    display: flex;
    flex-direction: column;
    gap: 15px;
    flex-grow: 1;
}

.session-body-description > .btn{
    width: 100%;
    max-width: 300px;
}

.session-avatar {
    object-fit: cover;
    object-position: center;
    width: 180px;
    aspect-ratio: 1/1;
    border-radius: 50%;
    background-color: var(--primary-light-color);
  }

.session-duration{
    margin-top: auto
    
}

.session-header-description{
    display: flex;
    flex-direction: column;
    gap: 25px;
}

.session-body-description > a{
    width: fit-content;
}



@media all and (max-width: 1000px){
    .session{
        flex-direction: column;

    }

    .session-body{
        flex-direction: row;
        justify-content: space-evenly;
        align-items: center;
        background: linear-gradient(180deg, rgba(255,231,173,1) 0%, rgba(255,255,255,1) 40%);
        flex-wrap: wrap;
        gap: 5px;
        padding: 5px;
        padding-bottom: 15px;
    }

    .session-body-description{
        justify-content: center;
        align-items: center;
        text-align: center;
        flex-grow: 0;
        
    }

    .session-body-description{
        width: 100%;
    }

    .session-header{
        width: auto;
    }

    .session-header-description{
        flex-direction: row;
        justify-content: space-between;
    }

    .session-duration{
        margin:0;
    }

    .session-avatar{
        width: 140px;
    }

    

}

@media all and (max-width: 580px){
     .session-header-description{
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .session-duration{
        margin:0;
    }

    .session-icon-content{
        width: 200px;
        text-align: center;
    }

    .session-body{
        padding: 0px;
        flex-wrap: unset;
        flex-direction: column;
    }
    
    .session-body-description > .btn{
        width: 100%;
        max-width: 100%;
        border-radius: 0px;
        border-bottom: 0px;

    }

    ul{
        list-style-type: none;
        padding: 0;
    }

    

    

}

</style>