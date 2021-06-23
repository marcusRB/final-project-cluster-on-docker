INSERT INTO sales
(uuid, total, sale_date, created_at, city, country, latitude, longitude)
VALUES('675867b9-e318-44be-8560-774e59601340', 10.66, now(), now(), 'madrid', 'spain', 40.42841, -3.70496);


INSERT INTO fraud
(uuid, created_at, fraud_type)
VALUES('675867b9-e318-44be-8560-774e59601340', now(), 1);