<template>
    <div>

    </div>
</template>

<script>
    export default {
        name: "Logout",
        mounted() {
            this.$cookie.delete('email')
            this.$cookie.delete('token')
            this.$router.push('/')
        }
    }
</script>

<style scoped>

</style>