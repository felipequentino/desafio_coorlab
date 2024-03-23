<script>
import axios from 'axios';

export default {
    data() {
        return {
            items: [],
        };
    },
    created() {
        this.getItems(); 
    },
    methods: {
        getItems() {
            axios.get('http://localhost:3000/api/items')
                .then(response => {
                    this.items = response.data;
                    this.$emit('itemAdded', this.items); 
                })
                .catch(error => {
                    console.error(error);
                });
        }
    }
};
</script>