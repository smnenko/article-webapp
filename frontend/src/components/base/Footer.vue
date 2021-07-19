<template>
    <div class="mt-3 d-flex flex-wrap">
        <a href="" v-for="item in items" v-bind:key="item" class="item text-decoration-none text-muted mx-3 my-2">{{ item }}</a>
    </div>
</template>

<script>
    export default {
        name: "Footer",
        data() {
            return {
                items: ['Help', 'Status', 'Writers', 'Blog', 'Careers', 'Privacy', 'Terms', 'About']
            }
        }
    }
</script>

<style scoped>

    .item {
        font-size: 13px;
    }

</style>