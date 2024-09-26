def generate_pet_data(pet_id, name, status="available"):
    return {
        "id": pet_id,
        "name": name,
        "status": status
    }
