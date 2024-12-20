# Ransomware Simulation

Ce projet illustre un scénario simplifié de simulation de ransomware, où un fichier exécutable unique effectue toutes les actions : chiffrement, demande de rançon et décryptage après paiement.  
**ATTENTION** : Ce projet est exclusivement destiné à des fins éducatives et de sensibilisation à la cybersécurité.

---

## **Structure des fichiers**
### 1. `init_mail.py`
- **Objectif** : Approcher la victime en lui envoyant un email contenant un lien de téléchargement vers un fichier exécutable malveillant.
- **Fonctionnement** :
  - Envoie un email HTML à la victime (indiquée par `email_cible`) avec un lien de téléchargement pour récupérer un fichier exécutable (`bienvenue.exe`).
  - Le lien incite la victime à télécharger et exécuter le fichier pour résoudre un problème supposé.
- **Variable clé** :
  - `email_cible` : Adresse email de la victime.

---

### 2. `bienvenue.exe`
- **Objectif** : Réaliser toutes les étapes du ransomware dans un seul fichier exécutable.
- **Fonctionnement** :
  - **Chiffrement** : Chiffre les fichiers du dossier cible à l'aide d'une clé AES générée localement.
  - **Demande de rançon** : Affiche une interface utilisateur demandant un paiement en crypto-monnaie pour restaurer les fichiers.
  - **Décryptage** : Une fois le paiement validé, permet à la victime de restaurer ses fichiers.

---

## **Processus global**
1. **Approche initiale (`init_mail.py`)** :
   - Un email HTML est envoyé à la victime avec un lien de téléchargement vers le fichier exécutable malveillant.
   - L'email contient un message incitant la victime à télécharger et exécuter le fichier.

2. **Exécution de `bienvenue.exe`** :
   - Une fois téléchargé et exécuté par la victime :
     - Les fichiers du dossier cible sont chiffrés avec une clé AES locale.
     - Une interface utilisateur s'affiche demandant un paiement en crypto-monnaie pour restaurer les fichiers.
     - Après validation du paiement, les fichiers sont déchiffrés automatiquement.

---

## **Instructions d'utilisation**
1. **Configuration initiale** :
   - Remplissez les variables dans `init_mail.py` :
     - `email_cible` : Adresse email de la victime.
     - `username` et `password` : Informations d'authentification SMTP pour envoyer l'email.

2. **Exécution des scripts** :
   - **Étape 1** : Exécutez `init_mail.py` pour envoyer l'email initial contenant le lien vers `bienvenue.exe`.
   - **Étape 2** : Une fois que la victime télécharge et exécute `bienvenue.exe` :
     - Les fichiers ciblés sont chiffrés.
     - Une interface utilisateur demande un paiement en crypto-monnaie.
     - Après le paiement, les fichiers sont déchiffrés automatiquement.

---

## **Exemple de configuration SMTP**
Dans `init_mail.py`, configurez les paramètres SMTP comme suit :
```python
smtp_server = "smtp.example.com"
smtp_port = 587
username = "votre_email@example.com"
password = "votre_mot_de_passe"
