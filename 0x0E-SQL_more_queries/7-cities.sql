-- create a database called hbtn_0d_usa and table called cities
-- create hbtn_0d_usa database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use the new table
USE hbtn_0d_usa;
-- create states table
CREATE TABLE IF NOT EXISTS
cities(id INT AUTO_INCREMENT UNIQUE NOT NULL, state_id INT NOT NULL,
name VARCHAR(256), PRIMARY KEY (id),
FOREIGN KEY(state_id) REFERENCES states(id));
