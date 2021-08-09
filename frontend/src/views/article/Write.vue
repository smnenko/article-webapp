<template>
    <div class="wrapper">
        <Header />
        <div class="container">
            <h2 class="fw-bold">Write new article</h2>
            <div v-for="err in errors" :key="err" class="alert alert-danger m-1">
                {{ err }}
            </div>
            <div class="alert alert-success" v-if="message">
                {{ message }}
            </div>
            <form @submit="checkForm" @submit.prevent class="container mt-4">
                <div class="row mt-5">
                    <label for="title" class="col-2 fw-bold text-center">Title: </label>
                    <input type="text" class="col-10" id="title" name="title" v-model="title" minlength="8" maxlength="128">
                </div>
                <div class="row mt-3">
                    <label for="content" class="col-2 fw-bold text-center">Content: </label>
                    <textarea rows="10" cols="45" class="col-10" name="content" id="content" v-model="content" minlength="64"></textarea>
                </div>
                <div class="row mt-3">
                    <span class="col-2 fw-bold text-center">Topics: </span>
                    <div class="topics col-10">
                        <div class="topic-item" v-for="topic in availableTopics" :key="topic.id">
                            <label :for="topic.id" class="ml-2">
                                <input type="checkbox" :name="topic.id" :id="topic.id" :value="topic.id" v-model="selectedTopics">
                                {{ topic.name }}
                            </label>
                        </div>
                    </div>
                </div>
                <input type="submit" value="Create new article" class="submit btn btn-success fw-bold mt-4">
            </form>
        </div>
        <Footer class="footer" />
    </div>
</template>

<script>
    import axios from 'axios'
    import Header from "@/components/base/Header";
    import {updateRefresh} from "@/utils/auth";
    import Footer from "@/components/base/Footer";
    export default {
        name: "Write",
        components: {Footer, Header},
        data() {
            return {
                title: null,
                content: null,
                author: this.$cookie.get('email'),
                availableTopics: [],
                selectedTopics: [],
                errors: [],
                message: null
            }
        },
        methods: {
            checkForm(e) {
                this.errors = []
                if (!this.title) {
                    this.errors.push('Title is required for article')
                }
                if (!this.content) {
                    this.errors.push('Some content is required for article')
                }
                if (this.selectedTopics.length === 0) {
                    this.errors.push('Please select at least one topic')
                }
                if (this.errors.length === 0) {
                    this.sendRequest(e)
                }
                e.preventDefault()
            },
            sendRequest(e) {
                axios.post(process.env.VUE_APP_SERVER_HOST + 'article/create/', {
                    'title': this.title,
                    'content': this.content,
                    'author': this.author,
                    'topics': this.selectedTopics
                },{
                    headers: {
                        Authorization: 'Bearer ' + this.$cookie.get('access')
                    }
                })
                    .then(
                        response => {
                            if (response.status === 201) {
                                this.message = response.statusText
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
                            error.config.headers.Authorization = 'Bearer ' + access
                            return axios.request(error.config).then(
                                response => {
                                    if (response.status === 201) {
                                        this.message = response.statusText
                                    }
                                }
                            )
                        }
                        if (error.response.status === 400) {
                            this.errors.push(error.response.data['non_field_errors'][0])
                        }
                    }
                )
                e.target.reset()
            }
        },
        mounted() {
            if (!this.author) {
                this.$router.push('/login')
            }
            else {
                axios
                    .get(process.env.VUE_APP_SERVER_HOST + 'topic/', )
                    .then(
                        response => {
                            this.availableTopics = response.data.results
                        }
                    )

            }
        }
    }
</script>

<style scoped>
    input {
        border: 0;
        border-left: 1px solid silver;
        border-bottom: 1px solid silver;
        outline: none;
    }

    textarea {
        outline: none;
        border: 0;
        border-left: 1px solid silver;
        border-bottom: 1px solid silver;
    }
    .submit {
        margin-left: 45%;
    }

    .footer {
        position: relative;
        top: 10%;
        bottom: 0;
        left: 35%;
        width: 600px;
    }
</style>