-- convert database to UTF8
-- convert database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- select hbtn_0c_0 database
USE hbtn_0c_0
-- convert first_table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
