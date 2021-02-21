<template>
  <!-- <div class="container col-xs-12 col-sm-6 log-in-form bg-white"> -->
  <div class="log-in-form">
    <h2 class="header text-center">Admin Login</h2>
    <hr class="w-50 m-auto" />
    <form action="" class="form-group" @click.prevent="submit()">
      <div
        class="form-group"
        :class="{ 'form-group--error': $v.form.userName.$error }"
      >
        <label class="form__label col-form-label">Email</label>
        <input
          class="form__input form-control d-block m-auto"
          :class="status($v.form.userName)"
          v-model.trim="$v.form.userName.$model"
          placeholder="example@example.com"
        />
        <div class="error" v-if="!$v.form.userName.email" style="color: red">
          please enter a valid email.
        </div>
      </div>
      <div
        class="form-group"
        :class="{ 'form-group--error': $v.form.password.$error }"
      >
        <label class="form__label col-form-label">Password</label>
        <input
          class="form__input form-control d-block m-auto"
          :class="status($v.form.password)"
          v-model.trim="$v.form.password.$model"
          type="password"
          placeholder="********"
        />
      </div>
      <div class="error" v-if="!$v.form.password.minLength">
        Field must have at least
        {{ $v.form.password.$params.minLength.min }} characters.
      </div>
      <div class="form-group" :class="{ 'form-group--error': $v.form.$error }">
        <div
          class="error"
          v-if="$v.form.userName.$error && $v.form.password.$error"
        >
          Form is invalid.
        </div>
      </div>
      <button
        type="submit" :disabled="submitStatus === 'PENDING'"
        class="btn btn-success d-block m-auto form-control w-50 mt-4" >
        Login
      </button>
    </form>
    <p class="typo__p" v-if="submitStatus === 'OK'">Thanks for your submission!</p>
    <p class="typo__p" v-if="submitStatus === 'ERROR'">Please fill the form correctly.</p>
    <p class="typo__p" v-if="submitStatus === 'PENDING'">Sending...</p>
  </div>
</template>



<style scoped>
.log-in-form {
  background-color: white;
  overflow: auto;
  border: 1px solid black;
  position: absolute;
  top: 15%;
  right: 14%;
  width: 25%;
  height: 50%;
}

form input[type="text"] input[type="password"] {
  display: block !important;
  margin: 0 auto !important;
}

.form__input {
  width: 50%;
}

.error {
  color: red;
  width: 50%;
  margin: 0 auto;
}

.btn-submit {
  display: block;
  margin: 0 auto;
}

.dirty {
  border-color: #5a5;
  background: #efe;
}

.dirty:focus {
  outline-color: #8e8;
}

.error {
  border-color: red;
  background: #fdd;
}

.error:focus {
  outline-color: #fff;
}
</style>

<script>
import { required, minLength, email } from 'vuelidate/lib/validators';
/* eslint-disable */
export default {
  data() {
    return {
      form: {
        userName: '',
        password: '',
        submitStatus: null,
      },
    };
  },
  validations: {
    form: {
      userName: {
        required,
        email,
        minLength: minLength(5),
      },
      password: {
        required,
        minLength: minLength(8),
      },
    },
  },
  methods: {
    status(validation) {
      return {
        error: validation.$error,
        dirty: validation.$dirty,
      };
    },
  },
  submit() {
    console.log('submit!');
    this.$v.$touch();
    if (this.$v.$invalid) {
      this.submitStatus = 'ERROR';
    } else {
        console.log('WORKED');
      this.submitStatus = 'PENDING';
      setTimeout(() => {
        this.submitStatus = 'OK';
      }, 500);
    }
  },
};
</script>
