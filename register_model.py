
# ===== 1. Importer les bibliothèques =====

import mlflow
from mlflow import MlflowClient


# ===== 2. Se connecter à la même base que le TP3 =====

# Le fichier mlflow.db contient tous les runs
mlflow.set_tracking_uri("sqlite:///mlflow.db")


# ===== 3. Retrouver le meilleur run =====

runs = mlflow.search_runs(
    experiment_names=["churn-prediction"],
    order_by=["metrics.f1 DESC"]
)

# Sélectionner le meilleur run (F1-score le plus élevé)
best = runs.iloc[0]

# Récupérer son identifiant unique
run_id = best["run_id"]

print(
    "Meilleur run :",
    best["tags.mlflow.runName"],
    "| id :",
    run_id[:8],
    "..."
)


# ===== 4. Enregistrer le modèle dans le Registry =====

# Récupérer le modèle du meilleur run
model_uri = f"runs:/{run_id}/model"

# Enregistrer le modèle sous le nom "churn-model"
result = mlflow.register_model(
    model_uri,
    "churn-model"
)

print(
    "Modèle enregistré : churn-model | version",
    result.version
)


# ===== 5. Définir l'alias « champion » =====

# Créer un client MLflow
client = MlflowClient()

# Associer l'alias champion à la version enregistrée
client.set_registered_model_alias(
    name="churn-model",
    alias="champion",
    version=result.version
)

print(
    "Alias 'champion' -> version",
    result.version
)
