<template>
    <div class="wrapper">
        <Header/>
        <form @submit="checkForm" @submit.prevent>
            <div v-if="success" class="alert alert-success">
                {{ message }}
            </div>
            <h3 class="text-center fw-bold">Registration:</h3>
            <p v-if="errors.length" class="errors">
                <b>Please correct the following errors:</b>
            <ul>
                <li v-for="error in errors" v-bind:key="error">{{ error }}</li>
            </ul>
            <p class="row">
                <label for="email" class="col-6">Email: </label>
                <input type="email" id="email" class="input col-6" v-model="email">
            </p>
            <p class="row">
                <label for="password" class="col-6">Password</label>
                <input type="password" id="password" class="input col-6" minlength="8" maxlength="64"
                       v-model="password">
            </p>
            <input type="submit" value="Submit" class="submit btn btn-success">
        </form>
        <Footer class="footer position-absolute bottom-0" />
    </div>
</template>

<script>
    import axios from 'axios'
    import Header from "@/components/base/Header";
    import Footer from "@/components/base/Footer";

    export default {
        name: "Signup",
        components: {
            Footer,
            Header
        },
        data() {
            return {
                email: null,
                password: null,
                errors: [],
                success: false,
                message: 'Registration successful'
            }
        },
        methods: {
            checkForm: function (e) {
                this.errors = []

                if (!this.email) {
                    this.errors.push('Email is required')
                }

                if (!this.password) {
                    this.errors.push('Password is required')
                }
                if (this.errors.length === 0) {
                    this.sendRequest(e)
                }
                e.preventDefault()
            },
            sendRequest: function (e) {
                axios
                    .post('http://localhost:8000/api/v1/auth/create/', {'email': this.email, 'password': this.password})
                    .then(
                        response => {
                            if (response.status === 201) {
                                this.success = true
                            }
                        }
                    ).catch(
                        error => {
                            let err = error.response.data['email'][0]
                            this.errors.push(err[0].toUpperCase() + err.slice(1))
                        }
                )
                this.email = this.password = ''
                e.target.reset()
            }
        }
    }
</script>

<style scoped>

    form {
        width: 600px;
        margin: 10% auto auto;
    }

    .errors {
        position: relative;
        left: 130px;
    }

    .errors b {
        margin-left: 40px;
    }

    label {
        text-align: right;
    }

    .input {
        width: 300px;
    }

    .row {
        position: relative;
        right: 130px;
    }

    .submit {
        display: block;
        margin: auto;
    }

    .footer {
        left: 35%;
    }

</style>