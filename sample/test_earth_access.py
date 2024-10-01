import earthaccess

# 1. Login
earthaccess.login()

# 2. Search
results = earthaccess.search_data(
    short_name='SPL3SMP_E',  # ATLAS/ICESat-2 L3A Land Ice Height
    bounding_box=(-10, 20, 10, 50),  # Only include files in area of interest...
    temporal=("2024-08", "2024-09"),  # ...and time period of interest.
    count=10
)

# 3. Access
files = earthaccess.download(results, "./tmp")

