<template>
<!-- Just a side bar -->
<div class="sidebar">
    <img alt="CB logo" src="../../../doc/logo.png" class="sidebar-logo">
    <br><br>
    <i class="pi pi-calculator"> Calculadora</i> 
</div>
</template>

<script>
    import 'primeicons/primeicons.css';
    export default {
        name: 'SideBar'
    };
</script>

<style scoped>
.sidebar {
    position: fixed; 
    top: 0;
    bottom: 0;
    left: 0;
    width: 229px;
    background-color: #3e3d5a;
    padding: 20px;
    box-sizing: border-box;
}

.sidebar-logo {
    width: 100%;
}

.sidebar-label {
    color: white;
    margin-top: 20px;
    font-size: 18px;
}

.pi {
    color: white;
    margin-top: 20px;
    font-size: 18px;
    display: block;
    cursor: pointer;
}

@media (max-width: 600px) {
    .sidebar {
        display: none;
    }
}
</style>