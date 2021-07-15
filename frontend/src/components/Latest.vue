<template>
    <div class="container mt-5">
        <div class="row">
            <div class="col-8">
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. A culpa fuga incidunt itaque natus omnis placeat quasi quo. Adipisci, commodi in inventore itaque nulla perferendis quaerat quidem saepe voluptas voluptates.</p>
            </div>
            <div class="col-4">
                <Topics />
            </div>
        </div>
    </div>
</template>

<script>
    import Topics from "@/components/Topics";
    export default {
        name: "Latest",
        components: {Topics}
    }
</script>

<style scoped>

</style>