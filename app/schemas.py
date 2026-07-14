from pydantic import BaseModel


# ==========================================
# Health Response
# ==========================================

class HealthResponse(BaseModel):
    status: str
    model: str
    version: str


# ==========================================
# Prediction Request
# ==========================================

class PredictionRequest(BaseModel):

    Time: float

    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float

    Amount: float

    def to_feature_list(self):

        return [

            self.Time,

            self.V1,
            self.V2,
            self.V3,
            self.V4,
            self.V5,
            self.V6,
            self.V7,
            self.V8,
            self.V9,
            self.V10,
            self.V11,
            self.V12,
            self.V13,
            self.V14,
            self.V15,
            self.V16,
            self.V17,
            self.V18,
            self.V19,
            self.V20,
            self.V21,
            self.V22,
            self.V23,
            self.V24,
            self.V25,
            self.V26,
            self.V27,
            self.V28,

            self.Amount

        ]


# ==========================================
# Prediction Response
# ==========================================

class PredictionResponse(BaseModel):

    prediction: int

    fraud_probability: float