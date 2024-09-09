<!-- <template>
  <div>
    <h1>Data Profile Report</h1>
    <div v-if="profileHtml" v-html="profileHtml"></div>
    <div v-else-if="error">Error: {{ error }}</div>
    <div v-else>Loading...</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const profileHtml = ref('')
const error = ref(null)

const fetchProfileHtml = async () => {
  try {
    const response = await axios.get('http://localhost:8000/get_profile_html', {
      responseType: 'text'
    })
    profileHtml.value = response.data
  } catch (err) {
    console.error('Error fetching profile HTML:', err)
    error.value = err.message || 'An error occurred while fetching data'
  }
}

onMounted(fetchProfileHtml)
</script>

<style scoped>
/* 필요한 경우 여기에 스타일을 추가하세요 */
</style> -->

<template>
  <div id="app">
    <NavBar />
    <router-view></router-view>
  </div>
</template>

<script setup>
import NavBar from './components/Navbars/NavBar.vue'
// 필요한 경우 여기에 스크립트를 추가하세요
</script>

<style>
/* 필요한 경우 여기에 전역 스타일을 추가하세요 */
</style>
