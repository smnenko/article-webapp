<template>
    <div class="container mt-5">
        <div class="row">
            <div class="col-8">
                <div v-for="item in items" :key="item.id.toString()" class="mt-3">
                    <h6 class="fw-bold">{{ item.author }}</h6>
                    <router-link :to="'/article/' + item.id" class="text-decoration-none text-dark">
                        <h3 class="fw-bold">{{ item.title.substring(0, 50) }}...</h3>
                        <p class="text-muted">{{ item.content }}</p>
                        <div>
                            <span>{{ getDateFromDatetime(item.date_created) }}</span>
                            <span> • {{ randomMinRead(1, 8) }} min read • </span>
                            <span v-for="topic in item.topics" :key="topic.id.toString()" class="topic p-1 mr-3">{{ topic.name }}</span>
                        </div>
                    </router-link>
                </div>
            </div>
            <div class="col-4">
                <Topics />
                <Footer />
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import Topics from "@/components/Topics";
    import Footer from "@/components/base/Footer";
    import {getDateFromDatetime, randomMinRead} from '@/utils'
    export default {
        name: "Latest",
        components: {Footer, Topics},
        data() {
            return {
                items: null
            }
        },
        mounted() {
            axios
                .get('http://localhost:8000/api/v1/article/latest/')
                .then(
                    response => {
                        if (response.status === 200) {
                            this.items = response.data.results
                        }
                    }
                )
        },
        methods: {
            getDateFromDatetime,
            randomMinRead
        }
    }
</script>

<style scoped>

    h6 {
        font-size: 14px;
    }

    p {
        font-size: 15px;
    }

    .topic {
        display: inline-block;
        margin-right: 5px;
        background-color: lightgrey;
        border-radius: 5px;
        font-size: 14px;
    }

</style>