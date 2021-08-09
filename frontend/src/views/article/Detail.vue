<template>
    <div class="wrapper">
        <Header />
        <div class="container mt-3">
            <div class="inner-wrapper mx-5">
                <h3 class="fw-bold">{{ item.title }}</h3>
                <div class="mt-2">
                    {{ getDateFromDatetime(item.date_created) }} by <router-link :to="'/user/' + item.author" class="text-decoration-none text-dark">{{ item.author }}</router-link>
                </div>
                <div class="content mx-5 mt-4">
                    {{ item.content }}
                </div>
            </div>
        </div>
        <Footer class="footer" />
    </div>
</template>

<script>
    import axios from 'axios'
    import Header from "@/components/base/Header";
    import {getDateFromDatetime} from "@/utils";
    import Footer from "@/components/base/Footer";

    export default {
        name: "Detail",
        components: {Footer, Header},
        methods: {
            getDateFromDatetime,
        },
        data() {
            return {
                item: null
            }
        },
        mounted() {
            axios.get(process.env.VUE_APP_SERVER_HOST + 'article/' + this.$route.params.id + '/').then(
                response => {
                    if (response.status === 200) {
                        this.item = response.data
                        console.log(this.item)
                    }
                }
            )
        }
    }
</script>

<style scoped>

    .container h3 {
        word-break: break-all;
    }

    .content {
        word-break: break-all;
        white-space: pre-wrap;
    }

    .footer {
        position: relative;
        bottom: 0;
        left: 35%;
        width: 600px;
    }

</style>