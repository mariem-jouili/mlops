import requests  # Envoyer des requêtes HTTP depuis Python

URL = "http://localhost:8000"  # Adresse de notre API


# ===== 1. Vérifier si l'API est en vie =====
print("GET /health ->", requests.get(URL + "/health").json())


# ===== 2. Tester un client à faible consommation et faible ancienneté =====
client = {
    "age": 35,
    "salaire": 2500,
    "abonnement": "Standard",
    "anciennete": 1,
    "consommation": 10
}

# json= : envoie le dictionnaire au format JSON
r = requests.post(URL + "/predict", json=client)

print("POST /predict (client 1) ->", r.status_code, r.json())


# ===== 3. Tester un client fidèle =====
# Forte consommation et forte ancienneté
client2 = {
    "age": 50,
    "salaire": 4000,
    "abonnement": "Premium",
    "anciennete": 10,
    "consommation": 80
}

r = requests.post(URL + "/predict", json=client2)

print("POST /predict (client 2) ->", r.status_code, r.json())


# ===== 4. Provoquer volontairement une erreur =====
# L'âge est du texte au lieu d'un nombre entier
mauvais = dict(client, age="abc")  # Copie de client avec age modifié

r = requests.post(URL + "/predict", json=mauvais)

print("POST /predict (age='abc') ->", r.status_code)
print("Message :", r.json()["detail"][0]["msg"])