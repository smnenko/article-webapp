<template>
    <div class="border-bottom">
        <h6 class="fw-bold text-uppercase">Discover more of what matters to you</h6>
        <div class="item-wrapper">
            <div v-for="item in items" v-bind:key="item.id" class="item mx-1 my-1">
                <a :href="'/topic/' + item.name" class="px-3 py-2 d-block text-decoration-none text-muted">{{ item.name }}</a>
            </div>
        </div>
        <a href="/topics" class="d-block text-success text-decoration-none my-4">See all topics</a>
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

    .item-wrapper {
        display: flex;
        flex-wrap: wrap;
    }

    .item {
        border: 1px solid silver;
        border-radius: 5px;
    }

    .item a {
        font-size: 13px;
    }
</style>