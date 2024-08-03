from flask import Flask, request, render_template,flash
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Necesario para usar flash y sesiones

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/acerca')
def acerca():
    return render_template('acerca.html')
@app.route('/proyectos')
def portafolio():
    return render_template('portafolio.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        asunto = request.form['asunto']
        mensaje = request.form['mensaje']
        
        # Aquí puedes procesar el formulario (por ejemplo, enviando un email)
        enviar_email(nombre, email, asunto, mensaje)
        flash('Gracias por tu mensaje. Mail eviado correctamente.', 'success')
        
        return render_template('index.html')
    return render_template('contacto.html')
import yagmail

def enviar_email(nombre, email, asunto, mensaje):
    contenido = f"Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}"
    yag = yagmail.SMTP("pedrielmarta79@gmail.com", "yamx oibf psea vxnv")
    yag.send(
        to="pedrielmarta79@gmail.com",
        subject=f"Nuevo mensaje de contacto: {asunto}",
        contents=contenido
    )

# Instala yagmail con: pip install yagmail
def enviar_email2(nombre, email, asunto, mensaje):
    # Configura esto con tus datos de email
    email_emisor = email
    email_password = "yamx oibf psea vxnv"
    email_receptor = "martainesped@gmail.com"

    msg = MIMEText(f"Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}")
    msg['Subject'] = f"Nuevo mensaje de contacto: {asunto}"
    msg['From'] = email_emisor
    msg['To'] = email_receptor

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(email_emisor, email_password)
       smtp_server.sendmail(email_emisor, email_receptor, msg.as_string())

if __name__ == '__main__':
    app.run(debug=True)