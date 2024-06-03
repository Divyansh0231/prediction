import streamlit as st
import pandas as pd
import xgboost as xgb

def main():
    st.title("Bike Price Prediction")

    model = xgb.XGBRegressor()
    model.load_model('xgb_model_bike.json')

    kms_driven = st.number_input('What is the distance completed by the bike in kilometers?', 0, 750000, step=100)
    power = st.number_input('Power of your bike (in bhp)?', 0, 1800, step=20)
    stroke = st.number_input('Stroke of bike?', 0.0, 4.17, step=0.1)
    mileage = st.number_input('Mileage of bike (in kmpl)?', 0.0, 100.0, step=1.0)
    age = st.number_input('Age of bike?', 0, 63, step=1)
    
    # List of brands in the order expected by the model
    brands = [
        'Bajaj', 'Benelli', 'Ducati', 'Harley-Davidson', 'Hero', 'Honda',
        'Hyosung', 'Ideal', 'Indian', 'Jawa', 'KTM', 'Kawasaki', 'LML', 'MV',
        'Mahindra', 'Rajdoot', 'Royal Enfield', 'Suzuki', 'TVS', 'Triumph', 'Yamaha', 'Yezdi'
    ]
    selected_brand = st.selectbox("Select your bike's brand", brands)

    # Create the initial dict in the correct order as expected by the model
    data_dict = {
        'kms_driven': [kms_driven],
        'power': [power],
        'stroke': [stroke],
        'milage': [mileage],
        'age': [age]
    }

    # Update the dict with brand columns, ensuring they follow the order
    brand_dict = {f'brand_{brand}': [0] for brand in brands}
    data_dict.update(brand_dict)

    # Create DataFrame
    data_new = pd.DataFrame(data_dict)

    # Set the selected brand to 1
    data_new[f'brand_{selected_brand}'] = 1

    if st.button('Predict'):
        try:
            pred = model.predict(data_new)
            if pred > 0:
                st.success(f'You can sell the bike for ₹{pred[0]:.2f} ')
            else:
                st.warning("This bike may not be sellable at a meaningful price.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
