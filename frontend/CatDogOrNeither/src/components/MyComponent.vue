<script setup lang="ts">
defineProps<{
  test: string;
}>();
</script>

<template>
  <div class="container">
    <div id="upload-side">
        <div class = "file-upload-box">
            file-upload-box here
        </div>
    </div>
    <div id="result-side">
        <div class = "result-box"> result box here</div>
    </div>
  </div>
</template>

<style scoped>
/* Ensure the container fills the parent fully */
.container {
  display: flex; /* Flexbox for horizontal layout */
  width: 100%; /* Full width of the parent container */
  height: 100%; /* Full height of the parent container */
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Green div on the left */
#upload-side {
  flex: 1; /* Occupy half the space */
  background-color: green;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Red div on the right */
#result-side {
  flex: 1; /* Occupy the other half */
  background-color: red;
  display: flex;
  justify-content: center;
  align-items: center;
}

.file-upload-box, .result-box{
    background-color: lightgray;
    border-radius: 15px;
    height:40vh;
    width: 15vw;
}
</style>
