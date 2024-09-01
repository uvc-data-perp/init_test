<template>
  <div>
    <v-chart :option="chartOption" style="width: 100%; height: 400px" />
    <div style="display: flex; justify-content: space-between">
      <DraggableList />
      <DropZone />
      <Node></Node>
      <NodeEditor />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import VChart from 'vue-echarts'
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { BarChart } from 'echarts/charts'
import { GridComponent, TooltipComponent } from 'echarts/components'
import DraggableList from './components/DraggableList.vue'
import DropZone from './components/DropZone.vue'

import Node from './components/Node.vue'
import NodeEditor from './components/NodeEditor.vue'

use([CanvasRenderer, BarChart, GridComponent, TooltipComponent])

const chartOption = ref({})

onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:8000/chart-data')
    console.log('Raw response:', response.data)
    chartOption.value = response.data
  } catch (error) {
    console.error('차트 데이터를 불러오는 데 실패했습니다:', error)
    if (error.response) {
      console.error('Error data:', error.response.data)
      console.error('Error status:', error.response.status)
      console.error('Error headers:', error.response.headers)
    } else if (error.request) {
      console.error('Error request:', error.request)
    } else {
      console.error('Error message:', error.message)
    }
  }
})
</script>
