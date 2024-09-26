import pytest
from api_tests.api_client import PetstoreAPIClient
from api_tests.data import generate_pet_data


@pytest.mark.parametrize("pet_id, pet_name", [(12345, "Fluffy")])
def test_create_pet(api_client, pet_id, pet_name):
    pet_data = generate_pet_data(pet_id, pet_name)
    response = api_client.create_pet(pet_data)
    
    assert response.status_code == 200
    response_data = response.json()
    
    assert response_data["id"] == pet_id
    assert response_data["name"] == pet_name
    assert response_data["status"] == "available"


def test_get_pet(api_client):
    pet_id = 12345
    response = api_client.get_pet(pet_id)
    
    assert response.status_code == 200
    response_data = response.json()
    
    assert response_data["id"] == pet_id
    assert response_data["name"] == "Fluffy"
    assert response_data["status"] == "available"


def test_update_pet(api_client):
    pet_id = 12345
    updated_data = generate_pet_data(pet_id, "Fido", "sold")
    response = api_client.update_pet(updated_data)
    
    assert response.status_code == 200
    response_data = response.json()
    
    assert response_data["id"] == pet_id
    assert response_data["name"] == "Fido"
    assert response_data["status"] == "sold"


def test_delete_pet(api_client):
    pet_id = 12345
    response = api_client.delete_pet(pet_id)
    
    assert response.status_code == 200
    response_data = response.json()
    
    assert response_data["code"] == 200
    assert response_data["message"] == str(pet_id)


def test_create_pet_invalid_data(api_client):
    invalid_pet_data = {
        "id": "invalid_id",  # Invalid data type for ID
        "name": "Rover",
        "status": "available"
    }
    
    response = api_client.create_pet(invalid_pet_data)
    
    assert response.status_code == 500  # Bad Request expected


def test_get_non_existent_pet(api_client):
    non_existent_pet_id = 99999
    response = api_client.get_pet(non_existent_pet_id)
    
    assert response.status_code == 404  # Not Found expected


def test_update_pet_invalid_id(api_client):
    invalid_pet_data = generate_pet_data("invalid_id", "Buddy", "available")
    response = api_client.update_pet(invalid_pet_data)
    
    assert response.status_code == 500  # Bad Request expected


def test_delete_non_existent_pet(api_client):
    non_existent_pet_id = 99999
    response = api_client.delete_pet(non_existent_pet_id)
    
    assert response.status_code == 404  # Not Found expected


if __name__ == "__main__":
    pytest.main()
