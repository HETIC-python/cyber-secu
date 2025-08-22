# Ransomware Simulation

Ce projet illustre un scénario simplifié de simulation de ransomware, où un fichier exécutable unique effectue toutes les actions : chiffrement, demande de rançon et décryptage après paiement.  
**⚠️ ATTENTION** : Ce projet est exclusivement destiné à des fins éducatives et de sensibilisation à la cybersécurité.

**🔒 SÉCURITÉ** : Toutes les informations sensibles ont été remplacées par des exemples. Vous devez configurer vos propres paramètres avant utilisation.

---

## **Configuration requise**

### 1. **Copier le fichier de configuration**
```bash
cp config_template.py config.py
```

### 2. **Modifier config.py avec vos paramètres**
- Utilisez uniquement des comptes email de test
- Utilisez des mots de passe d'application Gmail (pas de mots de passe réguliers)
- Remplacez les URLs d'exemple par vos propres serveurs de test
- **JAMAIS** d'informations de production

### 3. **Modifications requises dans les fichiers**
Après avoir configuré `config.py`, modifiez les fichiers suivants pour importer votre configuration :
- `mailer/mail_sender.py`
- `mailer/malwaremail.py`
- `mailer/malware.py`
- `mailer/init_mail.py`

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

**⚠️ IMPORTANT** : Vous devez d'abord suivre les étapes de configuration ci-dessus avant d'utiliser le projet.

1. **Configuration initiale** :
   - Copiez `config_template.py` vers `config.py`
   - Remplissez vos propres paramètres dans `config.py`
   - Modifiez les fichiers dans le dossier `mailer/` pour utiliser votre configuration

2. **Exécution des scripts** :
   - **Étape 1** : Exécutez `init_mail.py` pour envoyer l'email initial contenant le lien vers `bienvenue.exe`.
   - **Étape 2** : Une fois que la victime télécharge et exécute `bienvenue.exe` :
     - Les fichiers ciblés sont chiffrés.
     - Une interface utilisateur demande un paiement en crypto-monnaie.
     - Après le paiement, les fichiers sont déchiffrés automatiquement.

**⚠️ RAPPEL DE SÉCURITÉ** :
- Utilisez uniquement des emails de test que vous contrôlez
- Informez toujours les participants qu'il s'agit d'une simulation
- Ne jamais utiliser sur des systèmes de production

---

## **Exemple de configuration**
Dans `init_mail.py`, configurez les paramètres SMTP comme suit :
```python
smtp_server = "smtp.example.com"
smtp_port = 587
username = "votre_email@example.com"
password = "votre_mot_de_passe"
