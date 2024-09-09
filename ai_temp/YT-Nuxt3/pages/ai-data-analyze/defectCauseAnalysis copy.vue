<template>
  <NuxtLayout name="default">
    <el-scrollbar max-height="100vh">
      <div class="container">
        <header
          class="el-header bg flex animate-fade-in items-center justify-center rounded-b-3xl transition duration-250 wp-100"
        >
          <div class="flex ~ gap3 mr-1 text-xl wp-95">
            <div class="flex items-center justify-center">
              불량원인 데이터 분석
            </div>
          </div>
        </header>

        <main class="el-main" id="el-main">
          <div class="nav-list">
            <EquipsList
              v-if="!isUploaded"
              @equipSelected="handleEquipSelected"
            />
            <DefectsList
              @defectSelected="handleDefectSelected"
              v-if="isUploaded"
            ></DefectsList>
          </div>
          <UploadDialogue
            v-if="isSelectedEquip && !isUploaded"
            :data="selectedData"
            @emitIsUploaded="handleIsUploaded"
          />

          <!-- 업로드 이후 표시되는 메인 영역 -->
          <div v-if="isUploaded" flex overflow-y-hidden>
            <!-- 메인영역 왼쪽 이미지 및 칼럼 -->
            <div class="inspection-left" wp-30 flex flex-col gap-10>
              <!-- 이미지 영역 -->
              <ObjectImg />
              <!-- 칼럼영역 -->
              <div class="ColumnList" flex-grow>
                <ScrollbarEl :data="filteredColumnListInfo"></ScrollbarEl>
              </div>
            </div>
            <!-- 메인 우측  -->
            <div
              v-if="isSelectedDefect"
              class="inspection-right"
              flex
              flex-wrap
              gap-4
              wp-70
              overflow-y-hidden
            >
              <div w-full>
                <div flex justify-end>
                  <button btn>
                    <div class="i-ic:round-plus w-1em h-1em"></div>
                  </button>
                </div>
                <div>
                  <!-- <div v-for="(component, index) in components" :key="index">
                    <component :is="component.type" v-bind="component.props" />
                  </div> -->

                  <div v-for="(component, index) in components" :key="index">
                    <component
                      :is="component.type"
                      v-bind="component.props"
                      :chartData="chartData"
                    />
                  </div>
                </div>

                <MultiClassScatterPlot
                  :chartData="processedChartData"
                  :initialThresholds="[33, 66]"
                  :xAxisField="xAxisField"
                  :yAxisFields="yAxisFields"
                />

                <!-- <div>
                  <div v-for="(component, index) in components" :key="index">
                    <component :is="component.type" v-bind="component.props" />
                  </div>
                  <el-button @click="addComponent">Add Component</el-button>
                </div> -->

                <div>
                  <!-- <h2>Grafana</h2> -->
                  <iframe
                    src="http://158.247.200.126:3000/d-solo/cdx1zqzt0p69sd/new-dashboard?orgId=1&panelId=1"
                    wp-100
                    height="400"
                    frameborder="0"
                  ></iframe>
                  <!-- <GrafanaEmbed panelId="1" width="100%" height="300" /> -->
                </div>
              </div>

              <!-- <template v-for="i in 5" :key="i">
              <component
                :is="`Graph${i}`"
                class="w-full md:w-1/2 mb-4"
              ></component>
            </template> -->

              <!--
              Graph1, Graph2, Graph3, ... , Graph5 컴포넌트를 생성하여
              위의 템플릿에서 사용할 수 있도록 한다.
            --></div>
          </div>
        </main>
      </div>
    </el-scrollbar>
  </NuxtLayout>
</template>

<script setup>
// import { ref } from "vue";
import ChartBuilder from "~/components/ChartBuilder.vue";
import MultiClassScatterPlot from "~/components/MultiClassScatterPlot.vue";

const treeData = ref([]);
const selectedData = ref(null);
const isSelectedEquip = ref(false);
const isSelectedDefect = ref(false);
const selectedIndex = ref([
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
  23, 24, 25, 26,
]);

const ColumnListInfo = ref([
  // {
  //   index: "No",
  //   "varName": "변수",
  //   "varType": "데이터 타입",
  //   "description": "설명",
  // },
  {
    index: 1,
    varName: "No_Shot",
    varType: "int64",
    description: "Shot 번호",
  },
  {
    index: 2,
    varName: "Machine_Cycle_Time",
    varType: "float64",
    description: "기계 사이클 타임",
  },
  {
    index: 3,
    varName: "Cycle_Time",
    varType: "float64",
    description: "사이클 타임",
  },
  {
    index: 4,
    varName: "Barrel_Temp_Z1",
    varType: "float64",
    description: "배럴 온도",
  },
  {
    index: 5,
    varName: "Barrel_Temp_Z2",
    varType: "float64",
    description: "배럴 온도",
  },
  {
    index: 6,
    varName: "Barrel_Temp_Z3",
    varType: "float64",
    description: "배럴 온도",
  },
  {
    index: 7,
    varName: "Barrel_Temp_Z4",
    varType: "float64",
    description: "배럴 온도",
  },
  {
    index: 8,
    varName: "Hopper_Temp",
    varType: "float64",
    description: "호퍼 온도",
  },
  {
    index: 9,
    varName: "Injection_Pressure_Real_Time",
    varType: "float64",
    description: "사출 시간",
  },
  {
    index: 10,
    varName: "Screw_Position",
    varType: "float64",
    description: "스크류 위치",
  },
  {
    index: 11,
    varName: "Injection_Peak_Press",
    varType: "float64",
    description: "사출최대압력",
  },
  {
    index: 12,
    varName: "Max_Injection_Rate",
    varType: "float64",
    description: "최대사출율",
  },
  {
    index: 13,
    varName: "Screw_Velocity",
    varType: "float64",
    description: "스크류 속도",
  },
  {
    index: 14,
    varName: "VP_Time",
    varType: "float64",
    description: "보압 시간",
  },
  {
    index: 15,
    varName: "VP_Position",
    varType: "float64",
    description: "보압절환위치",
  },
  {
    index: 16,
    varName: "Weighing_Start_Position",
    varType: "float64",
    description: "보압시작위치",
  },
  {
    index: 17,
    varName: "VP_Press",
    varType: "float64",
    description: "보압절환압력",
  },
  {
    index: 18,
    varName: "Plasticizing_Time",
    varType: "float64",
    description: "계량시간",
  },
  {
    index: 19,
    varName: "Plasticizing_Start_Position",
    varType: "float64",
    description: "계량시작위치",
  },
  {
    index: 20,
    varName: "Plasticizing_End_Position",
    varType: "float64",
    description: "계량종료위치",
  },
  {
    index: 21,
    varName: "Plasticizing_Screw_Velocity",
    varType: "float64",
    description: "계량스크류속도",
  },
  {
    index: 22,
    varName: "Minimum_Cushion",
    varType: "float64",
    description: "최소쿠션",
  },
  {
    index: 23,
    varName: "Cooling_Time",
    varType: "float64",
    description: "냉각시간",
  },
  {
    index: 24,
    varName: "Back_Flow",
    varType: "float64",
    description: "백플로우",
  },
  {
    index: 25,
    varName: "Decompression_Time",
    varType: "float64",
    description: "석백",
  },
  {
    index: 26,
    varName: "_ID",
    varType: "int64",
    description: "식별정보",
  },
]);

const chartData = ref([
  {
    No_Shot: 0,
    Machine_Cycle_Time: 16.54,
    Cycle_Time: 16.52,
    Barrel_Temp_Z1: 210.2,
    Barrel_Temp_Z2: 200.7,
    Barrel_Temp_Z3: 193.5,
    Barrel_Temp_Z4: 187.3,
    Hopper_Temp: 40.1,
    Injection_Pressure_Real_Time: 1.23,
    Screw_Position: 6.02,
    Injection_Peak_Press: 1211.65,
    Max_Injection_Rate: 78.37,
    Screw_Velocity: 20.6,
    VP_Time: 2,
    VP_Position: 8.14,
    Weighing_Start_Position: 10.51,
    VP_Press: 1062,
    Plasticizing_Time: 4.74,
    Plasticizing_Start_Position: 10.46,
    Plasticizing_End_Position: 63.11,
    Plasticizing_RPM: 28.27,
    Minimum_Cushion: 6.02,
    Cooling_Time: 8,
    Back_Flow: 49.03,
    Decompression_Time: 0.32,
    _ID: 0,
  },
  {
    No_Shot: 1,
    Machine_Cycle_Time: 16.56,
    Cycle_Time: 16.54,
    Barrel_Temp_Z1: 210.2,
    Barrel_Temp_Z2: 200.8,
    Barrel_Temp_Z3: 193.5,
    Barrel_Temp_Z4: 187.2,
    Hopper_Temp: 40.2,
    Injection_Pressure_Real_Time: 1.24,
    Screw_Position: 6.02,
    Injection_Peak_Press: 1211.65,
    Max_Injection_Rate: 78.37,
    Screw_Velocity: 20.6,
    VP_Time: 2,
    VP_Position: 8.14,
    Weighing_Start_Position: 10.51,
    VP_Press: 1062,
    Plasticizing_Time: 4.81,
    Plasticizing_Start_Position: 10.49,
    Plasticizing_End_Position: 63.11,
    Plasticizing_RPM: 28.27,
    Minimum_Cushion: 6.02,
    Cooling_Time: 8,
    Back_Flow: 49.03,
    Decompression_Time: 0.32,
    _ID: 1,
  },
  {
    No_Shot: 2,
    Machine_Cycle_Time: 16.58,
    Cycle_Time: 16.56,
    Barrel_Temp_Z1: 210.1,
    Barrel_Temp_Z2: 200.7,
    Barrel_Temp_Z3: 193.5,
    Barrel_Temp_Z4: 187.2,
    Hopper_Temp: 40.2,
    Injection_Pressure_Real_Time: 1.26,
    Screw_Position: 6.02,
    Injection_Peak_Press: 1209.16,
    Max_Injection_Rate: 78.32,
    Screw_Velocity: 35.38,
    VP_Time: 2,
    VP_Position: 8.12,
    Weighing_Start_Position: 10.54,
    VP_Press: 1101.41,
    Plasticizing_Time: 4.8,
    Plasticizing_Start_Position: 10.53,
    Plasticizing_End_Position: 63.11,
    Plasticizing_RPM: 28.27,
    Minimum_Cushion: 6.02,
    Cooling_Time: 8,
    Back_Flow: 49.03,
    Decompression_Time: 0.32,
    _ID: 2,
  },
  {
    No_Shot: 3,
    Machine_Cycle_Time: 16.62,
    Cycle_Time: 16.58,
    Barrel_Temp_Z1: 210.1,
    Barrel_Temp_Z2: 200.6,
    Barrel_Temp_Z3: 193.5,
    Barrel_Temp_Z4: 187.2,
    Hopper_Temp: 40.2,
    Injection_Pressure_Real_Time: 1.3,
    Screw_Position: 6.28,
    Injection_Peak_Press: 1228.24,
    Max_Injection_Rate: 78.19,
    Screw_Velocity: 36.35,
    VP_Time: 2,
    VP_Position: 8.12,
    Weighing_Start_Position: 10.79,
    VP_Press: 1092.55,
    Plasticizing_Time: 4.84,
    Plasticizing_Start_Position: 10.78,
    Plasticizing_End_Position: 63.11,
    Plasticizing_RPM: 28.27,
    Minimum_Cushion: 6.28,
    Cooling_Time: 8,
    Back_Flow: 49.03,
    Decompression_Time: 0.33,
    _ID: 3,
  },
  {
    No_Shot: 4,
    Machine_Cycle_Time: 16.62,
    Cycle_Time: 16.62,
    Barrel_Temp_Z1: 210,
    Barrel_Temp_Z2: 200.5,
    Barrel_Temp_Z3: 193.4,
    Barrel_Temp_Z4: 187.3,
    Hopper_Temp: 40.1,
    Injection_Pressure_Real_Time: 1.31,
    Screw_Position: 6.46,
    Injection_Peak_Press: 1287.11,
    Max_Injection_Rate: 77.99,
    Screw_Velocity: 46.1,
    VP_Time: 2,
    VP_Position: 8.1,
    Weighing_Start_Position: 10.96,
    VP_Press: 1153.41,
    Plasticizing_Time: 4.86,
    Plasticizing_Start_Position: 10.94,
    Plasticizing_End_Position: 63.11,
    Plasticizing_RPM: 28.27,
    Minimum_Cushion: 6.46,
    Cooling_Time: 8,
    Back_Flow: 49.03,
    Decompression_Time: 0.33,
    _ID: 4,
  },
  {
    No_Shot: 5,
    Machine_Cycle_Time: 16.62,
    Cycle_Time: 16.64,
    Barrel_Temp_Z1: 210,
    Barrel_Temp_Z2: 200.4,
    Barrel_Temp_Z3: 193.4,
    Barrel_Temp_Z4: 187.3,
    Hopper_Temp: 40.1,
    Injection_Pressure_Real_Time: 1.3,
    Screw_Position: 6.43,
    Injection_Peak_Press: 1261.17,
    Max_Injection_Rate: 78.07,
    Screw_Velocity: 47.77,
    VP_Time: 2,
    VP_Position: 8.11,
    Weighing_Start_Position: 10.94,
    VP_Press: 1176.73,
    Plasticizing_Time: 4.87,
    Plasticizing_Start_Position: 10.92,
    Plasticizing_End_Position: 63.11,
    Plasticizing_RPM: 28.27,
    Minimum_Cushion: 6.43,
    Cooling_Time: 8,
    Back_Flow: 49.03,
    Decompression_Time: 0.33,
    _ID: 5,
  },
  {
    No_Shot: 6,
    Machine_Cycle_Time: 16.62,
    Cycle_Time: 16.62,
    Barrel_Temp_Z1: 210,
    Barrel_Temp_Z2: 200.3,
    Barrel_Temp_Z3: 193.3,
    Barrel_Temp_Z4: 187.4,
    Hopper_Temp: 40,
    Injection_Pressure_Real_Time: 1.31,
    Screw_Position: 6.51,
    Injection_Peak_Press: 1276.63,
    Max_Injection_Rate: 78.03,
    Screw_Velocity: 46.78,
    VP_Time: 2,
    VP_Position: 8.11,
    Weighing_Start_Position: 11,
    VP_Press: 1162.02,
    Plasticizing_Time: 4.84,
    Plasticizing_Start_Position: 10.99,
    Plasticizing_End_Position: 63.11,
    Plasticizing_RPM: 28.27,
    Minimum_Cushion: 6.51,
    Cooling_Time: 8,
    Back_Flow: 49.03,
    Decompression_Time: 0.33,
    _ID: 6,
  },
  {
    No_Shot: 7,
    Machine_Cycle_Time: 16.62,
    Cycle_Time: 16.62,
    Barrel_Temp_Z1: 210.1,
    Barrel_Temp_Z2: 200.3,
    Barrel_Temp_Z3: 193.4,
    Barrel_Temp_Z4: 187.5,
    Hopper_Temp: 40,
    Injection_Pressure_Real_Time: 1.3,
    Screw_Position: 6.38,
    Injection_Peak_Press: 1285.61,
    Max_Injection_Rate: 78.17,
    Screw_Velocity: 45.13,
    VP_Time: 2,
    VP_Position: 8.12,
    Weighing_Start_Position: 10.89,
    VP_Press: 1151.92,
    Plasticizing_Time: 4.87,
    Plasticizing_Start_Position: 10.87,
    Plasticizing_End_Position: 63.11,
    Plasticizing_RPM: 28.27,
    Minimum_Cushion: 6.38,
    Cooling_Time: 8,
    Back_Flow: 49.03,
    Decompression_Time: 0.32,
    _ID: 7,
  },
  {
    No_Shot: 8,
    Machine_Cycle_Time: 16.6,
    Cycle_Time: 16.64,
    Barrel_Temp_Z1: 210,
    Barrel_Temp_Z2: 200.4,
    Barrel_Temp_Z3: 193.4,
    Barrel_Temp_Z4: 187.7,
    Hopper_Temp: 39.9,
    Injection_Pressure_Real_Time: 1.31,
    Screw_Position: 6.39,
    Injection_Peak_Press: 1241.21,
    Max_Injection_Rate: 78.11,
    Screw_Velocity: 39.1,
    VP_Time: 2,
    VP_Position: 8.14,
    Weighing_Start_Position: 10.9,
    VP_Press: 1108.89,
    Plasticizing_Time: 4.89,
    Plasticizing_Start_Position: 10.89,
    Plasticizing_End_Position: 63.11,
    Plasticizing_RPM: 28.27,
    Minimum_Cushion: 6.39,
    Cooling_Time: 8,
    Back_Flow: 49.03,
    Decompression_Time: 0.32,
    _ID: 8,
  },
  {
    No_Shot: 9,
    Machine_Cycle_Time: 16.62,
    Cycle_Time: 16.62,
    Barrel_Temp_Z1: 209.9,
    Barrel_Temp_Z2: 200.3,
    Barrel_Temp_Z3: 193.6,
    Barrel_Temp_Z4: 187.9,
    Hopper_Temp: 40,
    Injection_Pressure_Real_Time: 1.32,
    Screw_Position: 6.4,
    Injection_Peak_Press: 1283.99,
    Max_Injection_Rate: 78.17,
    Screw_Velocity: 45.59,
    VP_Time: 2,
    VP_Position: 8.12,
    Weighing_Start_Position: 10.9,
    VP_Press: 1149.05,
    Plasticizing_Time: 4.93,
    Plasticizing_Start_Position: 10.88,
    Plasticizing_End_Position: 63.11,
    Plasticizing_RPM: 28.27,
    Minimum_Cushion: 6.4,
    Cooling_Time: 8,
    Back_Flow: 49.03,
    Decompression_Time: 0.32,
    _ID: 9,
  },
]);

// components 배열 수정
const components = ref([
  {
    type: MultiClassScatterPlot,
    props: { title: "Multi-Class Scatter Plot" },
  },
  {
    type: ChartBuilder,
    props: { title: "Chart Builder" },
  },
]);

const xAxisField = ref("Max_Injection_Rate");
const yAxisFields = ref(["Injection_Pressure_Real_Time", "Screw_Velocity"]);

const processedChartData = computed(() => {
  return chartData.value.map((item) => {
    const result = {
      x: item[xAxisField.value],
      y: yAxisFields.value.map((field) => item[field]),
      classValue: item["No_Shot"], // 분류를 위한 값
    };
    return result;
  });
});

const addComponent = () => {
  // 사용자 입력을 받아 컴포넌트 타입과 props를 결정
  const componentType = prompt(
    "Enter component type (MultiClassScatterPlot or ChartBuilder):"
  );
  const props = {}; // 실제 구현에서는 사용자로부터 props를 입력받을 수 있습니다

  if (componentType === "MultiClassScatterPlot") {
    components.value.push({ type: MultiClassScatterPlot, props });
  } else if (componentType === "ChartBuilder") {
    components.value.push({ type: ChartBuilder, props });
  }
};
const filteredColumnListInfo = computed(() => {
  return ColumnListInfo.value.filter((item) =>
    selectedIndex.value.includes(item.index)
  );
});

const handleEquipSelected = (equip) => {
  isSelectedEquip.value = equip;
};

const handleDefectSelected = (defect) => {
  isSelectedDefect.value = defect;
  selectedIndex.value = [4, 5, 6, 7, 9, 11, 12, 22, 23];
  console.log(selectedIndex.value);
  console.log(filteredColumnListInfo.value);
};

///////////////////////
const dialogVisible = ref(false);
const form = ref({
  chartType: "",
  xAxis: "",
  yAxis: [],
});

const dataFields = computed(() => {
  if (chartData.value.length > 0) {
    return Object.keys(chartData.value[0]);
  }
  return [];
});

const showAddComponentModal = () => {
  dialogVisible.value = true;
};

const handleAddComponent = () => {
  let newComponent;
  const props = {
    data: chartData.value,
    xField: form.value.xAxis,
    yFields: form.value.yAxis,
  };

  switch (form.value.chartType) {
    case "line":
    case "bar":
    case "scatter":
      newComponent = {
        type: ChartBuilder,
        props: { ...props, chartType: form.value.chartType },
      };
      break;
    default:
      newComponent = { type: MultiClassScatterPlot, props };
  }

  components.value.push(newComponent);
  dialogVisible.value = false;
  form.value = { chartType: "", xAxis: "", yAxis: [] };
};
/////////////////////////////////////////////////

const handleIsUploaded = () => {
  isUploaded.value = true;
  console.log("🚀 ~ handleIsUploaded ~ isUploaded:", isUploaded);
};
const isUploaded = ref(false);
const handleNodeClick = (data) => {
  selectedData.value = data;
};
</script>

<style scoped>
/* 필요한 경우 스타일 추가 */
</style>
