<template>
    <div>
        <h4 class="fw-bold mb-5">Your last articles:</h4>
        <div v-if="articleMessage" class="alert alert-success">
            {{ articleMessage }}
        </div>
        <div v-for="item in items" :key="item.id" class="container mb-4">
            <button class="delete btn btn-danger" @click="deleteArticle(item.id)">Delete</button>
            <router-link :to="'/article/' + item.id" class="text-decoration-none text-dark">
                <h6 class="fw-bold">{{ item.title.slice(0, 55) }}...</h6>
                <p class="text-muted">{{ item.content.slice(0, 55) }}...</p>
                <span>{{ getDateFromDatetime(item.date_created) }} • {{ randomMinRead(1, 8) }} min read</span>
            </router-link>
        </div>
    </div>
</template>

<script>
    export default {
        name: "UserLatest"
    }
</script>

<style scoped>

</style>