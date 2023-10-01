<template>
    <form method="post" :onSubmit="authorize" class="auth-form card shadow-card">
        <h2 v-if="!createAccount" ref="auth_text">Войти</h2>
        <h2 v-else ref="auth_text">Создать аккаунт</h2>
        <span class="text-small bold btn-back" @click="exit">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-x-lg" viewBox="0 0 16 16">
                <path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8 2.146 2.854Z"/>
            </svg>
        </span>

        <div class="group">
            <label for="username" class="bold">Почта</label>
            <input name="username" id="username" class="text-small bold" placeholder="example@pomogu.su" type="email"
                ref="username" autocomplete="username" minlength="3" required>
        </div>
        <div class="group">
            <label for="username" class="bold">Пароль</label>
            <div class="password-wrap">
                <input name="password" id="password" class="text-small bold" placeholder="пароль" :type="showPassword ? 'text' : 'password'"
                    ref="password" autocomplete="current-password" minlength="8" required>
                
                <span class="password-eye" @mousedown="showPassword = true" @mouseup="showPassword = false" @mouseleave="showPassword = false" @touchstart.passive="showPassword=true" @touchend.passive="showPassword = false" @touchmove.passive="showPassword=false" tabindex="0">
                    <svg v-if="!showPassword" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><path d="M38.8 5.1C28.4-3.1 13.3-1.2 5.1 9.2S-1.2 34.7 9.2 42.9l592 464c10.4 8.2 25.5 6.3 33.7-4.1s6.3-25.5-4.1-33.7L525.6 386.7c39.6-40.6 66.4-86.1 79.9-118.4c3.3-7.9 3.3-16.7 0-24.6c-14.9-35.7-46.2-87.7-93-131.1C465.5 68.8 400.8 32 320 32c-68.2 0-125 26.3-169.3 60.8L38.8 5.1zM223 149.5c48.6-44.3 123-50.8 179.3-11.7c60.8 42.4 78.9 123.2 44.2 186.9L408 294.5c8.4-19.3 10.6-41.4 4.8-63.3c-11.1-41.5-47.8-69.4-88.6-71.1c-5.8-.2-9.2 6.1-7.4 11.7c2.1 6.4 3.3 13.2 3.3 20.3c0 10.2-2.4 19.8-6.6 28.3L223 149.5zm223.1 298L83.1 161.5c-11 14.4-20.5 28.7-28.4 42.2l339 265.7c18.7-5.5 36.2-13 52.6-21.8zM34.5 268.3c14.9 35.7 46.2 87.7 93 131.1C174.5 443.2 239.2 480 320 480c3.1 0 6.1-.1 9.2-.2L33.1 247.8c-1.8 6.8-1.3 14 1.4 20.5z"/></svg>
                    <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"> <path d="M288 32c-80.8 0-145.5 36.8-192.6 80.6C48.6 156 17.3 208 2.5 243.7c-3.3 7.9-3.3 16.7 0 24.6C17.3 304 48.6 356 95.4 399.4C142.5 443.2 207.2 480 288 480s145.5-36.8 192.6-80.6c46.8-43.5 78.1-95.4 93-131.1c3.3-7.9 3.3-16.7 0-24.6c-14.9-35.7-46.2-87.7-93-131.1C433.5 68.8 368.8 32 288 32zM144 256a144 144 0 1 1 288 0 144 144 0 1 1 -288 0zm144-64c0 35.3-28.7 64-64 64c-7.1 0-13.9-1.2-20.3-3.3c-5.5-1.8-11.9 1.6-11.7 7.4c.3 6.9 1.3 13.8 3.2 20.7c13.7 51.2 66.4 81.6 117.6 67.9s81.6-66.4 67.9-117.6c-11.1-41.5-47.8-69.4-88.6-71.1c-5.8-.2-9.2 6.1-7.4 11.7c2.1 6.4 3.3 13.2 3.3 20.3z"/></svg>
                </span>
            </div>
        </div>

        <div class="group" v-if="createAccount">
            <label for="name" class="bold">Имя</label>
            <input name="name" id="name" class="text-small bold" placeholder="Ваше имя" type="text"
                ref="name" autocomplete="given-name" 
                pattern="^[A-Za-zА-Яа-я]+(?:\s+[A-Za-zА-Яа-я]+)*$" title="Буквы кириллицы или латиницы без цифр и пробелов в начале" required>
        </div>

        <div class="group"  v-if="createAccount">
            <label for="birthday" class="bold">Дата рождения</label>
            <input name="birthday" id="birthday" class="text-small bold" type="date"
                ref="birthday" autocomplete="b-day" max-value="" required>
        </div>

        <div class="btn-group">
            <button v-if="!createAccount" class="btn btn-primary text-small bold" type="submit" name="login">Войти</button>
            <button v-else class="btn btn-secondary text-small bold" type="reset" @click.prevent="createAccount = false">Назад</button>
            <button v-if="!createAccount" class="btn btn-secondary text-small bold" type="button" @click.prevent="createAccount = true">Зарегистрироваться</button>
            <button v-else class="btn btn-primary text-small bold" type="submit" name="register">Создать аккаунт</button>
        </div>
        <label class="text-small">{{ error_message }}</label>
    </form>
</template>

<style scoped>
.btn-back {
    position: fixed !important;
    top: 0;
    right: 0;
    height: 48px !important;
    width: 48px !important;
    background-color: var(--primary-light-color);
    text-align: center;
    align-items: center;
    display: flex;
    justify-content: center;
    border-bottom-left-radius: 5px;
    cursor: pointer;
    transition: 0.5s;
}

.btn-back:hover{
    background-color: var(--primary-color);
    transition: 0.3s;
}

.auth-form>.group, .btn {
    width: 100%;
}

#password{
    flex-grow: 1;
}

.password-wrap{
    display: flex;
    align-items: center;
    gap: 10px;
    background-color: var(--gray-color);
    border-radius: 10px;
}

.password-eye{
    height: 32px;
    aspect-ratio: 1/1;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-right: 15px;
}

.password-eye > svg{
    margin: auto;
    display: flex;
    justify-content: center;
    align-items: center;
}

.auth-form {
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 15px;
}

</style>

<script setup lang="ts">
import { ref } from 'vue';
import {login, register} from '../api.js'


const emit = defineEmits(['onExit'])

let createAccount: Boolean = ref(false)
let showPassword: Boolean = ref(false)

const reset: Boolean = ref(false)

const username: any = ref(null)
const password: any = ref(null)
const birthday: any = ref(null)
const name: any = ref(null)

let error_message: any = ref("")

const error_translate = { "LOGIN_BAD_CREDENTIALS": "Ой-ой. Похоже вы ошиблись в почте или пароле, пожалуйста проверье их написание!", 
"LOGIN_USER_NOT_VERIFIED": "Ой-ой. Пользователь не подтвержден. Пожалуйста, проверье свой почтовый ящик.", "REGISTER_INVALID_PASSWORD": "Пароль должен быть больше 3 символов!",
"REGISTER_USER_ALREADY_EXISTS": "Такой пользователь уже существует."}

async function exit() {
    error_message.value = "";
    username.value.value = "";
    password.value.value = "";


    if (name.value != null){
        name.value.value = ""; 
        birthday.value.value = "";
    }

    createAccount.value = false;

    emit("onExit");
}

async function authorize(event: any) {
    event.preventDefault()

    error_message.value = "";

    switch (event.submitter.name) {
        case "login":
            await do_login()
            break

        case "register":
            await do_register()
            break
    }

}


async function do_login() {
    const result = await login(username.value.value, password.value.value)
    check_result(result)

}

async function do_register() {
    const result = await register(username.value.value, password.value.value, name.value.value, birthday.value.value)
    check_result(result)
}

async function check_result(result) {

    if (!result?.ok) {
        let answer = await result.json()
        let ansewr_detail: String = answer.detail
        error_message.value = error_translate[ansewr_detail]
    }else{
        exit();
        location.reload();
    }
}

</script>
