<template>
    <div class="profile content">
        
        <div class="btn-profile">
            <button v-if="therapist.error == undefined" class="btn btn-secondary bold text">Профиль психолога</button>
            <button class="btn btn-primary bold text" @click="do_logout();">Выйти</button>
        </div>


        <div class="profile-info card shadow-card">
            <img class="avatar" draggable="false" :src="info.avatar_url" :alt="'Аватар\n'+name">
            <div class="profile-info-description">
                <h2 class="bold">{{name}}</h2>
                <label class="text-small">{{info.email}}</label>
                <div class="profile-info-birthday">
                    <label>{{ year_birth }} года рождения</label>
                    <label>{{ age }}</label>
                </div>
            </div>
        </div>



        <div class="my-sessions card shadow-card">
            <div class="my-sessions-header">
                <h2 class="bold">Мои сессии</h2>
                <div class="my-sessions-switch">
                    <button :class="{'btn-primary': !lookingHistory, 'btn-secondary': lookingHistory}" class="btn text-small bold" @click="showHistory(false)">Предстоящии</button>
                    <button :class="{'btn-secondary': !lookingHistory, 'btn-primary': lookingHistory}" class="btn text-small bold" @click="showHistory(true)">История посещений</button>
                </div>
            </div>
            <div class="my-sessions-body">
            
                <Session v-for="session in sessions"
                :name="session.therapist.name"
                :therapist_id="session.therapist.id"
                :avatar_url="session.therapist.avatar_url"
                :connect_link="session.connect_link"
                :starts_at="new Date(session.starts_at)"
                :alone="session.alone"
                :young="session.young"
                :adult="session.adult"
                :status="session.status"
                :allow_cancel="session.allow_cancel"
                />


                <div v-if="!lookingHistory" class="my-session-empty">
                    <h2 v-if="sessions.length === 0" class="">Нет предстоящих записей</h2>
                    <h2 v-else>Больше записей нет</h2>
                    <a class="btn btn-secondary bold" href="search">Перейти в каталог</a>
                </div>

                <div v-if="sessions.length === 0 && lookingHistory" class="my-session-empty">
                    <h2>Вы ещё не записывались</h2>
                    <a class="btn btn-secondary bold" href="search">Перейти в каталог</a>
                </div>



            </div>
        </div>


    </div>
</template>

<script setup lang="ts">

    import { ref, reactive, computed, defineAsyncComponent} from 'vue';
    import {logout, getMyProfile, getTherapistProfile, getMySessions} from '../api';
    
    const Session = defineAsyncComponent(() => import('../components/Session.vue'));
    

    const info = reactive(await getMyProfile());
    const therapist = reactive(await getTherapistProfile())

    const year_birth = computed(() => {
        return new Date(info.birthday).getFullYear()
    })

    const age = computed(() => {
        // return Date.parse(info.date_of_birth).getYear()
        let cases = [2, 0, 1, 1, 1, 2];
        let number = new Date().getFullYear() - new Date(info.birthday).getFullYear();
        let titles = ['год', 'года', 'лет'];

        return `${number} ${titles[ (number%100>4 && number%100<20)? 2 : cases[(number%10<5)?number%10:5] ]}`
        
        
    })


    
    const name = computed(() => {
        if (info.name == null)
            return "Неизвестный"
        return info.name
    })

    let lookingHistory: any = ref(false);

    
    let sessions:any = ref({})
    let ongoin_sessions = await getMySessions(false)
    let history_sessions = await getMySessions(true)
    
    async function do_logout() {
        await logout();
        location.reload();
    }

    
    async function showHistory(toShow: Boolean) {
        lookingHistory = toShow

        if (lookingHistory){
            sessions.value = history_sessions
        }else{
            sessions.value = ongoin_sessions
        }
    }



    showHistory(false)

</script>

<style scoped>

.my-sessions-header{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
}

.my-sessions-switch{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
}

.my-sessions-body{
    position: relative;
    overflow-y: auto;
    background-color: var(--gray-color);


    background-image: url("/draw.png");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: bottom right, 50%, 50%;

    height: 100%;
    border-radius: 10px;
}

.my-sessions-body{
    position: relative;
    overflow: unset;
    background-color: var(--gray-color);

    background-image: url("/flower.png"), url("/lamp.png");
    background-repeat: no-repeat, no-repeat;
    background-size: auto;
    background-position: bottom left, bottom right;

    height: 100%;
    border-radius: 10px;
}



.my-session-empty{
    height: 100%;
    display: flex;
    gap: 25px;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 50px;
    text-align: center;
}

.my-session-empty > .btn{
    width: 80%;
    max-width: 500px;
}

.my-sessions-switch > .btn{
    width: 100%;
    max-width: 250px;
}

.my-sessions{
    height: 55vh;
    max-height: 800px;
    background-color: var(--gray-color);
}

.my-sessions{
    height: 100%;
    max-height: 100%;
    background-color: var(--gray-color);
}

@media all and (max-width: 580px){
    .my-sessions-header{
        flex-direction: column;
        gap: 20px;
        padding: 25px;
    }

    .my-sessions{
        padding: 0px;
        height: fit-content;
    }

    .my-sessions-body{
        background-position: bottom left -10%;
        background-image: url("/flower.png");
    }

}


.btn-profile{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
}

.btn-profile>*:last-child{
    margin-left: auto;
}

.btn-profile > .btn{
    width: 285px;
    background-color: white;
    border-color: white;
}

.avatar {
    position: relative;
    left: 0;
    top: 0;
    aspect-ratio: 1 / 1;
    height: calc(100% + 25px * 2);
    background-color: var(--primary-light-color);
    object-fit: cover;
    object-position: center;
    vertical-align: middle;

    margin:-25px
    
  }

.profile-info-birthday{
    margin-top: 25px;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    width: 100%;
}

.profile{
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    gap: 15px;
}


.profile-info-description{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex-grow: 1;
    text-align: center;

}

.profile-info{
    position: relative;
    display: flex;
    flex-direction: row;
    height: calc(180px - 25px*2);
    overflow: hidden;
    
}


.profile-contact{
    display: flex;
    flex-direction: column;
    background-color: var(--gray-color);
}


@media all and (max-width: 580px){
    .profile-info{
        height: 300px;
        flex-direction: column-reverse;
    }

    .avatar{
        height: 70px;
        width: calc(100% + 25px*2);
        aspect-ratio: unset;
        left: unset;
        top: unset;
        margin: -25px;
        flex-grow: 1;
        object-position: top;
    }
    
    .profile-info-description{
        flex-grow: 0;
        margin-bottom: 25px;
    }

    .profile-info-birthday{
        flex-direction: column;
        text-align: center;
    }

    .btn-profile{
        flex-direction: row;
        justify-content: center;
        align-items: center;
        gap: 10px;
    }

    .btn-profile > .btn{
        margin: 0px;
    }
}



</style>