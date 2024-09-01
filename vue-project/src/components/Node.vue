<template>
  <div class="node" :style="{ left: x + 'px', top: y + 'px' }">
    <div class="node-header">{{ data.name }}</div>
    <div class="node-content">
      <!-- 여기에 노드 특정 컨텐츠 -->
    </div>
    <div class="node-ports">
      <div class="port input" @mousedown="startConnection($event, 'input')"></div>
      <div class="port output" @mousedown="startConnection($event, 'output')"></div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue'

const props = defineProps(['data', 'x', 'y'])
const emit = defineEmits(['startConnection'])

const startConnection = (event, type) => {
  emit('startConnection', { event, type, nodeId: props.data.id })
}
</script>

<style scoped>
.node {
  position: absolute;
  width: 150px;
  background-color: #f0f0f0;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
}
.node-header {
  font-weight: bold;
  margin-bottom: 5px;
}
.node-ports {
  display: flex;
  justify-content: space-between;
}
.port {
  width: 10px;
  height: 10px;
  background-color: #333;
  border-radius: 50%;
  cursor: pointer;
}
</style>
