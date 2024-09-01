// router/index.js
import { createRouter, createWebHashHistory } from 'vue-router'
import ProfileViewer from '../src/components/ProfileViewer.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: ProfileViewer
  },
  {
    path: '/:section',
    name: 'Section',
    component: ProfileViewer
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
