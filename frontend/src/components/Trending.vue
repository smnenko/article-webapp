<template>
    <div class="wrapper">
        <div class="container py-5">
            <h6 class="text-uppercase fw-bold">Trending on Article Wep App</h6>
            <div class="trending row m-0">
                <div v-for="(item, index) in items" v-bind:key="index" class="col-4 my-3">
                    <div class="row m-0">
                        <h1 class="col-2 text-muted fw-bold">0{{ index + 1 }}</h1>
                        <div class="row col-10">
                        <span class="col-10 pt-2">
                            <img src="https://miro.medium.com/fit/c/20/20/1*dmbNkD5D-u45r44go_cf0g.png" class="pb-1" alt="">
                            <a :href="'/author/' + item.author" class="author px-3 fw-bold text-decoration-none text-dark">{{ item.author }}</a>
                        </span>
                            <span class="col-12 pt-2 fw-bold">
                            {{ item.title }}
                        </span>
                            <span class="col-12 date text-muted">
                            {{ getDateFromDatetime(item.date_created) }} • {{ randomMinRead(1, 8) }} min read
                        </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import {getDateFromDatetime, randomMinRead} from '@/utils'

    export default {
        name: "Trending",
        data() {
            return {
                items: null
            }
        },
        mounted() {
            axios
                .get('http://localhost:8000/api/v1/article/trending/')
                .then(
                    response => {
                        if (response.status === 200) {
                            this.items = response.data.results;
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

    .wrapper {
        border-bottom: 2px solid silver;
    }

    .author {
        font-size: 13px;
    }
    .date {
        font-size: 14px;
    }
</style>