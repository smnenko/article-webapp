<template>
    <nav class="pt-2">
        <a href="#" class="fw-light text-decoration-none text-dark px-3">Our story</a>
        <a href="#" class="fw-light text-decoration-none text-dark px-3">Membership</a>
        <a href="#" class="fw-light text-decoration-none text-dark px-3">Write</a>
        <span v-if="email">
            {{ email }}
            <router-link to="logout" class="logout fw-light text-decoration-none btn btn-secondary">Logout</router-link>
        </span>
        <span v-else>
            <router-link to="/login" class="fw-light text-decoration-none text-dark px-3">Sign In</router-link>
            <router-link to="/signup"
                         class="sign-up fw-light text-decoration-none btn btn-success px-3">Get started</router-link>
        </span>
    </nav>
</template>

<script>
    export default {
        name: "Nav",
        data() {
            return {
                email: localStorage.getItem('email')
            }
        },
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