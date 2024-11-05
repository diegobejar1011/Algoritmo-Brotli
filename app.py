from flask import Flask, render_template, request
from models.AT import AscTranslate
from models.BC import BrolitCompressor

app = Flask("Brotli Compress")

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/procesar', methods=['POST'])
def procesar():
    cadena = request.form["input-word"]
    at = AscTranslate()
    expression = at.transalate(cadena)
    if(expression):
        bc = BrolitCompressor(expression)
        resultado = bc.compress()
    else:
        resultado = "Error en la traducción"
    return render_template("index.html", resultado=resultado, entrada=cadena)


if __name__ == "__main__": 
    app.run(debug=True, host="0.0.0.0", port="5000")