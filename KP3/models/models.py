from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'
    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_title = Column(String(255))

class Room(Base):
    __tablename__ = 'room'
    room_prise = Column(Integer, nullable=False)
    room_id = Column(Integer, primary_key=True)
    room_type = Column(String(255), nullable=False)
    max_capacity = Column(Integer, nullable=False)
    status = Column(String(255))

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.role_id'))
    role = relationship('Role')

class Booking(Base):
    __tablename__ = 'booking'
    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    room_id = Column(Integer, nullable=False)
    room_type = Column(String(255), nullable=False)
    check_in_date = Column(DateTime, nullable=False)
    check_out_date = Column(DateTime, nullable=False)
    number_people = Column(Integer, nullable=False)
    user = relationship('User')
    room = relationship('Room')

class Payment(Base):
    __tablename__ = 'payment'
    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    booking_id = Column(Integer, ForeignKey('booking.booking_id'))
    booking = relationship('Booking')

