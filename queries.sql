-- Task 1
--Note: Change price to float??????
create table VEHICLE(
    VehicleID VARCHAR(17) NOT NULL ,
    Description VARCHAR(50) NOT NULL,
    Year INT NOT NULL,
    Type INT NOT NULL,
    Category INT NOT NULL, 
    PRIMARY KEY (VehicleID),
    FOREIGN KEY (Type, Category) references RATE(Type, Category)
);
    
create table RENTAL( 
    CustID INT NOT NULL,
    VehicleID VARCHAR(17) NOT NULL,
    StartDate DATE NOT NULL,
    OrderDate DATE NOT NULL,
    RentalType INT NOT NULL,
    Qty INT NOT NULL,
    ReturnDate DATE NOT NULL,
    TotalAmount INT NOT NULL,
    PaymentDate DATE,
    FOREIGN KEY (CustID) references CUSTOMER(CustID) on update CASCADE on delete RESTRICT,
    FOREIGN KEY (VehicleID) references VEHICLE(VehicleID)

);

create table CUSTOMER(
    CustID INTEGER PRIMARY KEY AUTOINCREMENT, 
    Name VARCHAR(30),
    Phone VARCHAR(13)
);
    
create table RATE(
    Type INT NOT NULL,
    Category INT NOT NULL,
    Weekly INT NOT NULL,
    Daily INT NOT NULL,
    PRIMARY KEY (Type, Category)
);

-- 2 


.import --csv --skip 1 CUSTOMER.csv CUSTOMER
.import --csv --skip 1 RATE.csv RATE
.import --csv --skip 1 RENTAL.csv RENTAL
.import --csv --skip 1 VEHICLE.csv VEHICLE

-- couting the number of records
SELECT COUNT(*) FROM CUSTOMER ;
SELECT COUNT(*) FROM RATE ;
SELECT COUNT(*) FROM VEHICLE ;
SELECT COUNT(*) FROM RENTAL ;

--3 

-- q1
insert into CUSTOMER (Name,Phone) VALUES ('M. Sehgal','(682) 521-8679');

-- q2
UPDATE CUSTOMER
SET Phone = '(837) 721-8965'
WHERE
    Name = 'M. Sehgal'; 

-- q3
UPDATE RATE
SET Daily = Daily*1.05
where Category = 1;
--q4
    -- a
    INSERT INTO VEHICLE VALUES ("5FNRL6H58KB133711","Honda Odyssey",2019,6,1);
    --b
    INSERT INTO RATE VALUES (5,1,900,150),(6,1,800,135);


 -- q5 (PROBLEM)
SELECT DISTINCT V.VehicleID, Description, Year, 
SUM(R.Qty * R.RentalType) AS 'Days Rented'
FROM VEHICLE AS V,RENTAL AS R 
WHERE V.VehicleID=R.VehicleID AND 
V.Type=1 AND V.Category=1 AND R.vehicleID NOT IN
(SELECT R.VehicleID 
FROM RENTAL AS R 
WHERE  
(R.StartDate Between '2019-06-01' AND '2019-06-20')  
OR 
(R.ReturnDate Between '2019-06-01' AND '2019-06-20'))
Group BY V.VehicleID;

-- q6


SELECT COUNT(*) AS 'ROWS RETURNED'
FROM CUSTOMER AS C, RENTAL AS R WHERE  
    C.CustID = R.CustID and R.CustID = 221 and R.PaymentDate = 'NULL';
    
--q7

SELECT COUNT(*) AS 'ROWS RETURNED'
FROM VEHICLE,RATE 
WHERE VEHICLE.Type = RATE.Type AND VEHICLE.Category = RATE.Category
ORDER BY VEHICLE.Category DESC, VEHICLE.Type ;


-- q8
SELECT COUNT(*) AS 'ROWS RETURNED',sum(TotalAmount) as TotalMoney from RENTAL where PaymentDate <> 'NULL'; 



--9a

SELECT V.Description,V.Year,
CASE V.Type
    WHEN 1  THEN 'Compact'
    WHEN 2  THEN 'Medium'
    WHEN 3  THEN 'Large'
    WHEN 4  THEN 'SUV'
    WHEN 5  THEN 'Truck'
    WHEN 6  THEN 'VAN'
END AS VehicleType,
CASE V.Category
    WHEN 0 THEN 'Basic'
    WHEN 1 THEN 'Luxury'
END as VehicleCategory,
R.TotalAmount/(R.Qty* R.RentalType) as 'Unit price',
CASE R.RentalType
    WHEN 1 THEN R.Qty || ' Day(s)'
    WHEN 7 THEN R.Qty || ' Week(s)'
END AS 'Total Duration',
R.TotalAmount,
CASE R.PaymentDate
    WHEN 'NULL' THEN 'Required'
    ELSE 'Completed'
END AS Payment    
FROM RENTAL AS R, CUSTOMER AS C, VEHICLE AS V
WHERE C.Name = 'J. Brown' AND V.VehicleID = R.VehicleID AND C.CustID = R.CustID
ORDER BY R.StartDate;


SELECT COUNT(*) AS 'ROWS RETURNED'
FROM RENTAL AS R, CUSTOMER AS C, VEHICLE AS V
WHERE C.Name = 'J. Brown' AND V.VehicleID = R.VehicleID AND C.CustID = R.CustID
ORDER BY R.StartDate;







--9b
--Assuming that the current balance is the amount he has to pay and not what he has already paid. 
SELECT SUM(R.TotalAmount) AS 'Current Balance' FROM RENTAL AS R,CUSTOMER AS C WHERE R.PaymentDate = 'NULL' 
AND C.Name = 'J. Brown' AND C.CustID = R.CustID;

SELECT COUNT(*) AS 'ROWS RETURNED' FROM RENTAL AS R,CUSTOMER AS C WHERE R.PaymentDate = 'NULL' 
AND C.Name = 'J. Brown' AND C.CustID = R.CustID;

--10

SELECT  C.Name, R.StartDate, R.ReturnDate, R.TotalAmount FROM CUSTOMER AS C,
RENTAL AS R WHERE R.RentalType = 7 AND R.CustID = C.CustID AND R.VehicleID = '19VDE1F3XEE414842' AND R.PaymentDate = 'NULL';


SELECT COUNT(*) AS 'ROWS RETURNED' FROM CUSTOMER AS C,RENTAL AS R WHERE R.RentalType = 7 AND R.CustID = C.CustID AND R.VehicleID = '19VDE1F3XEE414842' AND R.PaymentDate = 'NULL';


--11 

SELECT * FROM CUSTOMER WHERE not exists (select * FROM  RENTAL WHERE CUSTOMER.CustID = RENTAL.CustID);
SELECT COUNT(*) AS 'ROWS RETURNED' FROM CUSTOMER WHERE not exists (select * FROM  RENTAL WHERE CUSTOMER.CustID = RENTAL.CustID);

--12

SELECT C.Name, V.Description, R.StartDate, R.ReturnDate, R.TotalAmount , C.CustID
FROM CUSTOMER AS C, RENTAL AS R, VEHICLE AS V WHERE
C.CustID = R.CustID AND R.VehicleID = V.VehicleID AND R.StartDate = R.PaymentDate
ORDER BY C.Name;

SELECT COUNT(*) AS 'ROWS RETURNED'
FROM CUSTOMER AS C, RENTAL AS R, VEHICLE AS V WHERE
C.CustID = R.CustID AND R.VehicleID = V.VehicleID AND R.StartDate = R.PaymentDate
ORDER BY C.Name;

-- SELECT V.VehicleID AS VIN ,V.Description, V.Year FROM VEHICLE as V, RENTAL as R 
-- WHERE V.Type =1 AND V.Category =1 AND V.VehicleID = R.VehicleID AND 
-- R.StartDate  2019-06-01 OR R.ReturnDate > 2019-06-20 GROUP BY V.VehicleID;















 INSERT INTO RENTAL VALUES (229,'WAUTFAFH0E0010613','2019-06-02','2019-04-12',1,17,'2019-06-19',400,'2019-05-06')