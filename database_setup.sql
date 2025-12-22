CREATE DATABASE finance_db;
USE finance_db;

CREATE TABLE companies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    industry VARCHAR(50)
);

CREATE TABLE statements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_id INT,
    type VARCHAR(50),
    period DATE,
    revenue DECIMAL(15,2),
    net_income DECIMAL(15,2),
    assets DECIMAL(15,2),
    liabilities DECIMAL(15,2)
);
