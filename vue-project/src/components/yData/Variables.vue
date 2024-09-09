<template>
  <div class="variable-section" v-if="data" v-html="data"></div>
</template>

<script setup>
defineProps(['data'])
</script>

<style scoped>
.overview-section {
  /* 섹션별 스타일 */
}
</style>
