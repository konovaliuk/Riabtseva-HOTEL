use pis_hostel;

create table roles(
    role_id INT NOT NULL AUTO_INCREMENT,
    role_title VARCHAR(255),
    PRIMARY KEY (role_id)
);
create table room(
    room_prise INT NOT NULL,
    room_id INT NOT NULL ,
    room_type VARCHAR(255) NOT NULL,
    max_capacity INT NOT NULL,
    PRIMARY KEY (room_id, room_type)
);
create table users (
    user_id BIGINT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role_id INT,
    PRIMARY KEY (user_id),
    FOREIGN KEY(role_id) REFERENCES roles(role_id)
);
create table booking(
    booking_id BIGINT NOT NULL AUTO_INCREMENT,
    user_id BIGINT NOT NULL,
    room_id INT NOT NULL ,
    room_type VARCHAR(255) NOT NULL,
    booking_data DATE NOT NULL,
    check_in_date DATETIME NOT NULL,
    check_out_date DATETIME NOT NULL,
    PRIMARY KEY (booking_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (room_id, room_type) REFERENCES room(room_id, room_type)
);

create table payment(
    payment_id BIGINT NOT NULL AUTO_INCREMENT,
    booking_id BIGINT NOT NULL,
    PRIMARY KEY (payment_id),
    FOREIGN KEY (booking_id) REFERENCES booking(booking_id)
)
