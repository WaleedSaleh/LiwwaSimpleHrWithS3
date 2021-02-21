<template>
  <div class="card mt-4 m-auto">
    <h3 class="card-header text-center">Apply</h3>
    <div class="card-body">
      <form action="" enctype="multipart/form-data">
        <div class="form-row">
          <div class="form-group">
            <label for="">First Name:</label>
            <input
              type="text"
              class="form-control"
              v-model.trim="$v.firstname.$model"
              :class="{
                'is-invalid': $v.firstname.$error,
                'is-valid': !$v.firstname.$invalid,
              }"
            />
            <div class="valid-feedback">First Name is Valid</div>
            <div class="invalid-feedback">
              <span v-if="!$v.firstname.requiured">Field is required</span>
              <span v-if="!$v.firstname.minLength">
                First name must have at least
              </span>
            </div>
          </div>
        </div>
        <div class="form-group">
          <label for="">Last Name:</label>
          <input
            type="text"
            class="form-control"
            v-model.trim="$v.lastname.$model"
            :class="{
              'is-invalid': $v.lastname.$error,
              'is-valid': !$v.lastname.$invalid,
            }"
          />
          <div class="valid-feedback">Last Name is Valid</div>
          <div class="invalid-feedback">
            <span v-if="$v.lastname.required">Field is required</span>
            <span v-if="!$v.lastname.minLength">
              Last name must have at least
              {{ $v.firstname.$params.minlength.min }}
            </span>
          </div>
        </div>
        <div class="form-group">
          <label for="">Years of experience:</label>
          <input
            type="number"
            class="form-control"
            v-model.number="$v.yearsofexperience.$model"
            :class="{
              'is-invalid': $v.yearsofexperience.$error,
              'is-valid': !$v.yearsofexperience.$invalid,
            }"
          />
          <div class="valid-feedback">Years of experience are Valid</div>
          <div class="invalid-feedback">
            <span v-if="!$v.yearsofexperience.requiured"
              >Field is required</span
            >
            <span v-if="!$v.yearsofexperience.numeric">
              This field must be a number {{ $v.last.$params.numeric }}
            </span>
          </div>
        </div>
        <!-- For departments -->
        <div class="form-group">
          <label for="">Department:</label>
          <select
            v-model="$v.department.$model"
            class="custom-select form-control"
          >
            <option value="" readonly="true" hidden="true" selected>Select your option</option>
            <option value="1">One</option>
            <option value="2">Two</option>
            <option value="3">Three</option>
          </select>
        </div>
        <div class="">
            <div class="custom-file">
                <label class="custom-file-label mb-2 mt-2" for="customFile">Choose file:</label><br>
                <input type="file" class="custom-file-input form-control" id="customFile">
            </div>
        </div>
        <button type="submit" class="btn btn-success d-block m-auto mt-3">Submit</button>
      </form>
    </div>
  </div>
</template>

<script>
import { required, minLength, numeric } from 'vuelidate/lib/validators';

export default {
  name: 'Register',
  data() {
    return {
      firstname: '',
      lastname: '',
      yearsofexperience: '',
      department: '',
    };
  },
  validations: {
    firstname: {
      required,
      minlength: minLength(5),
    },
    lastname: {
      required,
      minlength: minLength(5),
    },
    yearsofexperience: {
      required,
      numeric,
    },
    department: {
      required,
    },
  },
};
</script>

<style scoped>
.card{
    width: 300px;
}
</style>
