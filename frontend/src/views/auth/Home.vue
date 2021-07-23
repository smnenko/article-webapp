<template>
    <div>
        <Header />
        <Welcome />
        <Latest />
    </div>
</template>

<script>
    import Header from "@/components/base/Header";
    import Welcome from "@/components/Welcome";
    import Latest from "@/components/Latest";
    export default {
        name: "Home",
        components: {Latest, Welcome, Header}
    }
</script>

<style scoped>

</style>