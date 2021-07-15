<template>
    <div class="wrapper border border-bottom-2 border-top-2 border-let-0 border-right-0 border-dark">
        <div class="container py-4">
            <div class="row">
                <div class="col">
                    <h1><span>Medium is a place</span>
                        <span>to write, read, and</span>
                        <span>connect</span>
                    </h1>
                    <p class="fw-bold">It's easy and free to post your thinking on any topic and
                        <span>connect with millions of readers.</span></p>
                </div>
                <div class="col">
                    <img src="https://miro.medium.com/max/349/4*BIK9VGjeCj2TaTDw4id2nA.png" alt="">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Welcome"
    }
</script>

<style scoped>
    .wrapper {
        background-color: lightblue;
    }

    h1 {
        font-size: 70px;
        font-family: Avenir, serif;
    }
    h1 span {
        display: block;
    }

    p span {
        display: block;
    }

    .col img {
        position: relative;
        left: 30%;
        top: 5%;
    }
</style>