from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# ==========================================
# Database Configuration
# ==========================================

DATABASE_URL = (
    "postgresql://postgres:vipul@localhost:5432/fraud_detection"
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