<template>
  <div class="drop-zone" style="">
    <h3>선택된 전처리 단계</h3>
    <div v-for="(step, index) in selectedSteps" :key="step.id" class="drop-item">
      {{ step.name }}
      <button @click="removeStep(step)">X</button>
    </div>
    <div
      class="drop-placeholder"
      @dragover.prevent
      @drop="onDrop($event, selectedSteps.length)"
    ></div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const selectedSteps = ref([])

const removeStep = (step) => {
  const index = selectedSteps.value.findIndex((s) => s.id === step.id)
  if (index !== -1) {
    selectedSteps.value.splice(index, 1)
  }
}

const onDrop = (event, index) => {
  event.preventDefault()
  const itemData = JSON.parse(event.dataTransfer.getData('application/json'))
  selectedSteps.value.splice(index, 0, itemData)
}
</script>

<style scoped>
.drop-zone {
  min-height: 200px;
  border: 2px dashed #ccc;
  padding: 10px;
}
.drop-item {
  padding: 10px;
  background-color: #e1e1e1;
  border: 1px solid #ccc;
  margin-bottom: 5px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.drop-placeholder {
  height: 20px;
  background-color: #f0f0f0;
  margin: 5px 0;
}
</style>
