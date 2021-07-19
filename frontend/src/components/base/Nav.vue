<template>
    <nav class="pt-2">
        <a href="#" class="fw-light text-decoration-none text-dark px-3">Our story</a>
        <a href="#" class="fw-light text-decoration-none text-dark px-3">Membership</a>
        <a href="#" class="fw-light text-decoration-none text-dark px-3">Write</a>
        <a href="#" class="fw-light text-decoration-none text-dark px-3">Sign In</a>
        <a href="#" class="sign-up fw-light text-decoration-none btn btn-success px-3">Get started</a>
    </nav>
</template>

<script>
    export default {
        name: "Nav"
    }
</script>

<style scoped>
    nav {
        font-size: 14px;
    }

    .sign-up {
        border-radius: 25px;
    }
</style>