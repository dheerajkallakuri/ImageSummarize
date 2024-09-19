import requests

from config import Config
config = Config()

def download_random_image():
    # Unsplash API URL for random photo
    url = "https://api.unsplash.com/photos/random"
    
    # Replace with your Unsplash API access key
    access_key = config.access_key
    
    # Set the Authorization headers with your access key
    headers = {
        "Authorization": f"Client-ID {access_key}"
    }

    try:
        # Get a random photo from Unsplash
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for any errors in the request
        
        # Extract the download URL from the JSON response
        image_url = response.json()['urls']['full']

        # Download the image content
        img_response = requests.get(image_url)
        img_response.raise_for_status()  # Check for errors in downloading the image

        # Save the image to a file
        with open("sample.jpg", "wb") as file:
            file.write(img_response.content)

        print("Image downloaded and saved as 'sample.jpg'")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching image: {e}")
