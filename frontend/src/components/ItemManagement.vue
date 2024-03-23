<script>
import axios from 'axios';

export default {
    // data to store the items
    data() {
        return {
            items: [],
        };
    },
    // get items when component is created
    created() {
        this.getItems(); 
    },
    // GET method to get items
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