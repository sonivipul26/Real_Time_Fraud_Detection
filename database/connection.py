import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

# ==========================================
# Database Configuration
# ==========================================

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


# ==========================================
# SQLAlchemy Engine
# ==========================================

engine = create_engine(
    DATABASE_URL,
    echo=True
)

# ==========================================
# Session Factory
# ==========================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ==========================================
# Database Dependency
# ==========================================

def get_db():
    """
    Create database session for every request.
    """

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()

# ==========================================
# Base Class
# ==========================================

Base = declarative_base()