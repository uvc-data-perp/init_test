<template>
  <div>
    <div v-for="(threshold, index) in thresholds" :key="index">
      <label>Threshold {{ index + 1 }}: </label>
      <input
        v-model.number="thresholds[index]"
        type="range"
        :min="0"
        :max="100"
        step="1"
      />
      <span>{{ threshold }}</span>
    </div>
    <button @click="addThreshold">Add Threshold</button>
    <button @click="removeThreshold" :disabled="thresholds.length <= 2">
      Remove Threshold
    </button>
    <button @click="resetZoom">Reset Zoom</button>
    <ClientOnly>
      <v-chart
        class="chart"
        :option="chartOption"
        autoresize
        @zr:click="onClick"
      />
    </ClientOnly>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import VChart from "vue-echarts";
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { ScatterChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  DataZoomComponent,
} from "echarts/components";

let chartInstance = null;

onMounted(() => {
  use([
    CanvasRenderer,
    ScatterChart,
    TitleComponent,
    TooltipComponent,
    LegendComponent,
    GridComponent,
    DataZoomComponent,
  ]);
});

const thresholds = ref([33, 66]);
const colors = [
  "#c23531",
  "#2f4554",
  "#61a0a8",
  "#d48265",
  "#91c7ae",
  "#749f83",
  "#ca8622",
  "#bda29a",
  "#6e7074",
  "#546570",
];

// 샘플 데이터
const data = [
  [10, 8.04, 30],
  [8, 6.95, 45],
  [13, 7.58, 60],
  [9, 8.81, 75],
  [11, 8.33, 90],
  [14, 9.96, 40],
  [6, 7.24, 55],
  [4, 4.26, 70],
  [12, 10.84, 85],
  [7, 4.82, 50],
  [5, 5.68, 65],
];

const getClass = (value) => {
  for (let i = 0; i < thresholds.value.length; i++) {
    if (value <= thresholds.value[i]) {
      return String.fromCharCode(65 + i); // A, B, C, ...
    }
  }
  return String.fromCharCode(65 + thresholds.value.length);
};

const chartOption = computed(() => ({
  title: {
    text: "Zoomable Multi-Class Dynamic Scatter Plot",
  },
  tooltip: {
    trigger: "item",
    formatter: function (params) {
      return `(${params.value[0]}, ${params.value[1]})<br/>Class: ${getClass(
        params.value[2]
      )}`;
    },
  },
  xAxis: {},
  yAxis: {},
  dataZoom: [
    {
      type: "inside",
      xAxisIndex: [0],
      filterMode: "empty",
    },
    {
      type: "inside",
      yAxisIndex: [0],
      filterMode: "empty",
    },
    {
      type: "slider",
      xAxisIndex: [0],
      filterMode: "empty",
    },
    {
      type: "slider",
      yAxisIndex: [0],
      filterMode: "empty",
    },
  ],
  series: [
    {
      symbolSize: 10,
      data: data.map((item) => ({
        value: item,
        itemStyle: {
          color:
            colors[thresholds.value.findIndex((t) => item[2] <= t) + 1] ||
            colors[0],
        },
      })),
      type: "scatter",
    },
  ],
}));

const addThreshold = () => {
  if (thresholds.value.length < 9) {
    thresholds.value.push(
      Math.floor((thresholds.value[thresholds.value.length - 1] + 100) / 2)
    );
    thresholds.value.sort((a, b) => a - b);
  }
};

const removeThreshold = () => {
  if (thresholds.value.length > 2) {
    thresholds.value.pop();
  }
};

const resetZoom = () => {
  if (chartInstance) {
    chartInstance.dispatchAction({
      type: "dataZoom",
      start: 0,
      end: 100,
    });
  }
};

const onClick = (event) => {
  chartInstance = event.chartInstance;
};
</script>

<style scoped>
.chart {
  height: 400px;
}
</style>
