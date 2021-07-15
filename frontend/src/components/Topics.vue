<template>
    <div>
        <h6 class="fw-bold text-uppercase">Discover more of what matters to you</h6>
        <div class="topics">
            <div v-for="item in items" v-bind:key="item.id" class="item px-3 py-2 mx-1 my-1">
                <a :href="'/topic/' + item.name" class="text-decoration-none text-muted">{{ item.name }}</a>
            </div>
        </div>
        <a href="/topics" class="d-block text-success text-decoration-none mt-1">See all topics</a>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "Topics",
        data() {
            return {
                items: null
            }
        },
        mounted() {
            axios
                .get('http://localhost:8000/api/v1/topic/')
                .then(
                    response => {
                        if (response.status === 200) {
                            this.items = response.data.results
                        }
                    }
                )
        },
    }
</script>

<style scoped>
    h6 {
        font-size: 14px;
    }

    .item {
        border: 1px solid silver;
        border-radius: 5px;
        float: left;
    }

    .item:last-of-type {
        clear: both;
    }

    .item a {
        font-size: 13px;
    }
</style>