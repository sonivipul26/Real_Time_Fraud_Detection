from sqlalchemy.orm import Session

from database.models import Transaction

from utils.logger import logger

def create_transaction(
    db,
    transaction_time,
    amount,
    prediction,
    fraud_probability
):

    logger.info("Creating Transaction Object")

    transaction = Transaction(

        transaction_time=transaction_time,

        amount=amount,

        prediction=prediction,

        fraud_probability=fraud_probability

    )

    logger.info("Adding Transaction To Database Session")

    db.add(transaction)

    logger.info("Committing Transaction")

    db.commit()

    logger.info("Refreshing Database Object")

    db.refresh(transaction)

    logger.info(
        f"Transaction Saved Successfully (ID={transaction.id})"
    )

    return transaction