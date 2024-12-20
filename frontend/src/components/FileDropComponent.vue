<script setup lang = "ts">
import { ref, watch } from "vue";

defineProps<{
  filename: string;
}>();

//reactive state for tracking drag-and-drop-status
const isDragging = ref(false);
const isDropped = ref(false);
const droppedFileName = ref("upload file here");
const imagePreviewUrl = ref<string | null>(null);


//event handlers
function onDragEnter(event: DragEvent): void{
    event.preventDefault();
    isDragging.value = true;
}

function onDragOver(event: DragEvent): void{
    event.preventDefault();
    isDragging.value = true;
}

function onDragLeave(event: DragEvent): void{
    isDragging.value = false;
}

function onDrop(event: DragEvent): void{
    event.preventDefault();
    isDragging.value = false;
    isDropped.value = true;
    
    const files = event.dataTransfer?.files;
    if(files && files.length >0){
        const file = files[0];

        if(file.type.startsWith("image/")){
            imagePreviewUrl.value = URL.createObjectURL(file);

        }
        else{
            alert("Please drop a valid image file");
        }
        droppedFileName.value = file.name;
    }
}

//cleanup object URL to avoid memory leaks
watch(imagePreviewUrl,(newUrl, oldUrl)=> {
    if(oldUrl){
        URL.revokeObjectURL(oldUrl);
    }
});

</script>

<template>
    <div class="file-upload-box"
         @dragenter="onDragEnter"
         @dragover="onDragOver"
         @dragleave="onDragLeave"
         @drop="onDrop">
      <div
        id="upload-box-inset"
        :class="{'drag-over': isDragging, 'dropped': isDropped}"
      >
        <div class = "preview-container">
            <!---Image preview-->
            <img v-if="imagePreviewUrl" :src="imagePreviewUrl" alt="Image preview" class="image-preview" />
            <!----file name-->
            <p class = "filename">{{droppedFileName}}</p>
        </div>
      </div>
    </div>
  </template>



<style>

.file-upload-box{
    display: flex; 
    justify-content: center; 
    align-items: center; 
}

#upload-box-inset{
    border: 4px dashed rgb(99, 99, 99); 
   
    border-radius: 15px;
    display: flex;
    background-color: rgba(128, 128, 128, 0.573);
    border-radius: 15px;
    height: 90%;
    width: 90%;
    text-align: center;
    justify-content: center;
    align-items: center;
    transition: 0.2s ease-in-out;
}

/*drag and drop styling*/

#upload-box-inset.drag-over {
    background-color: rgba(94, 94, 94, 0.573); 
    transform: scale(0.95);
}


#upload-box-inset.dropped {
    background-color: rgba(103, 103, 103, 0.573); 
    transform: scale(0.98);
}


.preview-container{
    display: flex;
    flex-direction: column;
    align-items: center;
}

.image-preview{
    max-width: 150px;
    max-height: 150px;
    margin-bottom: 8px;
    border-radius: 5px;
    object-fit: cover;
    
}

.filename{
    font-size: 14px;
    text-align: center;
    margin: 0;
}



</style>