from sqlalchemy.orm import Session

from database.models import Transaction


def create_transaction(
    db: Session,
    transaction_time: float,
    amount: float,
    prediction: int,
    fraud_probability: float,
):
    """
    Create a transaction record.
    """

    transaction = Transaction(
        transaction_time=transaction_time,
        amount=amount,
        prediction=prediction,
        fraud_probability=fraud_probability,
    )

    db.add(transaction)

    db.commit()

    db.refresh(transaction)

    return transaction