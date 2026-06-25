from flask import Flask, request
import requests

app = Flask(__name__)

usuarios_estado = {}

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    
    try:
        numero = data["entry"][0]["changes"][0]["value"]["messages"][0]["from"]
        mensaje = data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]

        mensaje = mensaje.strip().lower()

        # Crear estado si no existe
        if numero not in usuarios_estado:
            usuarios_estado[numero] = "menu_principal"

        estado = usuarios_estado[numero]

        # ===== FUNCIÓN GLOBAL ASESOR =====
        if "asesor" in mensaje:
            respuesta = """Un asesor se comunicará muy pronto contigo. ¡Hasta pronto!"""
            
            usuarios_estado[numero] = "menu_principal"
            enviar_mensaje(numero, respuesta)
            return "ok", 200

        # ===== MENÚ PRINCIPAL =====
        if mensaje in ["hola", "menu"]:
            usuarios_estado[numero] = "menu_principal"
            respuesta = """👋 ¡Bienvenido/a! soy Bienestar Bot y estaré ayudándote en esta ocasión.
Selecciona una opción de las que te presentaré a continuación:

1️⃣ Información
2️⃣ Productos
3️⃣ Si deseas comunicarte con un asesor, escribe la palabra "Asesor".

Responde con el número."""

        elif estado == "menu_principal" and mensaje == "1":
            usuarios_estado[numero] = "submenu_info"
            respuesta = """¡Vale!, ¿Sobre qué deseas información?

1️⃣ ¿Cómo se llama la compañía y de qué trata?
2️⃣ ¿Qué es el "Equipo de Triunfo"?
3️⃣ ¿Cómo puedes tener un mejor estilo de vida sin dejar atrás tu ocupación?
"""

        elif estado == "menu_principal" and mensaje == "2":
            usuarios_estado[numero] = "submenu_productos"
            respuesta = """📦 Productos principales 4Life:

1️⃣ Transfer Factor Plus® ⭐
2️⃣ BioEFA™
3️⃣ Transfer Factor Vistari®
4️⃣ Renuvo®
5️⃣ Pre/O Biotics®
6️⃣ Glutamine
7️⃣ Tri-Factor® Formula
8️⃣ Belle Vie®
9️⃣ Fibre System
🔟 RioVida®

Escribe el número del producto para ver más información.
Si no está el producto de tu interés escribe "Asesor" y con mucho gusto te atenderemos.

Responde con el número."""

        # ===== SUBMENÚ INFORMACIÓN =====
        elif estado == "submenu_info" and mensaje == "1":
            respuesta = """La compañía tiene por nombre 4Life Research®, líder mundial en la ciencia del sistema inmunitario y pionera en la comercialización de los Factores de Transferencia.

¿De qué trata el proyecto?
Se basa en dos pilares fundamentales:

Ciencia y Salud: Ofrecemos productos de biotecnología diseñados para educar, fortalecer y equilibrar tus defensas. No son simples vitaminas, son moléculas mensajeras de inteligencia inmunitaria.

Oportunidad de Negocio: 4Life utiliza el modelo de Network Marketing, permitiéndote generar ingresos al conectar a otros con estos productos. Puedes construir un activo financiero que te brinde libertad de tiempo.

¿Cómo empezar?
Puedes registrarte como Cliente Preferente para comprar a precio de mayorista o como Afiliado para construir tu propia red.

¿Deseas más información? Escribe la palabra "Asesor" y te daremos toda la información.
"""

        elif estado == "submenu_info" and mensaje == "2":
            respuesta = """¿Qué es el Equipo de Triunfo?
Es una organización de liderazgo y formación empresarial fundada por el Dr. José Pérez y Sara Meléndez. Su objetivo principal es educar a personas para que desarrollen sus propios negocios a través de la industria del Network Marketing (Amway).

¿Qué ofrecen?

Sistema Educativo: Acceso a audios, libros y convenciones sobre inteligencia emocional y finanzas.

Mentoría: Guía directa de líderes con décadas de experiencia en la construcción de activos.

Comunidad: Un entorno de apoyo para emprendedores que buscan libertad de tiempo y bienestar integral.

¿Deseas más información? Escribe la palabra "Asesor" y te daremos toda la información."""

        elif estado == "submenu_info" and mensaje == "3":
            respuesta = """Excelente decisión ✨
Un asesor se comunicará muy pronto contigo. ¡Hasta pronto!
"""

        # ===== SUBMENÚ PRODUCTOS =====
        elif estado == "submenu_productos" and mensaje == "1":
            respuesta = """⭐ Transfer Factor Plus®

Fórmula avanzada con zinc y vitaminas.
• El zinc contribuye al funcionamiento normal del sistema inmunitario.
• Las vitaminas A, C y E contribuyen a la protección de las células frente al daño oxidativo.

Producto diseñado para complementar una dieta equilibrada.
"""

        elif estado == "submenu_productos" and mensaje == "2":
            respuesta = """🟢 BioEFA™

Suplemento de ácidos grasos esenciales omega-3 y omega-6.
Aporta nutrientes esenciales dentro de una alimentación saludable.
"""

        elif estado == "submenu_productos" and mensaje == "3":
            respuesta = """🔵 Transfer Factor Vistari®

• La vitamina A juega un papel fundamental en la visión.
• El zinc contribuye al funcionamiento normal del sistema inmunitario.

Diseñado para complementar una dieta equilibrada.
"""

        elif estado == "submenu_productos" and mensaje == "4":
            respuesta = """🟡 Renuvo®

• El zinc contribuye al funcionamiento normal del sistema inmunitario.
• La vitamina D contribuye al funcionamiento normal del sistema inmunitario.

Aporta nutrientes dentro de una alimentación equilibrada.
"""

        elif estado == "submenu_productos" and mensaje == "5":
            respuesta = """🟠 Pre/O Biotics®

Combinación de probióticos y prebióticos.
Puede ayudar a normalizar funciones digestivas dentro de una alimentación adecuada.
"""

        elif estado == "submenu_productos" and mensaje == "6":
            respuesta = """🟣 Glutamine

Aminoácido presente en alimentos y suplementos.
Complementa la nutrición dentro de una dieta equilibrada.
"""

        elif estado == "submenu_productos" and mensaje == "7":
            respuesta = """🔴 Tri-Factor® Formula

Combinación de proteínas que complementan la alimentación diaria
con nutrientes valiosos.
"""

        elif estado == "submenu_productos" and mensaje == "8":
            respuesta = """💖 Belle Vie®

Diseñado con ingredientes nutritivos enfocados en el bienestar
como parte de una alimentación equilibrada.
"""

        elif estado == "submenu_productos" and mensaje == "9":
            respuesta = """🟤 Fibre System

Fuente de fibra dietaria.
Complementa una alimentación sana y puede contribuir a la regulación intestinal.
"""

        elif estado == "submenu_productos" and mensaje == "10":
            respuesta = """⚪ RioVida®

Bebida nutritiva con mezcla de frutas.
Rica en antioxidantes naturales que complementan una dieta equilibrada.
"""

        enviar_mensaje(numero, respuesta)

    except Exception as e:
        print("Error:", e)

    return "ok", 200
if __name__ == "__main__":
    app.run(port=5000, debug=True)
