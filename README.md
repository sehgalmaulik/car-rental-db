# Car Rental Project
This project is a simple car rental management system implemented in Python 3 using the Tkinter library for the graphical user interface and SQLite3 for the database.

## Prerequisites
Python 3: If you don't have Python 3 installed, you can download it from the official website. The Tkinter and SQLite3 libraries come bundled with the Python installation, so you don't need to install them separately.

## Creating the Database
Navigate to the directory where you want to create the database, or where you have an existing database.

Run the following command to create a new database: `````sqlite3 .open car-rental.db`````

Run the following commands to create the necessary tables for the database:
`````
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
   FOREIGN KEY (CustID) references CUSTOMER(CustID) on update CASCADE on delete
RESTRICT,
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
`````
## Loading the Database
Now, import the data into the database using the following commands:
`````
.mode box
.import --csv --skip 1 CUSTOMER.csv CUSTOMER
.import --csv --skip 1 RATE.csv RATE
.import --csv --skip 1 RENTAL.csv RENTAL
.import --csv --skip 1 VEHICLE.csv VEHICLE
`````
Note: The --csv --skip 1 option skips the first row in the CSV file as it contains the headers and not actual data.

## Running the Application
To run the application, open a shell and run the following command: 
`````python3 codep3.py`````

The graphical user interface should open and look like the image below.

![gui](https://raw.githubusercontent.com/sehgalmaulik/car-rental-db/main/data/gui.png)

This project is a good example of a simple database-driven application implemented in Python. It can be extended and modified to suit your specific requirements.

## Contributing
If you would like to contribute to the project, please submit bug reports, feature requests, or pull requests. You can also check out the list of issues or fork the repository and create your own version.

## Contact
If you have any questions or feedback, please feel free to contact the author.

## Copyright 

Copyright © 2023. All rights reserved.

This software is provided for educational purposes only. It is prohibited to use this code, for any college assignment or personal use. Unauthorized distribution, modification or commercial usage is strictly forbidden. Please respect the rights of the author.
