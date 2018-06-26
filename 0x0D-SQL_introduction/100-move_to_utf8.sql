-- convert database to UTF8
-- convert database to UTF8
ALTER DATABASE databasename CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- convert first_table to UTF8
ALTER TABLE tablename CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
