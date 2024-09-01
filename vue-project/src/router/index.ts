import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('../components/ProfileViewer.vue')
    },
    {
      path: '/:section',
      name: 'Section',
      component: () => import('../components/ProfileViewer.vue')
    }
  ]
})

export default router
