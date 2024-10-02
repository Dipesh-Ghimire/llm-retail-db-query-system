-- Create the database
CREATE DATABASE neptech_store;
USE neptech_store;

-- Create the laptops table
CREATE TABLE laptops (
    laptop_id INT AUTO_INCREMENT PRIMARY KEY,
    brand ENUM('Dell', 'HP', 'Lenovo', 'Apple', 'Asus') NOT NULL,
    processor ENUM('i3', 'i5', 'i7', 'Ryzen 5', 'Ryzen 7') NOT NULL,
    ram ENUM('4GB', '8GB', '16GB', '32GB') NOT NULL,
    storage ENUM('256GB SSD', '512GB SSD', '1TB SSD', '1TB HDD') NOT NULL,
    price INT CHECK (price BETWEEN 300 AND 2000),
    stock_quantity INT NOT NULL,
    UNIQUE KEY brand_processor_ram_storage (brand, processor, ram, storage)
);

-- Create the discounts table
CREATE TABLE laptop_discounts (
    discount_id INT AUTO_INCREMENT PRIMARY KEY,
    laptop_id INT NOT NULL,
    pct_discount DECIMAL(5,2) CHECK (pct_discount BETWEEN 0 AND 100),
    FOREIGN KEY (laptop_id) REFERENCES laptops(laptop_id)
);

-- Create a stored procedure to populate the laptops table
DELIMITER $$
CREATE PROCEDURE PopulateLaptops()
BEGIN
    DECLARE counter INT DEFAULT 0;
    DECLARE max_records INT DEFAULT 100;
    DECLARE brand ENUM('Dell', 'HP', 'Lenovo', 'Apple', 'Asus');
    DECLARE processor ENUM('i3', 'i5', 'i7', 'Ryzen 5', 'Ryzen 7');
    DECLARE ram ENUM('4GB', '8GB', '16GB', '32GB');
    DECLARE storage ENUM('256GB SSD', '512GB SSD', '1TB SSD', '1TB HDD');
    DECLARE price INT;
    DECLARE stock INT;

    -- Seed the random number generator
    SET SESSION rand_seed1 = UNIX_TIMESTAMP();

    WHILE counter < max_records DO
        -- Generate random values
        SET brand = ELT(FLOOR(1 + RAND() * 5), 'Dell', 'HP', 'Lenovo', 'Apple', 'Asus');
        SET processor = ELT(FLOOR(1 + RAND() * 5), 'i3', 'i5', 'i7', 'Ryzen 5', 'Ryzen 7');
        SET ram = ELT(FLOOR(1 + RAND() * 4), '4GB', '8GB', '16GB', '32GB');
        SET storage = ELT(FLOOR(1 + RAND() * 4), '256GB SSD', '512GB SSD', '1TB SSD', '1TB HDD');
        SET price = FLOOR(300 + RAND() * 1701); -- Price between $300 and $2000
        SET stock = FLOOR(10 + RAND() * 91);

        -- Insert a new record, ignoring duplicates due to unique constraint
        BEGIN
            DECLARE CONTINUE HANDLER FOR 1062 BEGIN END;  -- Handle duplicate key error
            INSERT INTO laptops (brand, processor, ram, storage, price, stock_quantity)
            VALUES (brand, processor, ram, storage, price, stock);
            SET counter = counter + 1;
        END;
    END WHILE;
END$$
DELIMITER ;

-- Call the stored procedure to populate the laptops table
CALL PopulateLaptops();

-- Insert at least 10 records into the laptop_discounts table
INSERT INTO laptop_discounts (laptop_id, pct_discount)
VALUES
(1, 10.00),
(2, 20.00),
(3, 15.00),
(4, 5.00),
(5, 25.00),
(6, 30.00),
(7, 35.00),
(8, 40.00),
(9, 45.00),
(10, 50.00);
