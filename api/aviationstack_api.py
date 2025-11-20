import requests
import os
from dotenv import load_dotenv

class AviationstackAPI:
    """
    API Client for interacting with the aviationstack API.
    """

    def __init__(self, base_url="http://api.aviationstack.com/v1"):
        """
        Initializes the API client with a base URL and API key.
        
        Args:
            base_url (str): The base URL for the API endpoints.
        """
        self.base_url = base_url
        load_dotenv()
        self.params = {'access_key': '4138bd20697197fa64d198e74bc593e1'}

    def get_airports(self):
        """
        Performs a GET request to the /airports endpoint.

        Returns:
            requests.Response: The full response object from the requests library.
        """
        endpoint = "/airports"
        url = f"{self.base_url}{endpoint}"
        
        response = requests.get(url, params=self.params)
        return response

    def get_countries(self):
        """
        Performs a GET request to the /countries endpoint.

        Returns:
            requests.Response: The full response object from the requests library.
        """
        endpoint = "/countries"
        url = f"{self.base_url}{endpoint}"
        
        response = requests.get(url, params=self.params)
        return response