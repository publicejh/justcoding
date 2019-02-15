<template>
  <div class="hello">
    <h1 class="title">모임이 쉬워진다! <br>우리끼리 SIG</h1> <!-- Page title -->
    <p class="subtitle">당신의 모임도 SIG로 시작하세요</p>



    <div class="columns">
      <div class="column is-one-third is-offset-one-third"> <!-- Narrow centered column -->
        <form><!-- Form for adding tasks -->

          <div class="field"> <!-- Normal input field for the description -->
            <label class="label">Description</label>
            <div class="control">
              <input class="input" type="text">
            </div>
          </div>

          <div class="field"> <!-- Select field for choosing the status (0 and 1 as value, same as in the django status choices) -->v
            <label class="label">Status</label>
            <div class="control">
              <div class="select">
                <select>
                  <option value="0">To do</option>
                  <option value="1">Done</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field is-grouped"> <!-- Submit button -->
            <div class="control">
              <button class="button is-link">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>


  </div>
</template>

<script>
export default {
  name: 'SignUp',
  data () {
    return {
    }
  }
}
</script>

<style scoped>
.select, select { /* 100% width for the select */
  width: 100%;
}

.card { /* Adding some air under the tasks */
  margin-bottom: 25px;
}

.done { /* Make the done tasks a little bit transparent */
  opacity: 0.3;
}
</style>
