<template>
    <div class="not-found">
        <h1>Ой-ой!<br>Страница не найдена.</h1>
        <h2>Проверьте, правильно ли вы указали URL</h2>
        <a class="btn btn-primary bold" href="/">На главную!</a>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped>

.not-found{
    position: fixed;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    min-width: 300px;
    gap: 25px;
}

</style>