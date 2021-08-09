<template>
    <div class="wrapper">
        <Header />
        <div class="container">
            <div class="container">
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
                        <div class="fw-bold fs-3">{{ name }}</div>
                        <p>{{ quote }}</p>
                        <hr>
                        <p>{{ description }}</p>
                        <hr>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import Header from "@/components/base/Header";
    import {getDateFromDatetime, randomMinRead} from "@/utils";

    export default {
        name: "Detail",
        components: {Header},
        data() {
            return {
                name: null,
                quote: null,
                description: null,
                items: null,
            }
        },
        methods: {
            getDateFromDatetime,
            randomMinRead,
            checkForm: function (e) {
                axios.get(process.env.VUE_APP_SERVER_HOST + 'article/filter/?topic=' + this.name + '&content=' + this.content)
                    .then(
                        response => {
                            this.items = response.data.results
                        }
                    )
                e.preventDefault()
            }
        },
        mounted() {
            axios.get(process.env.VUE_APP_SERVER_HOST + 'topic/' + this.$route.params.name + '/')
                .then(
                    response => {
                        this.name = response.data['name']
                        this.quote = response.data['quote']
                        this.description = response.data['description']
                        axios.get(process.env.VUE_APP_SERVER_HOST + 'article/filter/?topic=' + this.name).then(
                            response => {
                                this.items = response.data.results
                            }
                        )
                    }
                )
        }
    }
</script>

<style scoped>
    .topic {
        display: inline-block;
        margin-right: 5px;
        background-color: lightgrey;
        border-radius: 5px;
        font-size: 14px;
    }
</style>