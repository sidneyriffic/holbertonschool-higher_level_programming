-- create a user on server and assign all privileges
-- create user
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
-- assign all privileges to everything
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
