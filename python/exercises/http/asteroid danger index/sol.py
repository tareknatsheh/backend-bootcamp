import os
from dotenv import load_dotenv
import http_client as h, storage as st, data_analysis as d, plotter as p

# TODO: finish plotter.py

load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")


def main():
    # Get asteroid data from Nasa API
    asteroid_data_by_day = h.get_asteroid_data()
    # Save it in a json file
    st.store_data_in_file("data.json", asteroid_data_by_day)
    # Process the data (keep only: id, name, est diameter (min and max), miss distance (km), relative velocity (KM/H))
    clean_asteroid_list = d.clean_asteroid_data(asteroid_data_by_day)
    # Save it in a json file
    st.store_data_in_file("clean_data.json", clean_asteroid_list)
    # Create graphs for each asteroid (min diameter vs velocity AND miss distance vs max diameter)
    p.plot(clean_asteroid_list)


if __name__ == "__main__":
    main()


# Calculate the danger index of each asteroid
# Plot DYNAMICALLY asteroid name vs danger index
