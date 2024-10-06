import os

def load_evap_data(file_path_2024, file_path_2023):
    import xarray as xr
    # Load the NetCDF files
    ds_2024 = xr.open_dataset(file_path_2024)
    ds_2023 = xr.open_dataset(file_path_2023)

    # Extract Evap_tavg variables
    evap_2024 = ds_2024['Evap_tavg']
    evap_2023 = ds_2023['Evap_tavg']

    return evap_2024, evap_2023


def visualize_evap(evap, year, region, save_path):
    """
    Visualize Evapotranspiration for a given year and region (global or Egypt) and save the figure.
    """
    import matplotlib.pyplot as plt

    # Create the plot
    plt.figure(figsize=(10, 6))
    evap.plot(cmap='viridis')
    plt.title(f'Evapotranspiration - {year} ({region})')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    # Save the plot
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def visualize_evap_difference(evap_2024, evap_2023, title, save_path):
    """
    Visualize the difference in Evapotranspiration between 2024 and 2023 and save the figure.
    """
    import matplotlib.pyplot as plt

    # Calculate the difference between 2024 and 2023
    evap_diff = evap_2024 - evap_2023

    # Plot the difference
    plt.figure(figsize=(10, 6))
    evap_diff.plot(cmap='RdBu_r')  # Use a diverging colormap to visualize differences
    plt.title(title)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    # Save the plot
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def clip_evap_data_to_egypt(evap_2024, evap_2023, geojson_path):
    import rioxarray
    import geopandas as gpd
    from shapely.geometry import mapping

    # Load Egypt boundary from GeoJSON
    egypt_boundary = gpd.read_file(geojson_path)

    # Set coordinate reference system (CRS) to WGS84 (EPSG:4326)
    evap_2024 = evap_2024.rio.write_crs("EPSG:4326")
    evap_2023 = evap_2023.rio.write_crs("EPSG:4326")

    # Extract Egypt polygon for clipping
    egypt_polygon = egypt_boundary.geometry.unary_union

    # Clip Evapotranspiration data to Egypt boundary
    evap_2024_clipped = evap_2024.isel(time=0).rio.clip([mapping(egypt_polygon)], evap_2024.rio.crs, drop=True)
    evap_2023_clipped = evap_2023.isel(time=0).rio.clip([mapping(egypt_polygon)], evap_2023.rio.crs, drop=True)

    return evap_2024_clipped, evap_2023_clipped


def main():
    file_path_2024 = '../data/Vegetation_ET/FLDAS_NOAH01_C_GL_M.A202408.001.nc'
    file_path_2023 = '../data/Vegetation_ET/FLDAS_NOAH01_C_GL_M.A202308.001.nc'
    geojson_path = '../data/egypt.geojson'
    img_dir = '../data/img/'

    # Ensure the output directory exists
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    # Load evapotranspiration data
    evap_2024, evap_2023 = load_evap_data(file_path_2024, file_path_2023)

    # Visualize and save global evapotranspiration for 2023 and 2024
    visualize_evap(evap_2023.isel(time=0), 2023, 'Global', os.path.join(img_dir, 'global_evap_2023.png'))
    visualize_evap(evap_2024.isel(time=0), 2024, 'Global', os.path.join(img_dir, 'global_evap_2024.png'))

    # Clip the data to Egypt and visualize for 2023 and 2024
    evap_2024_clipped, evap_2023_clipped = clip_evap_data_to_egypt(evap_2024, evap_2023, geojson_path)
    visualize_evap(evap_2023_clipped, 2023, 'Egypt', os.path.join(img_dir, 'egypt_evap_2023.png'))
    visualize_evap(evap_2024_clipped, 2024, 'Egypt', os.path.join(img_dir, 'egypt_evap_2024.png'))

    # Visualize and save the global difference between 2024 and 2023
    visualize_evap_difference(evap_2024.isel(time=0), evap_2023.isel(time=0),
                              'Difference in Evapotranspiration (2024 - 2023) - Global',
                              os.path.join(img_dir, 'global_evap_difference.png'))

    # Visualize and save the Egypt difference between 2024 and 2023
    visualize_evap_difference(evap_2024_clipped, evap_2023_clipped,
                              'Difference in Evapotranspiration (2024 - 2023) - Egypt',
                              os.path.join(img_dir, 'egypt_evap_difference.png'))


if __name__ == "__main__":
    main()
