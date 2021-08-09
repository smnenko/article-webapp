<template>
    <nav class="pt-2">
        <a href="#" class="fw-light text-decoration-none text-dark px-3">Our story</a>
        <a href="#" class="fw-light text-decoration-none text-dark px-3">Membership</a>
        <router-link to="/write" class="fw-light text-decoration-none text-dark px-3">Write</router-link>
        <span v-if="status">
                <router-link to="/profile" class="text-decoration-none text-dark">{{ email }}</router-link>
            <router-link to="/logout" class="logout fw-light text-decoration-none btn btn-secondary">Logout</router-link>
        </span>
        <span v-else>
            <router-link to="/login" class="fw-light text-decoration-none text-dark px-3">Sign In</router-link>
            <router-link to="/signup"
                         class="sign-up fw-light text-decoration-none btn btn-success px-3">Get started</router-link>
        </span>
    </nav>
</template>

<script>
    import {logout} from "@/utils/auth";

    export default {
        name: "Nav",
        data() {
            return {
                email: this.$cookie.get('email'),
                status: null,
            }
        },
        mounted() {
            if (this.$cookie.get('email')) {
                let expTokenDate = this.$cookie.get('refresh_exp')
                if (new Date(expTokenDate * 1000) > new Date())
                {
                    this.status=true
                }
                else {
                    logout(this.$cookie)
                    this.status=false
                }
            }
        }
    }
</script>

<style scoped>
    nav {
        font-size: 14px;
    }

    .sign-up {
        border-radius: 25px;
    }

    .logout {
        border-radius: 5px;
        margin-left: 5px;
    }
</style>