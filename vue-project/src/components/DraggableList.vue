<template>
  <div>
    <h3>전처리 단계</h3>
    <div
      v-for="item in items"
      :key="item.id"
      class="drag-item"
      draggable="true"
      @dragstart="onDragStart($event, item)"
    >
      {{ item.name }}
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const items = ref([
  { id: 1, name: '결측치 처리' },
  { id: 2, name: '이상치 처리' },
  { id: 3, name: '정규화' },
  { id: 4, name: '인코딩' }
])

const onDragStart = (event, item) => {
  event.dataTransfer.setData('application/json', JSON.stringify(item))
}
</script>

<style scoped>
.drag-item {
  padding: 10px;
  background-color: #f1f1f1;
  border: 1px solid #ddd;
  margin-bottom: 5px;
  cursor: move;
}
</style>
