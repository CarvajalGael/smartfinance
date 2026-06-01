import smtplib
from email.mime.text import MIMEText

def enviar_codigo(correo_destino, codigo):

    remitente = "gaelito.carvajal.08@gmail.com"
    password = "siuw wrng ctlw vdel"

    mensaje = MIMEText(f"Tu código de recuperación es: {codigo}")
    mensaje["Subject"] = "Recuperación de contraseña"
    mensaje["From"] = remitente
    mensaje["To"] = correo_destino

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(remitente, password)
    server.send_message(mensaje)
    server.quit()