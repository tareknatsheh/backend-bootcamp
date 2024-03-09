import os
from dotenv import load_dotenv
import http_client as h, storage as st, data_analysis as d, plotter as p

load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")

def main():
    # Get asteroid data from Nasa API
    asteroid_data_by_day = h.get_asteroid_data()
    # Save it in a json file
    st.store_data_in_file("data.json", asteroid_data_by_day)

    data_handler = d.DataHandler(asteroid_data_by_day)

    # Create graphs for each asteroid:
    # min diameter vs velocity 
    p.ScatterPlot(data_handler.min_diameter_list, data_handler.relative_velocity_list, "min dia vs vel", "min dia", "vel")
    # miss distance vs max diameter
    p.ScatterPlot(data_handler.miss_distance_list, data_handler.max_diameter_list, "miss dist vs max dia", "miss dist", "max dia")
    p.show_plots()

    # Create the interactive bar plot
    # It gives the user the ability to alter A, B and C coefficients
    p.InteractiveBarsPlot(data_handler.get_danger_indices, data_handler.asteroid_names_list)
    p.show_plots()


if __name__ == "__main__":
    main()