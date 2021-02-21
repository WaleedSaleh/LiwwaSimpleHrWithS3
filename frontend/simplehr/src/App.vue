<template>
<div id="app">
  <Navbar />
  <router-view />
</div>
</template>


<style scoped>
#nav-holder{
  width: 100%;
}
</style>

<script>
import Navbar from './components/Navbar.vue';


export default {
  name: 'App',
  components: {
    Navbar,
  },
};
</script>
