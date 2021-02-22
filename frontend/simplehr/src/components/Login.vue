<template>
  <div class="card mt-4 m-auto">
    <h3 class="card-header text-center">Login</h3>
    <div class="card-body">
      <form action="" enctype="multipart/form-data">
        <div class="form-row">
          <div class="form-group">
            <label for="">Email:</label>
            <input
              type="text"
              class="form-control"
              v-model.trim="$v.email.$model"
              :class="{
                'is-invalid': $v.email.$error,
                'is-valid': !$v.email.$invalid,
              }"
            />
            <div class="valid-feedback">Email is Valid</div>
            <div class="invalid-feedback">
              <span class="d-block" v-if="!$v.email.requiured">Field is required</span>
              <span class="d-block" v-if="!$v.email.email">
                Email  must have at least
              </span>
            </div>
          </div>
          <div class="form-group">
            <label for="">Password:</label>
            <input
              type="password"
              class="form-control"
              v-model.trim="$v.password.$model"
              :class="{
                'is-invalid': $v.password.$error,
                'is-valid': !$v.password.$invalid,
              }"
            />
            <div class="valid-feedback">Password Name is Valid</div>
            <div class="invalid-feedback">
              <span class="d-block" v-if="!$v.password.requiured">Field is required</span>
              <span class="d-block" v-if="!$v.password.minlength">
                Password must have at least {{ $v.password.$params.minlength.min }} characters
              </span>
            </div>
          </div>
    </div>
        <button type="submit" class="btn btn-success d-block m-auto mt-3">Login</button>
      </form>
    </div>
  </div>
</template>

<script>
import { required, minLength, email } from 'vuelidate/lib/validators';

export default {
  data() {
    return {
      email: '',
      password: '',
    };
  },
  validations: {
    email: {
      required,
      email,
    },
    password: {
      required,
      minlength: minLength(8),
    },
  },
};
</script>

<style scoped>
.card{
    width: 300px;
}
</style>
