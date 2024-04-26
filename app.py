


import streamlit as st

EMISSION_FACTORS = {
    "Air Travel": 0.254,  # kg CO2 per passenger-km
    "Car Travel": 0.164,  # kg CO2 per km
    "Electricity": 0.20707,  # kg CO2 per kWh
    "Internet": 0.00268,  # kg CO2 per MB
    "Server": 0.00031,  # kg CO2 per MB
    "Personal Computer": 0.233,  # kg CO2 per hour
    "Mobile Device": 0.00005,  # kg CO2 per hour
    "Accommodation": 5,  # kg CO2 per night
    "Commute": {"Public Transport": 2.8, "Private Vehicle": 2.4},  # kg CO2 per km
}

def calculate_emissions(event_type, event_data):
    total_emissions = 0
    
    if event_type == "Physical":
        total_emissions += event_data["participants"] * event_data["distance_air"] * EMISSION_FACTORS["Air Travel"]
        total_emissions += event_data["distance_car"] * EMISSION_FACTORS["Car Travel"]
        total_emissions += event_data["accommodation"] * EMISSION_FACTORS["Accommodation"]
        total_emissions += event_data["participants"] * event_data["distance_commute"] * EMISSION_FACTORS["Commute"][event_data["commute_method"]]
    else:
        total_emissions += event_data["electricity"] * EMISSION_FACTORS["Electricity"]
        total_emissions += event_data["internet"] * EMISSION_FACTORS["Internet"]
        total_emissions += event_data["server"] * EMISSION_FACTORS["Server"]
        total_emissions += event_data["pc"] * EMISSION_FACTORS["Personal Computer"]
        total_emissions += event_data["mobile"] * EMISSION_FACTORS["Mobile Device"]
    
    return total_emissions

#  4: Streamlit App Setup
st.title("Event Carbon Emissions Calculator")

event_type = st.radio("Select Event Type", ("Physical", "Virtual"))

#  5: User Input Handling
if event_type == "Physical":
    st.subheader("Physical Event Details")
    participants = st.number_input("Number of Participants", min_value=1, value=1)
    distance_air = st.number_input("Air Travel Distance (km)", min_value=0.0, value=0.0)
    distance_car = st.number_input("Car Travel Distance (km)", min_value=0.0, value=0.0)
    accommodation = st.number_input("Number of Nights Accommodation", min_value=0, value=0)
    commute_method = st.selectbox("Commute Method", ("Public Transport", "Private Vehicle"))
    distance_commute = st.number_input("Commute Distance (km)", min_value=0.0, value=0.0)
    event_data = {
        "participants": participants,
        "distance_air": distance_air,
        "distance_car": distance_car,
        "accommodation": accommodation,
        "commute_method": commute_method,
        "distance_commute": distance_commute,
    }
else:
    st.subheader("Virtual Event Details")
    electricity = st.number_input("Electricity Consumption (kWh)", min_value=0.0, value=0.0)
    internet = st.number_input("Internet Usage (MB)", min_value=0.0, value=0.0)
    server = st.number_input("Server Emissions (MB)", min_value=0.0, value=0.0)
    pc = st.number_input("Personal Computer Usage (hours)", min_value=0.0, value=0.0)
    mobile = st.number_input("Mobile Device Usage (hours)", min_value=0.0, value=0.0)
    event_data = {
        "electricity": electricity,
        "internet": internet,
        "server": server,
        "pc": pc,
        "mobile": mobile,
    }

#  6: Emissions Calculation
total_emissions = calculate_emissions(event_type, event_data)
st.divider()
st.divider()

#  7: Display Results
st.subheader("Total Carbon Emissions")
st.write(f"Total emissions: {total_emissions:.2f} kg CO2e")

st.divider()
st.divider()


st.image("images/king.jpg", caption="Rimba Raya Biodiversity Reserve")
st.divider()
st.divider()

st.image("images/queen.jpg", caption="Eden Reforestation")
st.divider()
st.divider()


st.image("images/pawn.jpg", caption="Second Life Ocean Plastic Recovery and Recycling")


