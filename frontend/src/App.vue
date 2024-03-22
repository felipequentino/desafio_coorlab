<template>
  <div id="app">
    <h1>CB Viagens</h1>
    <CityFilter />
    <ItemManagement />
  </div>
</template>

<script>
import CityFilter from './components/CityFilter.vue';
import ItemManagement from './components/ItemManagement.vue';

export default {
  components: {
    CityFilter,
    ItemManagement
  },
  data() {
    return {
      items: [],
      newItemName: ''
    };
  },
};
</script>

<style>
#app {
  font-family: Arial, Helvetica, sans-serif;
}
</style>
