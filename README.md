# Ransomware Simulation

Ce projet illustre un scénario d'utilisation simulée d'un ransomware avec plusieurs étapes et scripts.
ATTENTION: A ne pas reproduire à des fins malveillantes.

---

## **Structure des fichiers**
### 1. `init_mail.py`
- **Objectif** : Ce script est utilisé pour approcher la victime.
- **Fonctionnement** :
  - Envoie un email à la victime (indiquée par `email_cible`) avec le fichier malveillant `malware.py` en pièce jointe.
  - L'email contient un message incitant la victime à exécuter le fichier malveillant pour résoudre un problème supposé.
- **Variable clé** :
  - `email_cible` : Adresse email de la victime.

---

### 2. `malware.py`
- **Objectif** : Chiffre les fichiers de la victime.
- **Fonctionnement** :
  - Génère une clé AES aléatoire pour chiffrer les fichiers d'un dossier ciblé.
  - Les fichiers sont renommés avec l'extension `.enc` après chiffrement.
  - Supprime les fichiers originaux après chiffrement.
  - Envoie la clé AES générée au hacker via email.
- **Variable clé** :
  - `email_cible` : Utilisée pour envoyer les emails de confirmation à la victime. Il faudra donc le remplacer par l'email de la victime avant de faire init_mail.py.

---

### 3. `all_done.py`
- **Objectif** : Envoyer le fichier de décryptage à la victime après réception du paiement.
- **Fonctionnement** :
  - Utilise la clé AES reçue par le hacker pour générer un fichier de décryptage.
  - Envoie un email à la victime avec le script de décryptage et les instructions de restauration.

---

### 4. `mail_sender.py`
- **Objectif** : Fournit une fonction utilitaire pour envoyer des emails.
- **Fonctionnement** :
  - Configure le serveur SMTP avec un `username` (adresse email) et un `password` (mot de passe ou clé d'application).
  - Permet d'envoyer des emails avec des pièces jointes au format HTML ou texte brut.

---

## **Processus global**
1. **Approche initiale (`init_mail.py`)** :
   - Un email est envoyé à la victime contenant le fichier malveillant `malware.py` en pièce jointe.
   - L'email incite la victime à exécuter le fichier pour résoudre un problème supposé.

2. **Chiffrement des fichiers (`malware.py`)** :
   - Lorsque la victime exécute le fichier `malware.py` :
     - Les fichiers ciblés sont chiffrés à l'aide d'une clé AES unique.
     - La clé de décryptage est envoyée au hacker par email.
     - Un message d'instructions est envoyé à la victime pour lui demander un paiement en crypto-monnaie.

3. **Paiement et confirmation (`all_done.py`)** :
   - Après réception du paiement, le hacker exécute `all_done.py`.
   - Le script utilise la clé reçue pour envoyer à la victime un email contenant :
     - Le script de décryptage.
     - Les instructions pour restaurer les fichiers.

---

## **Instructions d'utilisation**
1. **Configuration initiale** :
   - Remplissez les variables suivantes dans les fichiers :
     - `email_cible` : Adresse email de la victime (dans `init_mail.py` et `malware.py`).
     - `username` et `password` : Informations d'authentification SMTP (dans `mail_sender.py`).

2. **Exécution des scripts** :
   - **Étape 1** : Exécutez `init_mail.py` pour envoyer l'email initial à la victime.
   - **Étape 2** : Une fois que la victime exécute `malware.py` :
     - Vérifiez votre boîte de réception pour récupérer la clé de décryptage.
   - **Étape 3** : Après le paiement, exécutez `all_done.py` pour envoyer le fichier de décryptage à la victime.

---

## **Exemple de configuration SMTP**
Dans `mail_sender.py`, configurez les paramètres SMTP comme suit :
```python
smtp_server = "smtp.example.com"
smtp_port = 587
username = "votre_email@example.com"
password = "votre_mot_de_passe"

<img width="775" alt="Capture d’écran 2024-12-19 à 20 18 14" src="https://github.com/user-attachments/assets/d6acd08d-f04e-4e41-96b7-ce2386cb5be4" />

<img width="909" alt="Capture d’écran 2024-12-19 à 20 14 20" src="https://github.com/user-attachments/assets/7236e44c-a788-4029-898a-a3ba111a812b" />
