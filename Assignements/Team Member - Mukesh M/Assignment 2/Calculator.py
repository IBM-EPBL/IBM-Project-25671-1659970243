<html>
  <head>
    <meta charset="utf-8">
    <title>HTML CSS Register Form</title>
    <link rel="stylesheet" href="D:\VScode\Newfolder\style.css">
  </head>
  <body>
    <form class="signup-form" action="/register" method="post">

      <!-- form header -->
      <div class="form-header">
        <h1>Registration Form</h1>
      </div>

      <!-- form body -->
      <div class="form-body">

        <!--name -->
        <div class="horizontal-group">
          <div class="form-group left">
            <label for="firstname" class="label-title">Name</label>
            <input type="text" id="firstname" class="form-input" placeholder="enter your first name" required="required" />
          </div>
          
          <div class="horizontal-group">
            <div class="form-group left" >
              <label for="firstname" class="label-title">e-mail</label>
              <input type="text" id="city" class="form-input" placeholder="enter your mail address" required="required" />
            </div>
       
        <!-- Gender -->
        <div class="horizontal-group">
          <div class="form-group left">
            <label class="label-title">Gender</label>
            <div class="input-group">
              <label for="male"><input type="radio" name="gender" value="male" id="male"> Male</label>
              <label for="female"><input type="radio" name="gender" value="female" id="female"> Female</label>
            </div>
          </div>
          


         <!-- Source of Income and Income -->
         <div class="horizontal-group">
          <div class="form-group left" >
            <label for="firstname" class="label-title">City</label>
            <input type="text" id="city" class="form-input" placeholder="enter your city" required="required" />
          </div>

          <div class="horizontal-group">
            <div class="form-group left" >
              <label for="firstname" class="label-title">State</label>
              <input type="text" id="city" class="form-input" placeholder="enter your state" required="required" />

            </div>
            <div class="horizontal-group">
              <div class="form-group left" >
                <label for="firstname" class="label-title">Country</label>
                <input type="text" id="city" class="form-input" placeholder="enter your country" required="required" />
              </div>

              <div class="horizontal-group">
                <div class="form-group left" >
                  <label for="firstname" class="label-title">Mobile No</label>
                  <input type="text" id="city" class="form-input" placeholder="enter your mobile number" required="required" />
                </div>

      <!-- form-footer -->
      <div class="form-footer">
        <button type="submit" onclick="alert('Registered Successfully')" class="btn">Register</button>
      </div>

    </form>

  </body>
</html> 
