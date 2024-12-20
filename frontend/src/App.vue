<script setup lang="ts">
import MyComponent from './components/MyComponent.vue';
</script>

<template>
  <div id="app">
    <MyComponent test="hello World!" />
  </div>
</template>

<style>
html, body {
  margin: 0;
  padding: 0;
  width: 100vw; /* Full width of the viewport */
  height: 100vh; /* Full height of the viewport */
  box-sizing: border-box;
}

#app {
  display: flex; /* Flexbox for child alignment */
  width: 100%; /* Full width of the viewport */
  height: 100%; /* Full height of the viewport */
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
</style>

