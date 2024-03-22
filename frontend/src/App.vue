<template>
  <div id="app">
    <h1>CB Viagens</h1>
    <CityFilter />
    <ItemManagement />
    <button @click="addItem">Adicionar</button>
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
    },
    addItem() {
      axios.post('http://localhost:5000/api/items', { name: this.newItemName })
        .then(response => {
          this.items.push(response.data);
          this.newItemName = '';
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
  },
};
</script>

<style>
#app {
  font-family: Arial, Helvetica, sans-serif;
}
</style>
