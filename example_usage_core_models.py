from core_models import PowerSource, PowerConsumer, NetworkElement

def main():
    solar_plant = PowerSource("Solar Plant 1", "solar", 100.0)
    wind_farm = PowerSource("Wind Farm 1", "wind", 150.0)
    city_grid = PowerConsumer("City Grid", 200.0)
    transmission_line = NetworkElement("Main Transmission Line", 300.0)

    transmission_line.connect_element(solar_plant)
    transmission_line.connect_element(wind_farm)
    transmission_line.connect_element(city_grid)

    # Simulate one time step
    for element in [solar_plant, wind_farm, city_grid, transmission_line]:
        element.update_state()

    print(f"Solar Plant output: {solar_plant.current_output}")
    print(f"Wind Farm output: {wind_farm.current_output}")
    print(f"City Grid demand: {city_grid.current_demand}")
    print(f"Transmission Line load: {transmission_line.current_load}")

if __name__ == "__main__":
    main()