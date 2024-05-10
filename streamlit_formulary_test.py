import streamlit as st
from datetime import datetime, timedelta

def main():
    st.title("Travel Planner")
    st.markdown("---")
    
    st.header("Where are you traveling to?")
    destination = st.text_input("Enter destination", placeholder="e.g., Paris, France")
    
    st.header("Arrival date")
    min_arrival_date = datetime.today()# + timedelta(days=1)
    arrival_date = st.date_input("Select arrival date", min_value=min_arrival_date)
    
    st.header("Departure date")
    min_departure_date = arrival_date + timedelta(days=1) if arrival_date else min_arrival_date + timedelta(days=1)
    departure_date = st.date_input("Select departure date", min_value=None)
    
    st.header("Persons")
    num_persons = st.number_input("Adjust number of people", min_value=1, value=1)
    
    st.markdown("---")
    
    if st.button("FIND!"):
        if destination:
            st.success("Finding options for {} from {} to {} for {} persons.".format(destination, arrival_date.strftime("%Y-%m-%d"), departure_date.strftime("%Y-%m-%d"), num_persons))
        else:
            st.error("Please enter a destination.")
    st.write("")  # You can also use st.empty() or st.markdown("")

if __name__ == "__main__":
    main()
