<template>
    <div>
        HELLO WORLD {{ $route.params.id }}
    </div>
</template>

<script setup lang="ts">

import { useRoute } from 'vue-router';

let route = useRoute()
console.log(route.params.id)

</script>

<style scoped>

</style>