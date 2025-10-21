# 🏢 InOut 🏢
***Platforme de gestion des visiteurs pour entreprises***

## 📦 Sommaire
- [Présentation du projet](#présentation-du-projet)
- [Architecture type](#architecture-type)
- [Fonctionnalités](#fonctionnalités)
- [Installation (via Docker & Portainer)](#installation-via-docker--portainer)
- [Déploiement du serveur maître](#déploiement-du-serveur-maître)
- [Déploiement d’un serveur enfant](#déploiement-dun-serveur-enfant)
- [Connexion Raspberry Pi (client)](#connexion-raspberry-pi-client)
- [Initialisation & administration](#initialisation--administration)
- [Accès web et API](#accès-web-et-api)
- [Structure du projet](#structure-du-projet)
- [Dépannage](#dépannage)

---

## Présentation du projet
**InOut** permet de : 
- Gérer l'accueil et la sortie des visiteurs sur plusieurs sites d'une entreprise
- Centraliser les données sur un serveur maître
- Offrir des interfaces web de configuration (Formulaires, vidéos d'accueil, règles de sécurité)
- Fournir des DashBoard avec graphique et statistiques

---

## Architecture type 
<img width="878" height="741" alt="image" src="https://github.com/user-attachments/assets/32f81eb8-18e3-404d-8b4a-1ba336578c7f" />
Chaque serveur enfant gère localement les entrées/sorties des visiteurs et synchronise avec le serveur maître lorsqu'il est disponible. 

---

## Fonctionnalités
**🎛 Serveur Maître**
- Tableau de bord global (état des serveurs enfants)
- Gestion centralisée des formulaires
- Rapports multi-sites et graphiques d’activité
- API REST principale

**🖥 Serveur Enfant**
- Gestion locale des visiteurs
- Synchronisation avec le maître
- Interface web locale (personnalisation de formulaires)
- Dashboard local et statistiques

**🧾 Raspberry Pi (Client)**
- Interface tactile pour les visiteurs (entrée/sortie)
- Formulaire configurable depuis le serveur enfant
- Mode hors ligne si le réseau tombe

--- 

## Installation (via Docker & Portainer)
**🧰 Prérequis :**
- Debian / Ubuntu / Raspberry Pi OS
- Docker + Docker Compose
- Portainer (facultatif mais recommandé)
**Installation de docker + Portainer :**
```bash
curl -fsSL https://get.docker.com | sh
docker volume create portainer_data
docker run -d -p 9000:9000 --name=portainer \
  --restart=always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce
```
**Accèder ensuite à portainer sur :**
➡️ http://<IP_SERVEUR>:9000

--- 

## Déploiement du serveur Maître 
- Ouvrir **Portainer → Stacks → Add Stack**
- Nom de la stack : **InOut-master**
- Copier le contenu de **docker-compose.master.yml**
- Cliquer sur **Deploy the stack**
#### Initialisation :
**Dans Portainer :**
- Ouvrir le conteneur **master_server**
- Cliquer sur **Console → /bin/bash**
- Exécuter :
  ```bash
  python manage.py migrate
  python manage.py createsuperuser
  ```
**Accès web :**
🌐 http://<IP_MAITRE>:8000/

--- 

## Déploiement d'un serveur Enfant 
- Ouvrir **Portainer → Stacks → Add Stack**
- Nom de la stack : **InOut-child**
- Copier le contenu de **docker-compose.child.yml**
- Modifier la ligne suivante dans le fichier :
  `MASTER_API_URL=http://<IP_SERVEUR_MAITRE>:8000/api/`
- Cliquer sur **Deploy the stack**
#### Initialisation :
**Dans Portainer :**
- Ouvrir le conteneur **child_server**
- Cliquer sur **Console → /bin/bash**
- Exécuter :
  ```bash
  python manage.py migrate
  python manage.py createsuperuser
  ```
**Accès web :**
🌐 http://<IP_ENFANT>:8001/
