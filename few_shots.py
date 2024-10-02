few_shots_list = [
    {'Question' : "How many Asus laptops with 8GB RAM and 512GB SSD are left in stock?",
     'SQLQuery' : "SELECT sum(stock_quantity) FROM laptops WHERE brand = 'Asus' AND ram = '8GB' AND storage = '512GB SSD'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "95"},

    {'Question': "What is the total price of the inventory for all HP laptops with 16GB RAM?",
     'SQLQuery':"SELECT SUM(price * stock_quantity) FROM laptops WHERE brand = 'HP' AND ram = '16GB'",
     'SQLResult': "Result of the SQL query",
     'Answer': "188108"},

    {'Question': "If I sell all Lenovo laptops with i7 processors today after discounts, how much revenue will the store generate?",
     'SQLQuery' : """SELECT sum(a.total_amount * ((100 - COALESCE(laptop_discounts.pct_discount, 0)) / 100)) as total_revenue 
                     FROM (SELECT SUM(price * stock_quantity) as total_amount, laptop_id 
                           FROM laptops WHERE brand = 'Lenovo' AND processor = 'i7' 
                           GROUP BY laptop_id) a 
                     LEFT JOIN laptop_discounts ON a.laptop_id = laptop_discounts.laptop_id""",
     'SQLResult': "Result of the SQL query",
     'Answer': "125000"},

    {'Question' : "How much revenue will the store generate if I sell all Apple laptops today without any discounts?",
     'SQLQuery': "SELECT SUM(price * stock_quantity) FROM laptops WHERE brand = 'Apple'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "556261"},

    {'Question': "How many Lenovo laptops with 256GB SSD are in stock?",
     'SQLQuery' : "SELECT sum(stock_quantity) FROM laptops WHERE brand = 'Lenovo' AND storage = '256GB SSD'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "245"},

    {'Question': "What will be the total sales amount if I sell all Apple laptops with 16GB RAM and 1TB HDD today after discounts?",
     'SQLQuery' : """SELECT SUM(a.total_amount * ((100 - COALESCE(laptop_discounts.pct_discount, 0)) / 100)) AS total_revenue FROM (
                        SELECT SUM(price * stock_quantity) AS total_amount, laptop_id 
                        FROM laptops WHERE brand = 'Apple' AND ram = '16GB' AND storage = '1TB HDD' 
                        GROUP BY laptop_id) a LEFT JOIN laptop_discounts ON a.laptop_id = laptop_discounts.laptop_id;""",
     'SQLResult': "Result of the SQL query",
     'Answer' : "34095.6"},
    {'Question': "If I sell all my Apple laptops today with discounts applied, how much revenue our store will generate (post discounts)?",
     'SQLQuery' : """SELECT sum(a.total_amount * ((100 - COALESCE(laptop_discounts.pct_discount, 0)) / 100)) as total_revenue 
                     FROM (SELECT SUM(price * stock_quantity) as total_amount, laptop_id 
                           FROM laptops WHERE brand = 'Apple' 
                           GROUP BY laptop_id) a 
                     LEFT JOIN laptop_discounts ON a.laptop_id = laptop_discounts.laptop_id""",
     'SQLResult': "Result of the SQL query",
     'Answer' : "541648.6"}
]
