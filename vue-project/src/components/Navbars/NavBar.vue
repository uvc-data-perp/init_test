<!-- Header.vue -->
<template>
  <header class="header">
    <div class="logo">
      <router-link to="/">
        <img src="../../assets/logo.svg" alt="Logo" />
      </router-link>
    </div>
    <nav class="nav-menu">
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/about">About</router-link></li>
        <li><router-link to="/services">Services</router-link></li>
        <li><router-link to="/contact">Contact</router-link></li>
      </ul>
    </nav>
    <div class="login-button">
      <button @click="login">{{ isLoggedIn ? 'Logout' : 'Login' }}</button>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const isLoggedIn = ref(false)

const login = () => {
  if (isLoggedIn.value) {
    // 로그아웃 로직
    isLoggedIn.value = false
    console.log('Logged out')
    router.push('/')
  } else {
    // 로그인 로직
    isLoggedIn.value = true
    console.log('Logged in')
    router.push('/dashboard')
  }
}
</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: #f8f8f8;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.logo img {
  height: 40px;
}

.nav-menu ul {
  display: flex;
  list-style-type: none;
  margin: 0;
  padding: 0;
}

.nav-menu li {
  margin: 0 1rem;
}

.nav-menu a {
  text-decoration: none;
  color: #333;
  font-weight: bold;
}

.login-button button {
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.login-button button:hover {
  background-color: #0056b3;
}

/* Active link styles */
.router-link-active {
  color: #007bff;
}
</style>
