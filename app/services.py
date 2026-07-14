from ml.predict import predict
from ml.predict import predict_probability

from database.crud import create_transaction


def predict_transaction(request, db):

    features = request.to_feature_list()

    prediction = predict(features)

    probability = predict_probability(features)

    create_transaction(

        db=db,

        transaction_time=request.Time,

        amount=request.Amount,

        prediction=prediction,

        fraud_probability=probability

    )

    return {

        "prediction": prediction,

        "fraud_probability": probability

    }