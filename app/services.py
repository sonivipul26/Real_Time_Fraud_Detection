from ml.predict import predict
from ml.predict import predict_probability


def predict_transaction(request):

    features = [

        request.Time,

        request.V1,
        request.V2,
        request.V3,
        request.V4,
        request.V5,
        request.V6,
        request.V7,
        request.V8,
        request.V9,
        request.V10,
        request.V11,
        request.V12,
        request.V13,
        request.V14,
        request.V15,
        request.V16,
        request.V17,
        request.V18,
        request.V19,
        request.V20,
        request.V21,
        request.V22,
        request.V23,
        request.V24,
        request.V25,
        request.V26,
        request.V27,
        request.V28,

        request.Amount

    ]

    prediction = predict(features)

    probability = predict_probability(features)

    return {
        "prediction": prediction,
        "fraud_probability": probability
    }