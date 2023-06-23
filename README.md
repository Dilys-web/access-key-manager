# Project Description
  A web application designed to facilitate the monetization of a multitenant school management platform by offering a key-based access system. It enables School IT Personnel to purchase and manage access keys, while providing Micro-Focus Admins with the ability to monitor and revoke keys, and integrates with school software through an endpoint.


<h2>Setup & Run</h2>
To run the application, please follow the guidlines below
<p>
1. Requirements
 <ul>
  <li>Python3</li>
  <li>Django</li>

</ul></p>
<p>2. Install python3</p>

<p>3. Please setup as indicated below:</p>

 
  ### Clone this repository into the directory of your choice
  ```
  git clone https://github.com/Dilys-web/access-key-manager.git
  ```
  
  ### Move into project folder
   ```
   cd file-server
   ```
  ### create a virtual environment and activate it
  ```
  python -m venv "the name of your virtual environment"
  ```

  ### install dependencies from requirments.txt
  ```
  pip install -r requirements.txt
  ```
  
  ### Migrate models
  ```
  python manage.py migrate
  ```
 ### login at
  ```
  http://127.0.0.1:8000/accounts/login/
  ```
  ### Signup at
  ```
  http://127.0.0.1:8000/accounts/signup/
  ```
  ### Reset Password at
  ```
  http://127.0.0.1:8000/accounts/password_reset/
  ```

  ### Access the keys page at
  ```
  http://127.0.0.1:8000/
  ```
  ### Access the create keys link at 
  ```
  http://127.0.0.1:8000/new-key/
  ```
  ### Access the api endpoint at
  ```
  http://127.0.0.1:8000/api/access-keys/<email>/
  ```