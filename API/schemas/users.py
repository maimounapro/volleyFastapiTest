def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "nom": str(item["name"]),
        "age": str(item["description"]),
        "pseudo" : int(item["phone"]),
        "mdp": str(item["imageUrl"]),
        "taille": str(item["imageUrl"]),
        "email": str(item["imageUrl"]),
        "created_at": item["created_at"],
        "isActive": bool(item["imageUrl"]),
        "poste": item["poste"]
    }

def usersEntities(entities) -> list:
    return [userEntity(item) for item in entities]