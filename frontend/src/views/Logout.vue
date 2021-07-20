<template>
    <div>

    </div>
</template>

<script>
    export default {
        name: "Logout",
        mounted() {
            localStorage.removeItem('email')
            localStorage.removeItem('token')
            this.$router.push('/')
        }
    }
</script>

<style scoped>

</style>