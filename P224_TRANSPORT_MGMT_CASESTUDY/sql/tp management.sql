--creating database
create database cs_transport_management
use cs_transport_management

--table creation

--vehicles table
create table vehicles (
vehicle_id int identity(1,1) primary key,
model varchar(255) not null,
capacity decimal(10, 2) not null,
vehicle_type varchar(50) not null,  
status varchar(50) not null 
);
select * from vehicles




insert into vehicles (model, capacity, vehicle_type, status)
values
('ford f-150', 50.00, 'truck', 'available'),
('chevrolet express', 30.00, 'van', 'available'),
('mercedes sprinter', 25.00, 'van', 'on trip'),
('tesla semi', 80.00, 'truck', 'maintenance'),
('volvo fh', 75.00, 'truck', 'available'),
('toyota coaster', 30.00, 'bus', 'on trip'),
('scania r500', 70.00, 'truck', 'available'),
('ford transit', 25.00, 'van', 'available'),
('volkswagen crafter', 20.00, 'van', 'on trip'),
('renault master', 20.00, 'van', 'maintenance');

--drivers table
CREATE TABLE drivers (
    driver_id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    license_number VARCHAR(100) NOT NULL,
    status VARCHAR(50) NOT NULL
);

ALTER TABLE trips ADD driver_id INT;
ALTER TABLE trips ADD CONSTRAINT FK_driver FOREIGN KEY (driver_id) REFERENCES drivers(driver_id);

INSERT INTO drivers (name, license_number, status) VALUES
('Alice Smith', 'D1234567', 'Available'),
('Bob Johnson', 'D7654321', 'Available'),
('Charlie Brown', 'D1357924', 'Available'),
('Diana Prince', 'D2468013', 'Available'),
('Ethan Hunt', 'D9876543', 'Available');

--routes table
create table routes (
route_id int identity(1,1) primary key,
start_destination varchar(255) not null,
end_destination varchar(255) not null,
distance decimal(10, 2) not null
);



insert into routes (start_destination, end_destination, distance)
values 
('new york', 'los angeles', 4500.00),
('chicago', 'houston', 1500.00),
('miami', 'atlanta', 600.00),
('san francisco', 'las vegas', 800.00),
('seattle', 'portland', 200.00),
('dallas', 'denver', 1200.00),
('boston', 'philadelphia', 300.00),
('phoenix', 'san diego', 350.00),
('orlando', 'tampa', 100.00),
('detroit', 'cleveland', 150.00);


--trips table
create table trips (
trip_id int identity(1,1) primary key,
vehicle_id int, 
route_id int, 
departure_date datetime not null,
arrival_date datetime not null,
status varchar(50) not null, 
trip_type varchar(50) default 'freight',
max_passengers int,
constraint fk_trips_routes_rid foreign key(route_id) references routes(route_id),
constraint fk_trips_routes_vid foreign key(vehicle_id) references vehicles(vehicle_id),
);

insert into trips ( departure_date, arrival_date, status, trip_type, max_passengers)
values 
('2024-10-01 08:00:00', '2024-10-04 18:00:00', 'scheduled', 'freight', null),
( '2024-10-02 09:00:00', '2024-10-03 19:00:00', 'scheduled', 'passenger', 15),
('2024-10-01 07:00:00', '2024-10-01 17:00:00', 'in progress', 'freight', null),
( '2024-09-30 06:00:00', '2024-09-30 20:00:00', 'completed', 'passenger', 25),
( '2024-09-28 10:00:00', '2024-09-28 15:00:00', 'cancelled', 'freight', null),
( '2024-10-03 07:30:00', '2024-10-03 11:30:00', 'scheduled', 'passenger', 20),
('2024-09-29 12:00:00', '2024-09-29 18:00:00', 'completed', 'freight', null),
( '2024-10-01 14:00:00', '2024-10-01 20:00:00', 'in progress', 'passenger', 18),
('2024-09-27 05:00:00', '2024-09-27 09:00:00', 'completed', 'freight', null),
('2024-09-30 13:00:00', '2024-09-30 15:30:00', 'scheduled', 'passenger', 10);





--passengers table
create table passengers (
passenger_id int identity(1,1) primary key,
first_name varchar(255) not null,
gender varchar(255) not null,
age int not null,
email varchar(255) unique not null,
phone_no varchar(50) unique not null
);

insert into passengers (first_name, gender, age, email, phone_no)
values 
('johny', 'male', 32, 'john123@gmail.com', '123-456-7890'),
('lilly', 'female', 28, 'lilly234@gmailcom', '123-456-7891'),
('dais', 'male', 45, 'michael345@gmail.com', '123-456-7892'),
('saran', 'female', 35, 'sarah444@gmail.com', '123-456-7893'),
('david', 'male', 29, 'david567@gmail.com', '123-456-7894'),
('launa', 'female', 24, 'launa556@gmail.com', '123-456-7895'),
('james', 'male', 40, 'james456@gmail.com', '123-456-7896'),
('olivia', 'female', 30, 'olivia334@gmail.com', '123-456-7897'),
('william', 'male', 33, 'william123@gmail.com', '123-456-7898'),
('sophia', 'female', 27, 'sophia234@gmail.com', '123-456-7899');




--bookings table
create table bookings (
booking_id int identity(1,1) primary key,
trip_id int,
passenger_id int, 
booking_date datetime not null,
status varchar(50) not null,
constraint fk_bookings_trips_tid foreign key(trip_id) references trips(trip_id),
constraint fk_bookings_trips_pid foreign key(passenger_id) references passengers(passenger_id)
);

insert into bookings(booking_date, status)
values 
('2024-09-25 10:00:00', 'confirmed'),
( '2024-09-25 11:00:00', 'confirmed'),
( '2024-09-20 14:30:00', 'completed'),
( '2024-09-20 15:00:00', 'completed'),
('2024-09-29 09:00:00', 'confirmed'),
( '2024-09-29 09:30:00', 'confirmed'),
( '2024-09-27 12:00:00', 'in progress'),
( '2024-09-27 12:15:00', 'in progress'),
( '2024-09-28 08:45:00', 'scheduled'),
('2024-09-28 09:00:00', 'scheduled');




select * from vehicles
select * from drivers
select * from routes
select * from trips
select * from passengers
select * from bookings


TRUNCATE TABLE drivers;
