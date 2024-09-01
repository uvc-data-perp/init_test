<template>
  <div class="node-editor" @mousemove="onMouseMove" @mouseup="onMouseUp">
    <div class="toolbar">
      <button v-for="item in availableNodes" :key="item.id" @click="addNode(item)">
        {{ item.name }}
      </button>
    </div>
    <div class="editor-area">
      <Node
        v-for="node in nodes"
        :key="node.id"
        :data="node"
        :x="node.x"
        :y="node.y"
        @startConnection="startConnection"
      />
      <svg class="connections">
        <path
          v-for="connection in connections"
          :key="connection.id"
          :d="getPathD(connection)"
          fill="none"
          stroke="#666"
          stroke-width="2"
        />
      </svg>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Node from './Node.vue'

const availableNodes = ref([
  { id: 1, name: '결측치 처리' },
  { id: 2, name: '이상치 처리' },
  { id: 3, name: '정규화' },
  { id: 4, name: '인코딩' }
])

const nodes = ref([])
const connections = ref([])
const connectingInfo = ref(null)

const addNode = (item) => {
  nodes.value.push({
    id: Date.now(),
    name: item.name,
    x: Math.random() * 500,
    y: Math.random() * 300
  })
}

const startConnection = ({ event, type, nodeId }) => {
  connectingInfo.value = { type, nodeId, startX: event.clientX, startY: event.clientY }
}

const onMouseMove = (event) => {
  if (connectingInfo.value) {
    // 여기서 연결선을 그리는 로직을 구현
  }
}

const onMouseUp = (event) => {
  if (connectingInfo.value) {
    // 여기서 연결을 완료하는 로직을 구현
    connectingInfo.value = null
  }
}

const getPathD = (connection) => {
  // 여기서 연결선의 path를 계산
  return `M ${connection.startX} ${connection.startY} L ${connection.endX} ${connection.endY}`
}
</script>

<style scoped>
.node-editor {
  width: 100%;
  height: 600px;
  position: relative;
  border: 1px solid #ccc;
}
.toolbar {
  padding: 10px;
  background-color: #f0f0f0;
}
.editor-area {
  position: relative;
  height: calc(100% - 50px);
}
.connections {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}
</style>
