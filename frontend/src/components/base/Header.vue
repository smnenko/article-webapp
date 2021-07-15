<template>
    <header class="container py-4 d-flex justify-content-between">
        <a href="/" class="fw-bold fs-1 text-decoration-none text-dark">Article Web App</a>
        <Nav/>
    </header>
</template>

<script>
    import Nav from '@/components/base/Nav.vue'

    export default {
        name: "Header",
        components: {
            Nav
        }
    }
</script>

<style scoped>

</style>