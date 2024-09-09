<!-- components/SidebarLayout.vue -->
<template>
  <aside
    class="el-aside sidebar"
    :class="{ 'dark:bg-[#181818] light:bg-[#f4f5fa]': true }"
    m-0
    h-screen
    p-0
    hp-100
  >
    <div class="aside-header" relative flex items-center justify-center>
      <a href="/" class="mb-3 mt-2">
        <div flex cursor-default items-center justify-center text-2xl font-300>
          <div m-4 flex flex-col children:mx-auto>
            <div wp-100>
              <span mr-1 text-green-7>CPS</span>
              <span>PORTAL</span>
            </div>
          </div>
        </div>
      </a>
      <div
        right="-2"
        absolute
        top-5
        ml-auto
        h-5
        w-5
        flex
        items-center
        justify-center
        rounded-full
        text-sm
        md:hidden
      >
        <div i-mdi-close md:hidden></div>
      </div>
    </div>
    <el-scrollbar>
      <el-menu :default-active="activeIndex">
        <template v-for="item in menuItems" :key="item.index">
          <el-menu-item
            v-if="!item.children"
            :index="item.index"
            class="w-[300px]"
          >
            <div :class="item.icon" mr-3></div>
            <span>{{ item.title }}</span>
          </el-menu-item>
          <el-sub-menu v-else :index="item.index">
            <template #title>
              <div flex items-center justify-center>
                <div :class="item.icon" mr-3 text-base></div>
                <span>{{ item.title }}</span>
              </div>
            </template>
            <el-menu-item
              v-for="child in item.children"
              :key="child.index"
              :index="child.index"
              class=""
            >
              <NuxtLink :to="child.path" class="flex items-center w-full">
                <div :class="child.icon" class="mr-3 text-2"></div>
                <span class="hover:text-green">{{ child.title }}</span>
              </NuxtLink>
            </el-menu-item>
          </el-sub-menu>
        </template>
      </el-menu>
    </el-scrollbar>
  </aside>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const activeIndex = computed(() => route.path);

interface MenuItem {
  title: string;
  icon: string;
  index: string;
  path: string;
  children?: MenuItem[];
}

const menuItems: MenuItem[] = [
  {
    title: "커스텀 대시보드",
    icon: "i-carbon:cloud-monitoring",
    index: "/dashboard",
    path: "/",
  },
  {
    title: "설비 관리",
    icon: "i-carbon:industry",
    index: "/facility",
    path: "/",
  },
  {
    title: "엣지 관리",
    icon: "i-carbon:edge-node-alt",
    index: "/edge",
    path: "/",
  },
  {
    title: "인증서 관리",
    icon: "i-carbon:edge-node-alt",
    index: "/certification",
    path: "/",
  },
  {
    title: "데이터 수집",
    icon: "i-carbon:data-collection",
    index: "data-collect",
    path: "/",
    children: [
      {
        title: "모델러",
        icon: "i-ic:outline-circle",
        index: "/data-collect/opcua-modeler",
        path: "/",
      },
      // 더 많은 서브 메뉴 아이템들...
    ],
  },
  {
    title: "데이터 조회",
    icon: "i-carbon:data-collection",
    index: "data-retrieve",
    path: "/",
    children: [
      // 서브 메뉴 아이템들...
    ],
  },
  {
    title: "AI 데이터 분석",
    icon: "i-carbon:data-collection",
    index: "ai-data-analyze",
    path: "/",
    children: [
      {
        title: "불량원인 데이터 분석",
        icon: "i-ic:outline-circle",
        index: "/ai-data-analyze/defect-cause-analysis",
        path: "/ai-data-analyze/defectCauseAnalysis",
      },
      // 더 많은 서브 메뉴 아이템들...
    ],
  },
  {
    title: "시스템 관리",
    icon: "i-carbon:data-collection",
    index: "system-management",
    path: "/",
    children: [
      // 서브 메뉴 아이템들...
    ],
  },
];
</script>

<style scoped></style>

<!-- 

<el-scrollbar>
  <el-menu>
    <el-menu-item index="/dashboard">
      <div i-carbon:cloud-monitoring mr-3></div>
      <span>커스텀 대시보드</span>
    </el-menu-item>
    <el-menu-item index="/facility">
      <div i-carbon:industry mr-3></div>
      <span>설비 관리</span>
    </el-menu-item>
    <el-menu-item index="/edge">
      <div i-carbon:edge-node-alt mr-3></div>
      <span>엣지 관리</span>
    </el-menu-item>
    <el-menu-item index="/certification">
      <div i-carbon:edge-node-alt mr-3></div>
      <span>인증서 관리</span>
    </el-menu-item>
    <el-sub-menu index="data-collect">
      <template #title>
        <div flex items-center justify-center>
          <div i-carbon:data-collection mr-3 text-base></div>
          <span>데이터 수집</span>
        </div>
      </template>
      <el-menu-item index="/data-collect/opcua-modeler">
        <div i-ic:outline-circle mr-3 text-2></div>
        <span>모델러</span>
      </el-menu-item>
    </el-sub-menu>
    <el-sub-menu index="data-collect">
      <template #title>
        <div flex items-center justify-center>
          <div i-carbon:data-collection mr-3 text-base></div>
          <span>데이터 조회</span>
        </div>
      </template>
      <el-menu-item index="/data-collect/opcua-modeler">
        <div i-ic:outline-circle mr-3 text-2></div>
        <span>모델러</span>
      </el-menu-item>
    </el-sub-menu>
    <el-sub-menu index="data-collect">
      <template #title>
        <div flex items-center justify-center>
          <div i-carbon:data-collection mr-3 text-base></div>
          <span>AI 데이터 분석</span>
        </div>
      </template>
      <el-menu-item index="/data-collect/opcua-modeler">
        <div i-ic:outline-circle mr-3 text-2 background="#f4f5fa"></div>
        <span>불량원인 데이터 분석</span>
      </el-menu-item>
      <el-menu-item index="/data-collect/opcua-modeler">
        <div i-ic:outline-circle mr-3 text-2></div>
        <span>설비 데이터 분석</span>
      </el-menu-item>
      <el-menu-item index="/data-collect/opcua-modeler">
        <div i-ic:outline-circle mr-3 text-2></div>
        <span>AI 예측 모델 생성</span>
      </el-menu-item>
      <el-menu-item index="/data-collect/opcua-modeler">
        <div i-ic:outline-circle mr-3 text-2></div>
        <span>AI 이상감지 대시보드</span>
      </el-menu-item>
      <el-menu-item index="/data-collect/opcua-modeler">
        <div i-ic:outline-circle mr-3 text-2></div>
        <span>설비 진동 이상감지</span>
      </el-menu-item>
      <el-menu-item index="/data-collect/opcua-modeler">
        <div i-ic:outline-circle mr-3 text-2></div>
        <span>설비 전력 생성</span>
      </el-menu-item>
      <el-menu-item index="/data-collect/opcua-modeler">
        <div i-ic:outline-circle mr-3 text-2></div>
        <span>AI 예측 로그</span>
      </el-menu-item>

    </el-sub-menu>
    <el-sub-menu index="data-collect">
      <template #title>
        <div flex items-center justify-center>
          <div i-carbon:data-collection mr-3 text-base></div>
          <span>시스템 관리</span>
        </div>
      </template>
      <el-menu-item index="/data-collect/opcua-modeler">
        <div i-ic:outline-circle mr-3 text-2></div>
        <span>모델러</span>
      </el-menu-item>
    </el-sub-menu>
  </el-menu>
</el-scrollbar> -->
