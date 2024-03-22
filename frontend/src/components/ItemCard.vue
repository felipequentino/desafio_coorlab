<template>
    <div class="item-card">
      <h2>{{ item.name }}</h2>
      <p>{{ item.city }}</p>
      <p>{{ item.date }}</p>
      <!-- Adicione mais campos conforme necessário -->
    </div>
  </template>
  
  <script>
  export default {
    props: ['item'],
    name: 'ItemCard'
  };
  </script>
  
  <style scoped>
  .item-card {
    border: 1px solid #ccc;
    padding: 20px;
    margin-bottom: 20px;
  }
  </style>