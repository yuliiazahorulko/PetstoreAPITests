import requests

class PetstoreAPIClient:
    BASE_URL = "https://petstore.swagger.io/v2/pet"

    @staticmethod
    def create_pet(pet_data):
        return requests.post(PetstoreAPIClient.BASE_URL, json=pet_data)

    @staticmethod
    def get_pet(pet_id):
        return requests.get(f"{PetstoreAPIClient.BASE_URL}/{pet_id}")

    @staticmethod
    def update_pet(pet_data):
        return requests.put(PetstoreAPIClient.BASE_URL, json=pet_data)

    @staticmethod
    def delete_pet(pet_id):
        return requests.delete(f"{PetstoreAPIClient.BASE_URL}/{pet_id}")
