import streamlit as st
import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
# import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development


st.set_page_config(
    page_title="CLEO TECH CARBON OFFSET CALCULATOR",
    page_icon="✅",
    layout="wide",
)
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

st.title("EVENT CARBON CALCULATOR")


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
st.divider()


st.markdown("# REAL TIME TRACKING")


dataset_url = "https://raw.githubusercontent.com/toluwashekoni007/business_carbon_calculator/main/Carbon%20Emission.csv"

@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()

sex_filter = st.selectbox("Select the Gender", pd.unique(df["sex"]))

placeholder = st.empty()

df = df[df["sex"] == sex_filter]

for seconds in range(200):

    df["internetdailyhour_new"] = df["internetdailyhour"] * np.random.choice(range(1, 5))
    df["timespentonpc_new"] = df["timespentonpc"] * np.random.choice(range(1, 5))

    # creating KPIs
    avg_internetdailyhour = np.mean(df["internetdailyhour_new"])

    count_public = int(
        df[(df["transport"] == "public")]["transport"].count()
        + np.random.choice(range(1, 30))
    )



    timespentonpc = np.mean(df["timespentonpc_new"])



    with placeholder.container():

        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        st.divider()
        st.divider()
        st.divider()
        # fill in those three columns with respective metrics or KPIs
        kpi1.metric(
            label="Internet Use Daily",
            value=round(avg_internetdailyhour),
            delta=round(avg_internetdailyhour) - 10,
        )
        
        kpi2.metric(
            label="Transport",
            value=int(count_public),
            delta=-10 + count_public,
        )
        
        kpi3.metric(
            label="Time Spent on PC",
            value=f"£ {round(timespentonpc,2)} ",
            delta=-round(timespentonpc / count_public) * 100,
        )

        # # create two columns for charts
        # fig_col1, fig_col2 = st.columns(2)
        # with fig_col1:
        #     st.markdown("### First Chart")
        #     fig = px.density_heatmap(
        #         data_frame=df, y="internetdailyhour_new", x="transport"
        #     )
        #     st.write(fig)
            
        # with fig_col2:
        #     st.markdown("### Second Chart")
        #     fig2 = px.histogram(data_frame=df, x="internetdailyhour_new")
        #     st.write(fig2)

        #  4: Streamlit App Setup






st.dataframe(df)
time.sleep(1)
st.markdown("This is the data that is used in the real time tracking")

st.divider()
st.divider()

st.markdown ("## CLEO TECH CARBON OFFSET PROGRAM")

st.divider()


st.image("images/king.jpg", caption="Rimba Raya Biodiversity Reserve")
st.divider()
st.divider()

st.image("images/queen.jpg", caption="Eden Reforestation")
st.divider()
st.divider()


st.image("images/pawn.jpg", caption="Second Life Ocean Plastic Recovery and Recycling")

st.divider()


# 8: Educational Resources
st.markdown("## Educational Resources")

intro_text = """
Hey there! Welcome to Cleo Tech's Carbon Offset Program! Below, we've got some handy info to help you wrap your head around carbon offsetting and make some smart choices.
"""

st.write(intro_text)

carbon_offset_text = """
### What's Carbon Offset All About?
Ever heard of carbon offsetting? It's a cool way to balance out the carbon dioxide emissions from activities like travel, energy use, and manufacturing. Here's how it works: you invest in projects that either reduce or remove carbon from the atmosphere. These projects can be anything from planting trees to capturing methane emissions.

Carbon offset projects come in two flavors: there are ones that focus on cutting down emissions (like renewable energy projects), and others that trap carbon dioxide to keep it out of the air (like reforestation).
"""

offset_projects_text = """
### Check Out These Offset Projects
We've got a variety of offset projects aimed at fighting climate change and promoting sustainability:

- **Eden Reforestation**: Think planting trees and restoring forests to soak up CO2 and boost biodiversity.
- **Second Life Ocean Plastic Recovery and Recycling**: Get excited about recycling of plastic that is potentially harmful to sealife.
- **Rimba Raya Biodiversity Reserve**: The Rimba Raya Biodiversity Reserve protects 91,215 hectares of rich, tropical peat swamp forests which are monitored by local rangers.

Each project type has its own set of environmental perks and helps tackle different aspects of climate change and ecosystem health.
"""

maximize_contribution_text = """
### Making Your Impact Count
Want to make the most out of your sustainability efforts with carbon offsetting? Check out these tips:

- **Choose Wisely**: Pick projects with solid environmental credentials and transparent reporting. Look for certifications like the Verified Carbon Standard (VCS) to ensure your investment has a real impact.
- **Go Local**: Consider supporting offset projects in your community to address local environmental issues and boost sustainable development.
- **Know Your Carbon Footprint**: Figure out your carbon footprint to see where you can cut back on emissions through lifestyle changes and energy efficiency.
- **Offset as a Last Resort**: While carbon offsetting is awesome, it's even better to focus on reducing emissions first. So, try to cut back on energy use, choose eco-friendly transportation, and reduce waste before turning to offsetting.

Remember, every little bit helps in building a greener future! By offsetting your carbon footprint and backing carbon offset projects, you're playing a crucial role in fighting climate change and safeguarding our planet for generations to come.
"""

st.write(carbon_offset_text)
st.write(offset_projects_text)
st.write(maximize_contribution_text)
