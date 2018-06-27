-- create a database and a user with SELECT perms on it
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create user
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY "user_0d_2_pwd";
-- assign SELECT permission
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
