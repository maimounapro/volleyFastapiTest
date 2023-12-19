def tournoi_serial(tournoi) -> dict:
    return {
        "id": str(tournoi["_id"]),
        "nom": tournoi["nom"],
        "date": str(tournoi["date"]),
        "lieu": tournoi["lieu"],
        "nombreEquipe": tournoi["nombreEquipe"],
        "departement": tournoi["departement"],
        "nomOrganisateur": tournoi["nomOrganisateur"],
        "emailOrganisateur": tournoi["emailOrganisateur"],
        "telephone": tournoi["telephone"],
        "prixParEquipe": tournoi["prixParEquipe"],
        "heureDebut": tournoi["heureDebut"],
        "heureFin": tournoi["heureFin"],
        "niveau": tournoi["niveau"],
        "typeTournoi": tournoi["typeTournoi"],
        "typeSol": tournoi["typeSol"],
        "compositionEquipe": tournoi["compositionEquipe"],
        "isMixte": tournoi["isMixte"],
        "imageUrl": tournoi["imageUrl"],
        "isFood": tournoi["isFood"],
    }

def list_tournois(tournois) -> dict:
    return {
        "tournois": [tournoi_serial(tournoi) for tournoi in tournois],
        # "len": len(tournoi)
    }