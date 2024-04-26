import joblib
import housing_market_trends as m
rf_model = m.train_housing_model()
joblib.dump(rf_model, 'rf_model.pkl')
