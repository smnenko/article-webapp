<template>
    <div class="container mt-5">
        <div class="row">
            <div class="col-8">
                <div v-for="item in items" :key="item.id.toString()" class="mt-3">
                    <router-link :to="'/user/' + item.author" class="text-decoration-none text-dark">
                        <h6 class="fw-bold">{{ item.author }}</h6>
                    </router-link>
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
                <div class="border-bottom">
                    <h6 class="fw-bold text-uppercase">Article filter</h6>
                    <div class="item-wrapper mb-3">
                        <form @submit="checkForm" @submit.prevent class="my-3">
                            <label for="content" class="mx-2">Content contains: </label>
                            <input type="text" id="content" class="pl-3" v-model="content">
                        </form>
                        <div v-for="item in this.topics" v-bind:key="item.id" class="item mx-1 my-1">
                            <button class="px-3 py-2 d-block text-decoration-none text-muted btn" @click="selectTopic(item.id)" v-bind:class="{ 'btn-selected': selectedTopics.includes(item.id) }">{{ item.name }}</button>
                        </div>
                    </div>
                </div>
                <Footer />
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import Footer from "@/components/base/Footer";
    import {getDateFromDatetime, randomMinRead} from '@/utils'
    export default {
        name: "Latest",
        components: {Footer},
        data() {
            return {
                items: null,
                topics: null,
                content: null,
                selectedTopics: []
            }
        },
        methods: {
            getDateFromDatetime,
            randomMinRead,
            checkForm: function (e) {
                axios.get(process.env.VUE_APP_SERVER_HOST + 'article/latest/', {
                    params: {
                        topic: this.selectedTopics,
                        content: this.content
                    }
                })
                    .then(
                        response => {
                            this.items = response.data.results
                        }
                    )
                e.preventDefault()
            },
            selectTopic: function (id) {
                if (this.selectedTopics.includes(id)) {
                    let ind = this.selectedTopics.indexOf(this.topics[id - 1].id)
                    this.selectedTopics.splice(ind, 1)
                } else {
                    this.selectedTopics.push(this.topics[id - 1].id)
                }
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
            axios
                .get('http://localhost:8000/api/v1/topic/')
                .then(
                    response => {
                        if (response.status === 200) {
                            this.topics = response.data.results
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

    .item button {
        font-size: 13px;
    }

    input {
        border: 0;
        outline: none;
        border-left: 1px solid silver;
        border-bottom: 1px solid silver;
    }

    .btn-selected {
        background-color: skyblue;
        color: white!important;
    }
</style>