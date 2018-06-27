-- create a database called hbtn_0d_usa and table called states
-- create hbtn_0d_usa database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use the new table
USE hbtn_0d_usa;
-- create states table
CREATE TABLE IF NOT EXISTS
states(id INT AUTO_INCREMENT UNIQUE NOT NULL,
name VARCHAR(256), PRIMARY KEY (id));
