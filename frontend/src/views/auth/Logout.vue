<template>
    <div>

    </div>
</template>

<script>
    import {logout} from "@/utils/auth";
    export default {
        name: "Logout",
        mounted() {
            logout(this.$cookie)
            this.$router.push('/')
        }
    }
</script>

<style scoped>

</style>