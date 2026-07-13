from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy import func

from database.connection import Base


class Transaction(Base):
    """
    Transaction table.
    """

    __tablename__ = "transactions"

    # -----------------------------------
    # Primary Key
    # -----------------------------------

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # -----------------------------------
    # Transaction Features
    # -----------------------------------

    transaction_time = Column(
        Float,
        nullable=False
    )

    amount = Column(
        Float,
        nullable=False
    )

    # -----------------------------------
    # Prediction
    # -----------------------------------

    prediction = Column(
        Integer,
        nullable=False
    )

    fraud_probability = Column(
        Float,
        nullable=False
    )

    # -----------------------------------
    # Timestamp
    # -----------------------------------

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )