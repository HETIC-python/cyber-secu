import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def envoyer_mail(to, subject, body, filename):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  
    username = "fglindayi@gmail.com"
    password = "abkp ifgv ywxc ouyc" 

    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    file_path = filename 
    print("J'ai attaché une pièce jointe ")
    
    try:
        if len(filename) > 0:
            with open(file_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())

            # Encodage du fichier en Base64
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={filename}",
            )
            part.add_header("Content-ID", "<attached_file>") 
            msg.attach(part)

    except Exception as e:
        print(f"Erreur lors de l'ouverture du fichier : {e}")
        return

    server = None  
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  
        server.login(username, password)
        text = msg.as_string()
        server.sendmail(username, to, text) 
        print("Email envoyé avec succès !")
    except Exception as e:
        print(f"Erreur: {e}")
    finally:
        if server:  
            server.quit()
            print("Connexion SMTP fermée.")
