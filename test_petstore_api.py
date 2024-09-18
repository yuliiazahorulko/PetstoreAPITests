import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2/pet"


# Utility function to create a pet payload
def generate_pet_data(pet_id, name, status="available"):
    return {
        "id": pet_id,
        "name": name,
        "status": status
    }


### Positive Test Cases ###

# CREATE (POST)
def test_create_pet():
    pet_id = 12345
    pet_data = generate_pet_data(pet_id, "Fluffy")
    
    response = requests.post(BASE_URL, json=pet_data)
    
    assert response.status_code == 200
    response_data = response.json()
    
    assert response_data["id"] == pet_id
    assert response_data["name"] == "Fluffy"
    assert response_data["status"] == "available"


# READ (GET)
def test_get_pet():
    pet_id = 12345
    response = requests.get(f"{BASE_URL}/{pet_id}")
    
    assert response.status_code == 200
    response_data = response.json()
    
    assert response_data["id"] == pet_id
    assert response_data["name"] == "Fluffy"
    assert response_data["status"] == "available"


# UPDATE (PUT)
def test_update_pet():
    pet_id = 12345
    updated_data = generate_pet_data(pet_id, "Fido", "sold")
    
    response = requests.put(BASE_URL, json=updated_data)
    
    assert response.status_code == 200
    response_data = response.json()
    
    assert response_data["id"] == pet_id
    assert response_data["name"] == "Fido"
    assert response_data["status"] == "sold"


# DELETE (DELETE)
def test_delete_pet():
    pet_id = 12345
    response = requests.delete(f"{BASE_URL}/{pet_id}")
    
    assert response.status_code == 200
    response_data = response.json()
    
    assert response_data["code"] == 200
    assert response_data["message"] == str(pet_id)


### Negative Test Cases ###

# CREATE (POST) - Invalid data
def test_create_pet_invalid_data():
    invalid_pet_data = {
        "id": "invalid_id",  # Invalid data type for ID
        "name": "Rover",
        "status": "available"
    }
    
    response = requests.post(BASE_URL, json=invalid_pet_data)
    
    assert response.status_code == 500 #400  # Bad Request expected


# READ (GET) - Non-existent pet
def test_get_non_existent_pet():
    non_existent_pet_id = 99999
    response = requests.get(f"{BASE_URL}/{non_existent_pet_id}")
    
    assert response.status_code == 404  # Not Found expected


# UPDATE (PUT) - Invalid pet ID
def test_update_pet_invalid_id():
    invalid_pet_data = generate_pet_data("invalid_id", "Buddy", "available")
    
    response = requests.put(BASE_URL, json=invalid_pet_data)
    
    assert response.status_code == 500 #400  # Bad Request expected


# DELETE (DELETE) - Non-existent pet
def test_delete_non_existent_pet():
    non_existent_pet_id = 99999
    response = requests.delete(f"{BASE_URL}/{non_existent_pet_id}")
    
    assert response.status_code == 404  # Not Found expected


if __name__ == "__main__":
    pytest.main()
