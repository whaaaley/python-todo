import { VueQueryPlugin } from '@tanstack/vue-query'
import { createApp } from 'vue'
import { createRouter, createWebHistory, RouterView } from 'vue-router'

import './index.css'

const router = createRouter({
  history: createWebHistory('/'),
  routes: [
    {
      name: 'home',
      path: '/',
      component: () => import('./Home.page.tsx'),
    }
  ],
  scrollBehavior: (_to, _from, savedPosition) => {
    return savedPosition || { top: 0, behavior: 'smooth' }
  },
})

const app = createApp(RouterView)

app.use(router)
app.use(VueQueryPlugin)

app.mount('#app')
