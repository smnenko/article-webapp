<template>
    <div class="wrapper">
        <Header/>
        <div class="container">
            <div class="container">
                <div class="row">
                    <div class="col-8">
                        <div class="col-6">
                            <h4 class="fw-bold mb-5">{{ username }}'s last articles:</h4>
                            <div v-if="articleMessage" class="alert alert-success">
                                {{ articleMessage }}
                            </div>
                            <div v-for="item in items" :key="item.id" class="container mb-4">
                                <router-link :to="'/article/' + item.id" class="text-decoration-none text-dark">
                                    <h6 class="fw-bold">{{ item.title.slice(0, 55) }}...</h6>
                                    <p class="text-muted">{{ item.content.slice(0, 55) }}...</p>
                                    <span>{{ getDateFromDatetime(item.date_created) }} • {{ randomMinRead(1, 8) }} min read</span>
                                </router-link>
                            </div>
                        </div>
                    </div>
                    <div class="col-4">
                        <div>
                            <span class="fw-bold">Username: </span>
                            {{ username }}
                        </div>
                        <div>
                            <span class="fw-bold">Name: </span>
                            {{ name }}
                        </div>
                        <div>
                            <span class="fw-bold">Birthday: </span>
                            {{ birthday }}
                        </div>
                        <div>
                            <span class="fw-bold">Country: </span>
                            {{ country }}
                        </div>
                        <div>
                            <span class="fw-bold">Bio: </span>
                            {{ bio }}
                        </div>
                        <div v-if="errors">
                            <div v-for="error in errors" :key="error" class="alert alert-danger">
                                {{ error }}
                            </div>
                        </div>
                        <div v-if="status === true">
                            <button class="btn btn-danger" @click="subscribe">unSubscribe</button>
                        </div>
                        <div v-else>
                            <button class="btn btn-success" @click="subscribe">Subscribe</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <Footer class="footer" />
    </div>
</template>

<script>
    import axios from 'axios'
    import Header from "@/components/base/Header";
    import {getDateFromDatetime, randomMinRead} from "@/utils";
    import Footer from "@/components/base/Footer";

    export default {
        name: "User",
        components: {Footer, Header},
        data() {
            return {
                username: null,
                name: null,
                birthday: null,
                country: null,
                bio: null,
                items: null,
                status: null,
                errors: null
            }
        },
        methods: {
            getDateFromDatetime,
            randomMinRead,
            subscribe: function () {
                axios.post(process.env.VUE_APP_SERVER_HOST + 'subscribe/create/', {
                    author: this.username,
                    subscriber: this.$cookie.get('email')
                }, {
                    headers: {
                        Authorization: 'Bearer ' + this.$cookie.get('access')
                    }
                }).then(
                    response => {
                        if (response.status === 201) {
                            this.status = true
                        }
                        if (response.status === 204) {
                            this.status = false
                        }
                    }
                ).catch(
                    error => {
                        this.errors = []
                        let errorMsg = error.response.data['non_field_errors'][0]
                        this.errors.push(errorMsg[0].toUpperCase() + errorMsg.slice(1))
                    }
                )
            }
        },
        mounted() {
            axios.get(process.env.VUE_APP_SERVER_HOST + 'auth/' + this.$route.params.username + '/', {
                headers: {
                    Authorization: 'Bearer ' + this.$cookie.get('access')
                }
            })
                .then(
                    response => {
                        this.username = response.data['username']
                        this.name = response.data['name']
                        this.birthday = response.data['birthday']
                        this.country = response.data['country']
                        this.bio = response.data['bio']
                        this.status = response.data['status']
                        console.log(response.data)
                        axios.get(process.env.VUE_APP_SERVER_HOST + 'article/latest/' + this.username + '/').then(
                            response => {
                                if (response.status === 200) {
                                    this.items = response.data.results
                                    axios.get(process.env.VUE_APP_SERVER_HOST + 'subscribe/', {
                                        headers: {
                                            Authorization: 'Bearer ' + this.$cookie.get('access')
                                        },
                                        params: {
                                            author: this.username,
                                            subscriber: this.$cookie.get('email')
                                        }
                                    }).then(response => {
                                        if (response.status === 200) {
                                            this.status = response.data.status
                                        }
                                    })
                                }
                            }
                        )
                    }
                )
        }
    }
</script>

<style scoped>
    .footer {
        position: relative;
        bottom: 0;
        left: 35%;
        width: 600px;
    }
</style>