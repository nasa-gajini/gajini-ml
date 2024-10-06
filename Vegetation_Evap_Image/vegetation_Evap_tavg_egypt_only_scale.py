import os
import matplotlib.pyplot as plt

def load_evap_data(file_path_2024, file_path_2023):
    import xarray as xr
    # Load the NetCDF files
    ds_2024 = xr.open_dataset(file_path_2024)
    ds_2023 = xr.open_dataset(file_path_2023)

    # Extract Evap_tavg variables
    evap_2024 = ds_2024['Evap_tavg']
    evap_2023 = ds_2023['Evap_tavg']

    return evap_2024, evap_2023


def visualize_egypt(evap_2024_clipped, evap_2023_clipped, save_path):
    """
    Visualize only the Egypt Evapotranspiration for 2023, 2024, and the difference
    in a single image (1x3 layout) and save it.
    """
    # Calculate the differences for Egypt
    egypt_diff = evap_2024_clipped - evap_2023_clipped

    # Create subplots for Egypt (1 row, 3 columns)
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))

    # Plot 2023 Egypt data
    evap_2023_clipped.plot(ax=axes[0], cmap='viridis')
    axes[0].set_title('Evapotranspiration - 2023 (Egypt)')
    axes[0].set_xlabel('Longitude')
    axes[0].set_ylabel('Latitude')

    # Plot 2024 Egypt data
    evap_2024_clipped.plot(ax=axes[1], cmap='viridis')
    axes[1].set_title('Evapotranspiration - 2024 (Egypt)')
    axes[1].set_xlabel('Longitude')
    axes[1].set_ylabel('Latitude')

    # Plot difference in Egypt data (2024 - 2023) with limited range to enhance visibility of small differences
    egypt_diff.plot(ax=axes[2], cmap='RdBu_r', vmin=-1e-6, vmax=1e-6)  # 범위를 설정하여 차이를 강조
    axes[2].set_title('Difference in Evapotranspiration (2024 - 2023) (Egypt)')
    axes[2].set_xlabel('Longitude')
    axes[2].set_ylabel('Latitude')

    # Adjust layout
    plt.tight_layout()

    # Save the figure
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

    # Clip the data to Egypt
    evap_2024_clipped, evap_2023_clipped = clip_evap_data_to_egypt(evap_2024, evap_2023, geojson_path)

    # Visualize and save the Egypt-only plot (1x3 layout)
    visualize_egypt(evap_2024_clipped, evap_2023_clipped,
                    save_path=os.path.join(img_dir, 'egypt_evap_combined_emphasized.png'))


if __name__ == "__main__":
    main()
