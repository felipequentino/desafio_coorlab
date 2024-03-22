<template>
    <div>
      <input type="text" v-model="searchCity" placeholder="Digite a cidade">
      <div v-for="item in filteredItems" :key="item.id">
        <p>{{ item.name }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        items: [],
        searchCity: '',
      };
    },
    created() {
      this.getItems();
    },
    methods: {
      getItems() {
        axios.get('http://localhost:5000/api/items')
          .then(response => {
            this.items = response.data;
          })
          .catch(error => {
            console.error(error);
          });
      }
    },
    computed: {
      filteredItems() {
        return this.items.filter(item => item.city.includes(this.searchCity));
      }
    }
  };
  </script>
  
  <style>
  /* Estilos do componente */
  </style>
  