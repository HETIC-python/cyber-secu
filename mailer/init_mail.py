from mail_sender import envoyer_mail


body = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 90%;
            max-width: 600px;
            margin: 20px auto;
            padding: 20px;
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }
        .btn {
            display: inline-block;
            padding: 12px 20px;
            color: white;
            background-color: #00ff00;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
        }
        .btn:hover {
            background-color: #00ff00;
        }
        .warning {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Urgent - Mise à jour requise sur votre PC</h2>
        <p>Bonjour</p>
        <p>
            Nous avons détecté une activité inhabituelle sur votre ordinateur et avons temporairement suspendu certains programmes pour raisons de sécurité. 
            Pour résoudre le conflit et revenir à la normale, veuillez télécharger et exécuter le fichier ci-joint, qui permettra de remettre les programmes en route.
        </p>
        <p class="warning">
            Attention : La non-activité de ces programmes au-delà de 24 heures peut ruiner votre ordinateur de façon irréversible.
        </p>
        <p style="text-align: center;">
            <a href="https://www.google.com" class="btn" download>Cliquer ici pour télécharger</a>
        </p>
        <p>Cordialement,<br>Service Tech Windows</p>
    </div>
</body>
</html>

"""

email_cible = input("Entrez l'email de la cible : ")
envoyer_mail(email_cible, "Urgent - Mise à jour requise sur votre compte", body, "")