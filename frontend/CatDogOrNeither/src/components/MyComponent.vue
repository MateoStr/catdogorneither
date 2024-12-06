<script setup lang="ts">
defineProps<{
  test: string
}>()
</script>

<template>
    <h1>{{ test }}</h1>
    <div id = "upload">test</div>
    <div id = "result">test as well</div>
</template>

<style>
    #upload{
        min-width: 30%;
    }
    #result{
        min-width: 30%;
    }
</style>