<h1>This is for bootcamp activities</h1>

<h2>1. RestAPI</h2>
Dockerfile: Dockerfile_RestAPI.txt
<br>
build command: 
<br>
docker build -t bootcamp:restapi -f Dockerfile_RestAPI.txt .
<br>
image link: https://hub.docker.com/layers/179264454/brianjrmo/bootcamp/restapi/images/sha256-03fa256cc0332b9c1099ae2e860de39a5bf79f6f3e5b4a659413644bb7f9e1e8?context=repo
<br>


<h2>2. MySQL</h2>
sudo docker pull mysql/mysql-server:latest
<br>
sudo docker run --name=bootcamp_mysql --env="MYSQL_ROOT_PASSWORD=bootcamp" --restart on-failure -d mysql/mysql-server
<br>
sudo docker exec -i bootcamp_mysql mysql -uroot -pbootcamp <<< "CREATE USER 'bootcamp'@'%' IDENTIFIED BY 'bootcamp';"
<br>
sudo docker exec -i bootcamp_mysql mysql -uroot -pbootcamp <<< "GRANT ALL PRIVILEGES ON *.* TO 'bootcamp'@'%';"
<br>
sudo docker tag mysql/mysql-server brianjrmo/bootcamp:mysql

<h2>3. Airflow</h2>
<br>
docker build -t bootcamp:restapi -f Dockerfile_Airflow.txt .

<h2>4. Composer</h2>
docker-composer up
