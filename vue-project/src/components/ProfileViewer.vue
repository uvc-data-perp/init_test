<template>
  <div>
    <h1>Data Profile Report</h1>
    <div v-if="profileHtml" v-html="profileHtml" ref="contentContainer"></div>
    <div v-else-if="error">Error: {{ error }}</div>
    <div v-else>Loading...</div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, nextTick } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const profileHtml = ref('')
const error = ref(null)
const route = useRoute()
const router = useRouter()
const contentContainer = ref(null)

const fetchProfileHtml = async () => {
  try {
    const response = await axios.get('http://localhost:8000/get_profile_html', {
      responseType: 'text'
    })
    profileHtml.value = response.data
    await nextTick()
    initializeContent()
  } catch (err) {
    console.error('Error fetching profile HTML:', err)
    error.value = err.message || 'An error occurred while fetching data'
  }
}

const initializeContent = () => {
  addEventListeners()
  executeScripts()
  scrollToSection()
}

const addEventListeners = () => {
  if (!contentContainer.value) return

  const links = contentContainer.value.querySelectorAll('a[href^="#"]')
  links.forEach((link) => {
    link.addEventListener('click', handleClick)
  })
}

const executeScripts = () => {
  if (!contentContainer.value) return

  const scripts = Array.from(contentContainer.value.querySelectorAll('script'))
  scripts.forEach((oldScript) => {
    const newScript = document.createElement('script')
    Array.from(oldScript.attributes).forEach((attr) =>
      newScript.setAttribute(attr.name, attr.value)
    )
    newScript.appendChild(document.createTextNode(oldScript.innerHTML))
    oldScript.parentNode.replaceChild(newScript, oldScript)
  })
}

const scrollToSection = () => {
  const hash = window.location.hash.substring(1)
  if (hash) {
    setTimeout(() => {
      const element = document.getElementById(hash)
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' })
      }
    }, 100)
  }
}

const handleClick = (event) => {
  if (event.target.tagName === 'A' && event.target.getAttribute('href').startsWith('#')) {
    event.preventDefault()
    const hash = event.target.getAttribute('href').substring(1)
    router.push({ path: route.path, hash: `#${hash}` })
    scrollToSection()
  }
}

onMounted(() => {
  fetchProfileHtml()
})

watch(() => route.hash, scrollToSection)
</script>

<style scoped>
/* 필요한 경우 여기에 스타일을 추가하세요 */
</style>
