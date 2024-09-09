<template>
  <div class="profile-viewer">
    <div v-if="isLoading">Loading...</div>
    <div v-else-if="error">Error: {{ error }}</div>
    <div v-else>
      <Overview :data="overviewData" />
      <Variables :data="variablesData" />
      <Correlations :data="correlationsData" />
      <MissingValues :data="missingValuesData" />
      <Sample :data="sampleData" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Overview from './yData/Overview.vue'
import Variables from './yData/Variables.vue'
import Correlations from './yData/Correlations.vue'
import MissingValues from './yData/MissingValues.vue'
import Sample from './yData/Sample.vue'

const isLoading = ref(true)
const error = ref(null)
const overviewData = ref(null)
const variablesData = ref(null)
const correlationsData = ref(null)
const missingValuesData = ref(null)
const sampleData = ref(null)

const fetchAndParseHtml = async () => {
  try {
    isLoading.value = true
    const response = await axios.get('http://localhost:8000/get_profile_html', {
      responseType: 'text'
    })
    const html = response.data
    parseHtml(html)
  } catch (err) {
    console.error('Error fetching profile HTML:', err)
    error.value = err.message || 'An error occurred while fetching data'
  } finally {
    isLoading.value = false
  }
}

const parseHtml = (html) => {
  const parser = new DOMParser()
  const doc = parser.parseFromString(html, 'text/html')

  overviewData.value = extractSectionData(doc, '#overview')
  variablesData.value = extractSectionData(doc, '#variables')
  correlationsData.value = extractSectionData(doc, '#correlations_tab')
  missingValuesData.value = extractSectionData(doc, '#missing')
  sampleData.value = extractSectionData(doc, '#sample')
}

const extractSectionData = (doc, selector) => {
  const section = doc.querySelector(selector)
  return section ? section.innerHTML : null
}

onMounted(fetchAndParseHtml)
</script>

<style scoped>
.profile-viewer {
  /* 스타일 추가 */
}
</style>
