<template>
    <div>
      <ul>
        <li v-for="item in items" :key="item.id">
          <input v-model="item.name" />
          <button @click="updateItem(item)">Atualizar</button>
          <button @click="deleteItem(item.id)">Excluir</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        items: [],
      };
    },
    created() {
      this.getItems(); // Chamada do método getItems() no ciclo de vida created
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
      },
      updateItem(item) {
        axios.put(`http://localhost:5000/api/items/${item.id}`, item)
          .then(response => {
            // Atualiza o item localmente após a atualização no servidor
            Object.assign(item, response.data);
          })
          .catch(error => {
            console.error(error);
          });
      },
      deleteItem(itemId) {
        axios.delete(`http://localhost:5000/api/items/${itemId}`)
          .then(() => {
            this.items = this.items.filter(item => item.id !== itemId);
          })
          .catch(error => {
            console.error(error);
          });
      }
    }
  };
  </script>
  
  <style>
  /* Estilos do componente */
  </style>
  