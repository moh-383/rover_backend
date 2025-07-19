# 🛰️ Backend API - Rover Detector

Ce backend est développé avec [FastAPI](https://fastapi.tiangolo.com/) pour gérer les capteurs et le pilotage du rover. Il communique avec un ESP32-CAM via WiFi et pourra également gérer d'autres composants via une connexion série ou WiFi.

---

## ⚙️ Installation

### 1. Cloner le dépôt (si ce n’est pas encore fait)

git clone https://github.com/moh-383/rover_backend

### 2. Créer un environnement virtuel Python

python -m venv venv
venv\Scripts\activate  # Sous Windows
# ou
source venv/bin/activate  # Sous Linux/macOS


### 3. Activer l'environnement virtuel 

 .\venv\Scripts\activate
Vous devrez voir quelque chose comme: (venv) PS C:\Users\ton-nom\backend_rover>

### 4. Installer les dépendances

pip install -r requirements.txt

### 🚀 Lancer le serveur

uvicorn app.main:app --reload
Vous verrez: Uvicorn running on http://127.0.0.1:8000
vous le laissé ouvert en cours d'exécution et
Ensuite, vous ouvrez votre navigateur sur :
👉 http://127.0.0.1:8000/docs pour accéder à la documentation interactive Swagger.

## 📡 Connexion avec l’ESP32-CAM
## L’ESP32-CAM peut communiquer via WiFi en envoyant des requêtes HTTP à cette API.
## Exemple de requête HTTP envoyée depuis l’ESP32 :

HTTPClient http;
http.begin("http://<IP_PC>:8000/GEG/sensors"); // Remplace <IP_PC> par l’IP locale de ton PC
http.addHeader("Content-Type", "application/json");

String payload = "{\"temperature\": 27.3, \"magnetic\": 1}";
int httpResponseCode = http.POST(payload);

## 💡 Le PC et l’ESP32 doivent être sur le même réseau WiFi.

### 📌 Routes actuelles disponibles

| Méthode | URL            | Description                      |
| ------- | -------------- | -------------------------------- |
| POST    | `/GEG/sensors` | Envoie les données des capteurs  |
| GET     | `/GEG/status`  | (à venir) Récupère l’état actuel |
| POST    | `/GEG/control` | (à venir) Contrôle du rover      |

### 📂 Structure du backend
backend/
├── app/
│   ├── main.py          # Point d'entrée de l'API
│   ├── routers/
│   │   └── control.py   # Définition des routes
│   ├── models/
│   │   └── control.py   # Schémas Pydantic
│   └── utils/
│       └── serial_comm.py (à venir pour liaison série)
├── requirements.txt
└── README.md


🧠 À venir
Ajout des routes pour le contrôle en temps réel (mouvement du rover)

Intégration de la détection de mines

Liaison série (via USB) si nécessaire

Authentification pour sécuriser les requêtes

# 👨‍💻 Auteur
Développé dans le cadre du projet de rover détecteur de mines 🧨 – INGENOVA 2025
par l'équipe RoboDefenders



