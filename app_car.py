import streamlit as st
import pandas as pd
import xgboost as xgb

def main():
    st.title("Car Price Prediction")

    # Load the model
    model = xgb.XGBRegressor()
    model.load_model('xgb_model_car.json')

    # Inputs from the user
    age = st.number_input('Age of Car?', 0, 63, step=1)
    kms_driven = st.number_input('What is the distance completed by the car in kilometers?', 00, 6500000, step=100)
    mileage = st.number_input('Mileage of car(in kmpl, kmpkg, kWh)?',0.0, 33.54, step=1.0)
    engine = st.number_input('Engine of car (in CC)?',00, 5998, step=10)
    power = st.number_input('Power of your car (in bhp)?',0.0,560.0, step=10.0)
    seats = st.number_input('Number of seats in car?', 0, 10, step=2)

    # Brands, including all those expected by the model
    brands = [
        "Manufacturer_Ambassador", "Manufacturer_Audi", "Manufacturer_BMW",
        "Manufacturer_Bentley", "Manufacturer_Chevrolet", "Manufacturer_Datsun",
        "Manufacturer_Fiat", "Manufacturer_Force", "Manufacturer_Ford",
        "Manufacturer_Honda", "Manufacturer_Hyundai", "Manufacturer_ISUZU",
        "Manufacturer_Isuzu", "Manufacturer_Jaguar", "Manufacturer_Jeep",
        "Manufacturer_Lamborghini", "Manufacturer_Land", "Manufacturer_Mahindra",
        "Manufacturer_Maruti", "Manufacturer_Mercedes-Benz", "Manufacturer_Mini",
        "Manufacturer_Mitsubishi", "Manufacturer_Nissan", "Manufacturer_Porsche",
        "Manufacturer_Renault", "Manufacturer_Skoda", "Manufacturer_Smart",
        "Manufacturer_Tata", "Manufacturer_Toyota", "Manufacturer_Volkswagen",
        "Manufacturer_Volvo"
    ]
    selected_brand = st.selectbox("Select your car's brand", brands)

    # Fuel types, including all those expected by the model
    fuels = ["Fuel_Type_CNG", "Fuel_Type_Diesel", "Fuel_Type_Electric", "Fuel_Type_LPG", "Fuel_Type_Petrol"]
    selected_fuel = st.selectbox("Select your car's fuel type", fuels)

    # Transmission types
    transmissions = ["Transmission_Manual", "Transmission_Automatic"]
    selected_transmission = st.selectbox("Select your car's transmission type", transmissions)

    # Owner types
    owners = ["Owner_Type_First", "Owner_Type_Second", "Owner_Type_Third", "Owner_Type_Fourth & Above"]
    selected_owner = st.selectbox("Select your car's owner type", owners)

    # Initialize the data dictionary with all expected features
    data_dict = {feature: [0] for feature in model.get_booster().feature_names}

    # Update the dict with the user input
    data_dict.update({
        'Year': [age],
        'Kilometers_Driven': [kms_driven],
        'Mileage': [mileage],
        'Engine': [engine],
        'Power': [power],
        'Seats': [seats],
        selected_brand: [1],
        selected_fuel: [1],
        selected_transmission: [1],
        selected_owner: [1]
    })

    # Create DataFrame from dict
    data_new = pd.DataFrame(data_dict)

    if st.button('Predict'):
        try:
            pred = model.predict(data_new)
            if pred > 0:
                st.success(f'You can sell the car for ₹{pred[0]:.2f} lakhs.')
            else:
                st.warning("This car may not be sellable at a meaningful price.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
