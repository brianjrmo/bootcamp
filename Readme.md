<h1>This is for bootcamp activities</h1>

<h2>1. Functionality</h2>
In this bootcamp practise excercise, I develop an application that keep track of user activities. The functions of the application include:
<ul>
<li>1.1 Add and delete user in the application.</li>
<li>1.2 User can login and logoff in the application.</li>
<li>1.3 Find a user by name.</li>
<li>1.4 Count number of users.</li>
<li>1.5 Every 5 minutes, generate a report with all users and their last action time, include those have already been deleted.</li>
</ul>

<h2>2. Application Design</h2>
The application consists of 3 components: Database, RESTful API, Airflow
<h3>2.1 Database</h3>
Use MySQL as dabtabase. It has a usertable containing id, name, status, latest_action(datetime).
<br>
The table records all users which have ever been created. 'DELETED' user still remain in the table, but can not be further change.
<br>
Active(non-deleted) users are unique, we can not create a user with same name as existing active user.
<br>
<h3>2.2 RESTful API</h3>
RESTful API provide operations on individual user, this implement functionality from 1.1 to 1.4.
<br>
API list:
<table>
  <tr>
    <th>Function</th>
    <th>uri</th>
    <th>success respond</th>
    <th>fail respond</th>
  </tr>
  <tr>
    <td>Get number of active users</td>
    <td>http://(hostname):5000</td>
    <td>There are <n> user(s).</td>
    <td>There is no user.</td>
  </tr>
  <tr>
    <td>Find user by name</td>
    <td>http://(hostname):5000/find?username=(name)</td>
    <td>User found.</td>
    <td>User not found.</td>
  </tr>
  <tr>
    <td>Add a user</td>
    <td>http://(hostname):5000/add?username=(name)</td>
    <td>User (name) added</td>
    <td>User already exist.</td>
  </tr>
  <tr>
    <td>Delete a user</td>
    <td>http://(hostname):5000/delete?username=(name)</td>
    <td>User (name) DELETED</td>
    <td>User not exist.</td>
  </tr>
  <tr>
    <td>User login</td>
    <td>http://(hostname):5000/login?username=(name)</td>
    <td>User (name) LOGON</td>
    <td>User not exist.</td>
  </tr>
  <tr>
    <td>User logoff</td>
    <td>http://(hostname):5000/logoff?username=(name)</td>
    <td>User (name) LOGOFF</td>
    <td>User not exist.</td>
  </tr>
</table>
<br>
There's a CLI utility call RESTful API to carry out user management task. To run the utility:
<br>
Get all files from <a href="https://github.com/brianjrmo/bootcamp/tree/main/scripts/restapi">restapi</a>.
<br>
Run this command to check usage: python manage_user.py --help
<br>
<h3>2.3 Airflow</h3>
Airflow will map 2 volumns from host to container, host folders are:
<br>
- dags/ We can put valid dags file here so that Airflow can process with.
<br>
- logs/ Airflow log will come to here. 
<br>
A DAG user_status_dag run every 5 minutes to extract up-to-date user status information from usertable. The created report(a csv file) also save in logs/ folder.

<h3>2.4 Two steps to start the application</h3>
<h4>2.4.1 Download source</h4>
Download source from https://github.com/brianjrmo/bootcamp.git
<h4>2.4.2 Change access mode</h4>
To make the volumns accessible, run 2 command before start docker-compose:
<br>
chmod 777 -R logs/
<br>
chmod 777 -R dags/
<h4>2.4.3 Start containers</h4>
start the <a href="https://github.com/brianjrmo/bootcamp/blob/main/docker-compose.yaml">docker-composer.yaml</a> with command: docker-compose up


<h2>3. Limitation and Rooms of improvement</h2>
<h3>3.1 docker-compose vs kubernetes</h3>
The docker-compose here is running on a single host with multipul containers. To make the application more resilian to work load changing, can apply k8s as containers orchestration.
<h3>3.2 OpenAPI</h3>
Apply OpenAPI to facilate document generation.</h3>
<h3>3.3 Create docker image first</h3>
The docker-compose.yaml use 2 ways to create container: from a dockerfile and existing image. This is for the purpose of showing 2 alternatives to start container. However, it will be more efficient to create image first then the container can import directly.</h3>