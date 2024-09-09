// components/ChartBuilder.vue
<template>
  <div class="chart-builder">
    <div class="controls">
      <label>
        Chart Type:
        <select v-model="chartType">
          <option value="bar">Bar</option>
          <option value="line">Line</option>
          <option value="pie">Pie</option>
        </select>
      </label>
      <label>
        Title:
        <input v-model="chartTitle" type="text" />
      </label>
      <div v-if="chartType !== 'pie'">
        <label>
          X-Axis Label:
          <input v-model="xAxisLabel" type="text" />
        </label>
        <label>
          Y-Axis Label:
          <input v-model="yAxisLabel" type="text" />
        </label>
      </div>
      <div>
        <h3>Data:</h3>
        <div v-for="(item, index) in chartData" :key="index">
          <input v-model="item.name" placeholder="Category" />
          <input
            v-model.number="item.value"
            type="number"
            placeholder="Value"
          />
          <button @click="removeDataPoint(index)">Remove</button>
        </div>
        <button @click="addDataPoint">Add Data Point</button>
      </div>
    </div>
    <div class="chart-container">
      <ClientOnly>
        <v-chart class="chart" :option="chartOption" />
      </ClientOnly>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";

const chartType = ref("bar");
const chartTitle = ref("My Chart");
const xAxisLabel = ref("X Axis");
const yAxisLabel = ref("Y Axis");
const chartData = ref([
  { name: "Category 1", value: 120 },
  { name: "Category 2", value: 200 },
  { name: "Category 3", value: 150 },
]);

const addDataPoint = () => {
  chartData.value.push({ name: "New Category", value: 0 });
};

const removeDataPoint = (index: number) => {
  chartData.value.splice(index, 1);
};

const chartOption = computed(() => {
  const baseOption = {
    title: {
      text: chartTitle.value,
      left: "center",
    },
    tooltip: {
      trigger: "item",
    },
    legend: {
      orient: "vertical",
      left: "left",
    },
  };

  if (chartType.value === "pie") {
    return {
      ...baseOption,
      series: [
        {
          name: chartTitle.value,
          type: "pie",
          radius: "50%",
          data: chartData.value,
        },
      ],
    };
  } else {
    return {
      ...baseOption,
      xAxis: {
        type: "category",
        data: chartData.value.map((item) => item.name),
        name: xAxisLabel.value,
      },
      yAxis: {
        type: "value",
        name: yAxisLabel.value,
      },
      series: [
        {
          data: chartData.value.map((item) => item.value),
          type: chartType.value,
        },
      ],
    };
  }
});
</script>

<style scoped>
.chart-builder {
  display: flex;
  gap: 20px;
}
.controls {
  width: 300px;
}
.chart-container {
  flex-grow: 1;
}
.chart {
  height: 400px;
  width: 100%;
}
</style>
