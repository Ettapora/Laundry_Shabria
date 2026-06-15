from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .database import Base


class Role(Base):
    __tablename__ = "roles"
    id_role = Column(Integer, primary_key=True, index=True)
    nama_role = Column(String(50), unique=True, index=True)
    deskripsi = Column(String(255), nullable=True)

class User(Base):
    __tablename__ = "users"
    id_user = Column(Integer, primary_key=True, index=True)
    id_role = Column(Integer, ForeignKey("roles.id_role"))
    first_name = Column(String(50))
    last_name = Column(String(50), nullable=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255))
    nomor_telepon = Column(String(20), nullable=True)
    alamat = Column(String(255), nullable=True)
    status_aktif = Column(Boolean, default=True)    