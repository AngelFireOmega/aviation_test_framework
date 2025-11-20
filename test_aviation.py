import pytest
from api.aviationstack_api import AviationstackAPI

@pytest.fixture
def aviation_api_client():
    """Provides an AviationstackAPI client instance for tests."""
    return AviationstackAPI()

def test_get_airports_returns_200(aviation_api_client):
    """
    Tests that a GET request to the /airports endpoint returns a 200 OK status code.
    
    Args:
        aviation_api_client (AviationstackAPI): The API client fixture.
    """
    # 1. Act: Make the API call using the client
    response = aviation_api_client.get_airports()
    
    # Print response details to the command line
    print(f"\nAPI Request URL: {response.request.url}")
    print(f"\nStatus Code: {response.status_code}")
    response_json = response.json()
    
    # Extract the first airport's data
    airports = response_json.get('data', [])
    if airports:
        first_airport = airports[0]
        print("\n--- First Airport Data ---")
        for key, value in first_airport.items():
            print(f"{key}: {value}")
        print("--------------------------")
    else:
        print("\nNo airports found in the response.")

    # Assert that 100 airports are returned
    assert len(airports) == 100, f"Expected 100 airports, but got {len(airports)}"

    # Assert that the first airport is Anaa
    assert airports[0].get('airport_name') == "Anaa", f"Expected first airport to be Anaa, but got {airports[0].get('airport_name')}"

    # Iterate through the list of airports and print their names
    print(f"\n--- Found {len(airports)} Airports ---")
    for airport in airports:
        print(f"- {airport.get('airport_name', 'N/A')} ({airport.get('iata_code', 'N/A')})")
    print("--------------------------")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert "data" in response_json, "Response JSON should contain a 'data' key"

def test_get_countries_returns_100_with_200_ok(aviation_api_client):
    """
    Tests that a GET request to the /countries endpoint returns a 200 OK status code
    and a list of 100 countries.
    
    Args:
        aviation_api_client (AviationstackAPI): The API client fixture.
    """
    # 1. Act: Send API request
    response = aviation_api_client.get_countries()
    
    # 2. Assert: Assert the status code and the amount of countries returned
    assert response.status_code == 200, f"Expected status code 200, but received {response.status_code}"
    
    response_json = response.json()
    countries = response_json.get('data', [])
    
    print("\n--- /countries Full API Response (JSON) ---")
    print(response_json)
    print("------------------------------------")
    
    assert len(countries) == 100, f"Expected 100 countries, but got {len(countries)}"

    if countries:
        first_country = countries[0]
        # Verify the first country
        assert first_country.get('country_name') == 'Andorra', f"Expected the first country to be Andorra, but it was {first_country.get('country_name')}"

        print("\n--- First Country Data ---")
        for key, value in first_country.items():
            print(f"{key}: {value}")
        print("--------------------------")
    else:
        print("\nNo countries were found in the response.")

    print(f"\nSuccessfully retrieved {len(countries)} countries from /countries endpoint with status code {response.status_code}.")