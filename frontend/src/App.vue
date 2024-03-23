<template>
  <div id="app" class="flex-container">
    <Sidebar />
    <div class="main-content">
      <h1 id="header">Calcule o valor da Viagem</h1>
      <ItemManagement @itemAdded="updateItems" />
      <CityFilter :items="items" />
    </div>
  </div>
</template>

<script>
import CityFilter from './components/CityFilter.vue';
import ItemManagement from './components/ItemManagement.vue';
import Sidebar from './components/Sidebar.vue';

import 'primevue/resources/themes/saga-blue/theme.css'; // theme
import 'primevue/resources/primevue.min.css'; // css 
import 'primeicons/primeicons.css'; // icons

export default {
  name: 'App',
  components: {
    CityFilter,
    ItemManagement,
    Sidebar
  },
  data() {
    return {
      items: [],
    };
  },
  methods: {
    updateItems(items) {
      this.items = items;
    }
  }
};
</script>

<style>
#app {
  font-family: Arial, Helvetica, sans-serif;
}

#id {
  margin-left: 260px
}

#header {
  margin-left: 255px;
}
.main-content {
  margin-left: 20px; 
  width: 100%;
}
body, html {
  margin: 0;
  padding: 0;
}

@media (max-width: 600px) {
  .main-content {
    margin-left: 0px;
  }
  #header {
    margin-left: 5px;
  }
}
</style>
