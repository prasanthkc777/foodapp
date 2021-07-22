It is a simple food application with python & mysql. 
step 1: make sure python,mysql,flask,msql-db-connector was installed.
step 2: connect database by enter your password.
step 3: create a database with name, "fooddelivery". i.e.. create database fooddelivery;
step 4: activate database. i.e.. use fooddelivery;
step 5: create table with name, fooddetails and insert given data in code
         i.e.. insert into fooddetails(foodname,cost) values("Idly","10");
               insert into fooddetails(foodname,cost) values("Dosa","20");
               insert into fooddetails(foodname,cost) values("Meal","30");
               insert into fooddetails(foodname,cost) values("Biriyani","40");
               insert into fooddetails(foodname,cost) values("Parotta","50");
step 6:  create table with name, orderdetails. 
          i.e.. create table orderdetails(username varchar(255),foodordered varchar(255), totalcost varchar(255));
step 7:  create table with name, userdetails.   
           i.e.. create table userdetails(userid int NOT NULL AUTO_INCREMENT,username varchar(255),password varchar(255),mail varchar(255) , phone varchar(255) , address varchar(255), PRIMARY KEY (userid));
step 8:  change password of database in "app.py" file, line 2.
step 9:  save & execute your code.
