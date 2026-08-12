-- Database creation and setup for Bakery Management System
CREATE DATABASE IF NOT EXISTS BMS;
USE BMS;

-- Table structure for table `Products`
CREATE TABLE IF NOT EXISTS Products (
    ItNo INT(6) UNIQUE,
    Category VARCHAR(25),
    Item VARCHAR(25),
    Stock INT,
    Price INT
);

-- Initial seed data (Optional)
INSERT INTO Products (ItNo, Category, Item, Stock, Price) VALUES
(1, 'JUICE', 'ORANGE JUICE', 70, 50),
(2, 'CAKE', 'BLACK FOREST', 25, 450),
(3, 'CAKE', 'WHITE FOREST', 29, 650),
(4, 'CAKE', 'RED VELVET', 33, 560),
(5, 'SHAKE', 'OREO SHAKE', 58, 80),
(6, 'PUFFS', 'VEG. PUFFS', 60, 15),
(7, 'PUFFS', 'EGG PUFFS', 70, 18),
(8, 'ROLLS', 'VEG.ROLL', 50, 45),
(9, 'SAMOSA', 'SAMOSA', 56, 20),
(10, 'CUTLET', 'CHICKEN CUTLET', 50, 20);
