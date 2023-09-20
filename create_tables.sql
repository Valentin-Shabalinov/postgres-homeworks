-- SQL-команды для создания таблиц

CREATE DATABASE north;
-- создание БД north

\c north
-- переход в БД north

CREATE TABLE employees
(
	employee_id varchar UNIQUE NOT NULL,
	first_name varchar(20) NOT NULL,
	last_name varchar(20) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date varchar(20) NOT NULL,
	notes text
);

CREATE TABLE customers
(
	customer_id varchar UNIQUE NOT NULL,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50) NOT NULL
);

CREATE TABLE orders
(
	order_id varchar UNIQUE NOT NULL,
	customer_id varchar NOT NULL,
	employee_id varchar NOT NULL,
	order_date varchar(20) NOT NULL,
	ship_city varchar(50) NOT NULL
);