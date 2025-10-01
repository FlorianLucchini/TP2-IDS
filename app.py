from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message


mail = Mail()
app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'devtestingdev2@gmail.com'
app.config['MAIL_PASSWORD'] = 'ajyo zinv jddg japi'
app.config['MAIL_DEFAULT_SENDER'] = ('TP2-IDS', 'devtestingdev2@gmail.com')

# Conectar Flask-Mail con la app
mail.init_app(app) 

# Información del evento
info_evento = {
    1: {
        "nombre": "Rally MTB 2025",
        "organizador": "Club Social y Deportivo Unidos por el Deporte",
        "descripcion": "Carrera de MTB rural en dos modalidades 30km y 80km …",
        "fecha": "24 de Octubre de 2025",
        "horario": "8:00 hs",
        "lugar": "Tandil, Buenos Aires",
        "largada": "Av Alvear y Callao",
        "tipo_carrera": "MTB rural",
        "modalidad_costo": {
            1: {"nombre": "Distancia Corta", "valor": "100"},
            2: {"nombre": "Distancia Larga", "valor": "200"},
        },
        "Auspiciantes": [
            {
                "nombre": "Adidas",
                "logo": "images/auspiciantes/adidas.svg"
            },
            {
                "nombre": "Aerolineas Argentinas",
                "logo": "images/auspiciantes/aerolineas-arg.svg"
            },
            {
                "nombre": "Binance",
                "logo": "images/auspiciantes/binance.svg"
            },
            {
                "nombre": "Linux",
                "logo": "images/auspiciantes/linux.svg"
            },
            {
                "nombre": "Red Hat",
                "logo": "images/auspiciantes/red-hat.svg"
            },
            {
                "nombre": "Santander",
                "logo": "images/auspiciantes/santander.svg"
            },
            {
                "nombre": "Shimano",
                "logo": "images/auspiciantes/shimano.svg"
            },
            {
                "nombre": "Stanley",
                "logo": "images/auspiciantes/stanley.svg"
            },
        ],
        "mapas":{
                "30": "https://www.google.com/maps/d/u/0/embed?mid=1LqZNAYrVNeR_wx14DsdN41flpj3P800&ehbc=2E312F",
                "80": "https://www.google.com/maps/d/u/0/embed?mid=1y8KSYo-IM6fD5wMLvzg4ulV78IomJ_w&ehbc=2E312F"
        }
    }
}

#Rutas
@app.route("/")
def redirection():
    return redirect(url_for("tandil80k"))

@app.route("/80k")
def tandil80k():
    evento = info_evento[1]
    return render_template("index.html", section=80, evento=evento)


@app.route("/30k")
def tandil30k():
    evento = info_evento[1]
    return render_template("index.html", section=30, evento=evento)


@app.route("/registration", methods=["GET"])
def registration():
    evento = info_evento[1]
    return render_template("registration.html", evento=evento)

# Manejo del formulario
@app.route("/registration", methods=["POST"])
def submit_registration():
    #Captura de datos del formulario 
    nombre = request.form.get("nombre")
    email = request.form.get("email")
    telefono = request.form.get("telefono")
    fecha_nacimiento = request.form.get("fecha_nacimiento")
    categoria = request.form.get("categoria")
    genero = request.form.get("genero")
    deslinde = request.files.get("deslinde") 
    
    # Validación
    if not all([nombre, email, telefono, fecha_nacimiento, categoria, genero]) or not deslinde: 
        return redirect(url_for('registration'))

    #Procesamiento de datos y construcción del email
    evento = info_evento[1]
    modalidad_nombre = evento['modalidad_costo'][int(categoria)]['nombre']

    asunto = f"Nueva Inscripción para {evento['nombre']}: {nombre}"
    cuerpo_del_mensaje = f"""
        Se ha recibido una nueva inscripción con los siguientes datos:

        - Nombre: {nombre}
        - Email: {email}
        - Teléfono: {telefono}
        - Modalidad: {modalidad_nombre}
        - Género: {genero}
        - Fecha de Nacimiento: {fecha_nacimiento}
    """
    
    # Creación y envío del correo
    msg = Message(subject=asunto,
                  recipients=["lpeneff@fi.uba.ar"], 
                  body=cuerpo_del_mensaje)
    

    msg.attach(deslinde.filename, deslinde.content_type, deslinde.read())
    
    mail.send(msg)

    # Redirección
    return redirect(url_for('registration'))

if __name__ == "__main__":
    app.run("localhost", 8080, debug=True)