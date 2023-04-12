INSERT INTO roles(role_title) VALUES ('admin'), ('user');

INSERT INTO users ( first_name, last_name, email, password, role_id ) VALUES
('Ann', 'Ruab', 'ruab@gmail.com', 'somepassword', 1),
( 'Random', 'Number', 'number1@mail.com', 'somepassword', 2 );

INSERT INTO room (room_prise, room_id, room_type, max_capacity) VALUES
(120, 11, 'normal', 2);

INSERT INTO booking (user_id, room_id, room_type, booking_data, check_in_date, check_out_date) VALUES
(1, 11, 'normal', '2023-02-12', '2023-02-20','2023-02-24');

INSERT INTO payment (booking_id) VALUES (3);
