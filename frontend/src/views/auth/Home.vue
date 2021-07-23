<template>
    <div class="mb-5">
        <Header />
        <Welcome />
        <Trending />
        <Latest />
    </div>
</template>

<script>
    import Header from "@/components/base/Header";
    import Welcome from "@/components/Welcome";
    import Latest from "@/components/Latest";
    import Trending from "@/components/Trending";
    export default {
        name: "Home",
        components: {Trending, Latest, Welcome, Header}
    }
</script>

<style scoped>

</style>