<template>
    <div class="wrapper">
        <Header />
        <div class="container">
            <div class="row">
                <div class="col-6">
                    <h4 class="fw-bold mb-5">Your last articles:</h4>
                    <div v-if="articleMessage" class="alert alert-success">
                        {{ articleMessage }}
                    </div>
                    <div v-for="item in items" :key="item.id" class="container mb-4">
                        <button class="delete btn btn-danger" @click="deleteArticle(item.id)">Delete</button>
                        <router-link :to="'/article/' + item.id" class="text-decoration-none text-dark">
                            <h6 class="fw-bold">{{ item.title.slice(0, 55) }}...</h6>
                            <p class="text-muted">{{ item.content.slice(0, 55) }}...</p>
                            <span>{{ getDateFromDatetime(item.date_created) }} • {{ randomMinRead(1, 8) }} min read</span>
                        </router-link>
                    </div>
                </div>
                <div class="col-6">
                    <div class="col-12">
                        <h4 class="fw-bold">User info:</h4>
                        <div v-for="value, key in userInfo" :key="key" class="container">
                            <span class="fw-bold">{{ key.charAt(0).toUpperCase() + key.slice(1) }}: </span>
                            <span>{{ value }}</span>
                        </div>
                    </div>
                    <div class="col-12">
                        <h4 class="fw-bold">User settings:</h4>
                        <div v-for="err in errors" :key="err" class="alert alert-danger w-50 mt-1">
                            {{ err }}
                        </div>
                        <div v-if="message" class="alert alert-success w-50">
                            {{ message }}
                        </div>
                        <form @submit="checkForm" @submit.prevent class="container">
                            <div class="row mt-4">
                                <label for="username" class="col-2 text-center">Username: </label>
                                <input type="text" id="username" class="col-10 w-25" v-model="username">
                            </div>
                            <div class="row mt-3">
                                <label for="name" class="col-2 text-center">Name: </label>
                                <input type="text" id="name" class="col-10 w-25" v-model="name">
                            </div>
                            <div class="row mt-3">
                                <label for="bio" class="col-2 text-center">Bio: </label>
                                <textarea rows="2" class="col-10 w-25" name="content" id="bio" v-model="bio" minlength="1"></textarea>
                            </div>
                            <button type="submit" class="submit btn btn-light mt-3">Update</button>
                        </form>
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
    import {updateRefresh} from "@/utils/auth";

    export default {
        name: "Profile",
        components: {Footer, Header},
        mounted() {
            let id = this.$cookie.get('id')
            axios.get(process.env.VUE_APP_SERVER_HOST + 'auth/' + id + '/', {
                headers: {
                    Authorization: 'Bearer ' + this.$cookie.get('access')
                }
            }).then(
                response => {
                    if (response.status === 200) {
                        this.userInfo = response.data
                        this.name = this.userInfo.name
                        this.username = this.userInfo.username
                        this.bio = this.userInfo.bio
                    }
                    axios.get(process.env.VUE_APP_SERVER_HOST + 'article/latest/' + this.username + '/').then(
                        response => {
                            if (response.status === 200) {
                                this.items = response.data.results
                            }
                        }
                    )
                }
            )
        },
        methods: {
            getDateFromDatetime,
            randomMinRead,
            deleteArticle: function(id) {
                axios.delete(process.env.VUE_APP_SERVER_HOST + 'article/' + id + '/' + this.$cookie.get('id') + '/', {
                    headers: {
                        Authorization: 'Bearer ' + this.$cookie.get('access')
                    }
                }).then(
                    response => {
                        if (response.status === 204) {
                            this.articleMessage = 'Deleted'
                        }
                    }
                )
            },
            checkForm: function (e) {
                this.errors = []
                this.message = null
                if (!this.username) {
                    this.errors.push('Username is required for update profile')
                }
                if (!this.name) {
                    this.errors.push('Name is required for update profile')
                }
                if (!this.bio) {
                    this.errors.push('Bio is required for update profile')
                }
                if (this.name === this.userInfo.name && this.username === this.userInfo.username && this.bio === this.userInfo.bio) {
                    this.errors.push('Info must be different')
                }
                if (this.errors.length === 0) {
                    this.sendRequest(e)
                }
                e.preventDefault()
            },
            sendRequest: function (e) {
                axios.patch(process.env.VUE_APP_SERVER_HOST + 'auth/' + this.$cookie.get('id') + '/', {
                    'username': this.username,
                    'name': this.name,
                    'bio': this.bio,
                }, {
                    headers: {
                        Authorization: 'Bearer ' + this.$cookie.get('access')
                    }
                }).then(
                    response => {
                        if (response.status === 200) {
                            this.message = 'Update success'
                            this.mounted()
                        }
                    }
                )
                    .catch(
                        error => {
                            if (error.response && error.response.data && error.response.data.messages) {
                                let refresh_token = this.$cookie.get('refresh')
                                let email = this.$cookie.get('email')
                                updateRefresh(this.$cookie, email, refresh_token)
                                let access = this.$cookie.get('access')
                                console.log(access)
                                console.log(error.config.headers.Authorization)
                                error.config.headers.Authorization = 'Bearer ' + access
                                console.log(error.config.headers.Authorization)
                                return axios.request(error.config).then(
                                    response => {
                                        if (response.status === 200) {
                                            this.message = 'Update success'
                                        }
                                    }
                                )
                            }
                        }
                    )
                e.target.reset()
            }
        },
        data() {
            return {
                userInfo: null,
                items: null,
                name: null,
                username: null,
                bio: null,
                errors: null,
                message: null,
                articleMessage: null
            }
        },
    }
</script>

<style scoped>

    .delete {
        position: absolute;
        left: 40%;
    }

    .submit {
        margin-left: 20%;
    }

    input {
        outline: none;
        border: 0;
        border-left: 1px solid silver;
        border-bottom: 1px solid silver;
    }

    textarea {
        outline: none;
        border: 0;
        border-left: 1px solid silver;
        border-bottom: 1px solid silver;
    }

    .footer {
        position: relative;
        bottom: 0;
        left: 35%;
        width: 600px;
    }
</style>