import sys
import pandas as pd

def analyze_city_rooms(city_name, data_file="cleaned_data.xlsx"):
  
    try:
        df = pd.read_excel(data_file)  # Read Excel file
    except FileNotFoundError:
        print(f"Error: Data file '{data_file}' not found.")
        return

    # Filter data for the specified city (case-insensitive)
    city_data = df[df["City"].str.lower() == city_name.lower()]

    if city_data.empty:
        print(f"No data found for city: {city_name}")
        return

    # Best Room (based on Reviews - assuming higher is better)
    best_room = city_data.loc[city_data["Reviews"].idxmax()]
    print(f"The best type of Room based on its Reviews: {best_room['PType']} (Reviews: {best_room['Reviews']})")

    # Cheapest Room
    cheapest_room = city_data.loc[city_data["PPN"].idxmin()]
    print(f"The cheapest Room in the city: {cheapest_room['PType']} at {cheapest_room['Location ']} (PPN: {cheapest_room['PPN']})")

    # Costliest Room
    costliest_room = city_data.loc[city_data["PPN"].idxmax()]
    print(f"The costliest Room in the city: {costliest_room['PType']} at {costliest_room['Location ']} (PPN: {costliest_room['PPN']})")

    # Average PPN (Price Per Night)
    average_ppn = city_data["PPN"].mean()
    print(f"The average PPN for {city_name}: {average_ppn:.2f}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <city_name>")
        sys.exit(1)

    city_name = sys.argv[1]  # Get the city name (second element)
    analyze_city_rooms(city_name)