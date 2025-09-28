from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Información del evento
info_evento = {
    1: {
        "nombre": "Rally MTB 2025",
        "organizador": "Club Social y Deportivo Unidos por el Deporte",
        "descripcion": "Carrera de MTB rural en dos modalidades 30km y 80km …",
        "fecha": "24 de Octubre de 2025",
        "horario": "8am",
        "lugar": "Tandil, Buenos Aires",
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
    nombre = request.form["nombre"]
    email = request.form["email"]
    telefono = request.form["telefono"]
    fecha_nacimiento = request.form["fecha_nacimiento"]
    categoria = request.form["categoria"]
    genero = request.form["genero"]
    archivo = request.form.get("archivo")

    if not all([nombre, email, telefono, fecha_nacimiento, categoria, genero, archivo]):
        return "Por favor completa todos los campos obligatorios."

	# Aquí se deben enviar los datos al email del organizador
    print(f"Nuevo registro: {nombre}, {email}, {telefono}, {fecha_nacimiento}, {categoria}, {genero}")

    return f"Gracias {nombre}, te registraste en la categoría {categoria}!"

if __name__ == "__main__":
    app.run("localhost", 8080, debug=True)
