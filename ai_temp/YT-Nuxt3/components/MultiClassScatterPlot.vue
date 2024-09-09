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
    <select v-model="selectedChartType">
      <option value="scatter">Scatter</option>
      <option value="line">Line</option>
      <option value="bar">Bar</option>
    </select>
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
import { ScatterChart, LineChart, BarChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent,
  DataZoomComponent,
} from "echarts/components";

// Props 정의
const props = defineProps({
  chartData: {
    type: Array,
    required: true,
  },
  chartConfig: {
    type: Object,
    required: true,
  },
});

let chartInstance = null;

onMounted(() => {
  use([
    CanvasRenderer,
    ScatterChart,
    LineChart,
    BarChart,
    TitleComponent,
    TooltipComponent,
    LegendComponent,
    GridComponent,
    DataZoomComponent,
  ]);
});

const thresholds = ref(props.chartConfig.thresholds || [33, 66]);
const selectedChartType = ref(props.chartConfig.type || "scatter");
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

const chartOption = computed(() => {
  const baseOption = {
    title: {
      text: props.chartConfig.title || "Multi-Class Chart",
    },
    tooltip: {
      trigger: "item",
      formatter: function (params) {
        const index = thresholds.value.findIndex((t) => params.value[2] <= t);
        return `(${params.value[0]}, ${params.value[1]})<br/>Class: ${
          index === -1 ? "Class 1" : `Class ${index + 1}`
        }`;
      },
    },
    xAxis: {
      name: props.chartConfig.xAxisField,
    },
    yAxis: {
      name: props.chartConfig.yAxisFields[0], // 첫 번째 y축 필드 이름
    },
    dataZoom: [
      { type: "inside", xAxisIndex: [0], filterMode: "empty" },
      { type: "inside", yAxisIndex: [0], filterMode: "empty" },
      { type: "slider", xAxisIndex: [0], filterMode: "empty" },
      { type: "slider", yAxisIndex: [0], filterMode: "empty" },
    ],
  };

  return {
    ...baseOption,
    series: [
      {
        symbolSize: 10,
        data: props.chartData.map((item) => ({
          value: item,
          itemStyle: {
            color:
              colors[thresholds.value.findIndex((t) => item[2] <= t) + 1] ||
              colors[0],
          },
        })),
        type: selectedChartType.value,
      },
    ],
  };
});

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
