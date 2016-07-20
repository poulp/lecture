<template xmlns:v-on="http://www.w3.org/1999/xhtml">
    <div class="container">
        <div class="columns">
            <div class="column"></div>
            <div class="column">
                <div class="box">
                    <form v-on:submit.prevent="login">
                        <p class="control has-icon">
                            <input class="input" type="email" placeholder="Email" v-model="loginForm.username" required>
                            <i class="fa fa-envelope"></i>
                        </p>
                        <p class="control has-icon">
                            <input class="input" type="password" placeholder="Password" v-model="loginForm.password" required>
                            <i class="fa fa-lock"></i>
                        </p>
                        <p class="control">
                            <input type="submit" class="button is-success is-fullwidth" value="Login">
                        </p>
                    </form>
                </div>
                <p>Not registered yet? <a v-link="{ path: '/register' }">create your account here</a></p>
            </div>
            <div class="column"></div>
        </div>
    </div>
</template>

<script>
    export default{
        data () {
            return {
                loginForm: {
                    username: '',
                    password: ''
                }
            }
        },
        methods: {
            login: function() {
                this.$http.get('http://azeaze.com').then((response) => {
                    console.log("test");
                }, (response) => {
                    // error callback
                });
            }
        }
    }
</script>
