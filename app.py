import streamlit as st
from streamlit_gps_location import gps_location_button
from datetime import datetime


st.set_page_config(
    page_title="Field Discovery Report",
    layout="centered"
)

st.title("Field Report")
st.write("Document and report a real-world scientific observation.")

st.divider()



researcher_name = st.text_input("Researcher name")

field = st.selectbox(
    "Scientific field",
    [
        "Biology",
        "Geology",
        "Environmental Science",
        "Ecology",
        "Other"
    ]
)

# Observation details
st.subheader("Observation Details")

observation_title = st.text_input("Discovery / Observation title")

observation_type = st.selectbox(
    "Type of observation",
    [
        "Plant",
        "Animal",
        "Rock / Mineral",
        "Water / Soil",
        "Pollution",
        "Weather / Climate",
        "Other"
    ]
)

description = st.text_area(
    "Describe what you observed",
    placeholder="Example: I observed unusual algae growth near a slow-moving stream..."
)

conditions = st.text_area(
    "Environmental conditions",
    placeholder="Example: Sunny, humid, near freshwater, muddy soil..."
)

# Optional photo
photo = st.camera_input("Take a photo of the observation")

st.divider()

# GPS location
st.subheader("GPS Location")

location_data = gps_location_button(buttonText="📍 Get my location")

latitude = None
longitude = None

if location_data is not None:
    latitude = location_data.get("latitude")
    longitude = location_data.get("longitude")

    st.success("Location captured successfully!")

    st.write("Latitude:", latitude)
    st.write("Longitude:", longitude)

    if latitude is not None and longitude is not None:
        map_data = {
            "lat": [latitude],
            "lon": [longitude]
        }
        st.map(map_data)
else:
    st.info("Press the button above to capture your GPS location.")

st.divider()




st.subheader("Generate Report")

if st.button("Submit Report", use_container_width=True):
    if not researcher_name or not observation_title or not description:
        st.warning("Please complete the researcher name, title, and description.")
    else:
        report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        report = f"""
FIELD DISCOVERY REPORT

Date and Time:
{report_time}

Researcher:
{researcher_name}

Scientific Field:
{field}

Observation Title:
{observation_title}

Observation Type:
{observation_type}

Description:
{description}

Environmental Conditions:
{conditions}

GPS Coordinates:
Latitude: {latitude}
Longitude: {longitude}

Report Status:
Submitted
"""

        st.success("Report created successfully!")

        st.text_area("Report Preview", report, height=350)

        st.download_button(
            label="Download Report",
            data=report,
            file_name="field_discovery_report.txt",
            mime="text/plain",
            use_container_width=True
        )