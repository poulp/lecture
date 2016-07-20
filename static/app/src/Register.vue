<template xmlns:v-on="http://www.w3.org/1999/xhtml">
    <div class="container">
        <div class="columns">
            <div class="column"></div>
            <div class="column">
                <div class="box">
                    <form v-on:submit.prevent="register">
                        <p class="control has-icon">
                            <input class="input" type="email" placeholder="Email" v-model="registerForm.username" required>
                            <i class="fa fa-envelope"></i>
                        </p>
                        <p class="control has-icon">
                            <input class="input" type="password" placeholder="Password" v-model="registerForm.password" required>
                            <i class="fa fa-lock"></i>
                        </p>
                        <p class="control has-icon">
                            <input class="input" type="password" placeholder="Password confirmation" v-model="registerForm.passwordConfirm" required>
                            <i class="fa fa-lock"></i>
                        </p>
                        <p class="control">
                            <input type="submit" class="button is-info is-fullwidth" value="Register">
                        </p>
                    </form>
                </div>
            </div>
            <div class="column"></div>
        </div>
    </div>
</template>
<script>
    export default{
        data(){
            return{
                registerForm: {
                    email: '',
                    password: '',
                    passwordConfirm: ''
                }
            }
        },
        methods: {
            register: function() {
                console.log("register");
            }
        }
    }
</script>
