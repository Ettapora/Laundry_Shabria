from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# GANTI INI SAMA URL KONEKSI DARI DASHBOARD TIDB LU
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://3gEW8w9g8ZZf3e4.root:mONkrvzp2AeJj8Gz@gateway01.ap-southeast-1.prod.alicloud.tidbcloud.com:4000/shabria_laundry?ssl_verify_cert=true&ssl_verify_identity=true"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()