-- Sql Script for Wacode2020

Use Wacode2020

-- Create a user table
CREATE TABLE user(
   Name Varchar(50) NOT NULL,
   Username Varchar(25) NOT NULL PRIMARY KEY,
   Password Varchar(50) NOT NULL,
   ID Varchar(25) NOT NULL
);