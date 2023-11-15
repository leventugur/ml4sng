import requests
import zipfile
import io


# Set destination
destination_folder = "./ml4sng/tests/test_data/"

# Set target
download_url = "https://drive.google.com/uc?id=1rV4FhJ2lOJ5zv7qd5GeunSEbN9pJtpbS&confirm=t&uuid=cbc35fa9-3515-41f8-a45c-53b8c4a94cc0&at=AB6BwCA9AWClRSWXTxm8gHAKdMYW:1693255266420"

# Send a request to get the file
response = requests.get(download_url)
response.raise_for_status()

# Create a ZipFile object from the response content
with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_ref:
    # Extract the contents to the specified destination folder
    zip_ref.extractall(destination_folder)
