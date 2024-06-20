from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html",dados="Olá Mundo! (Exemplo de enviar dados para a página)")


if __name__ in "__main__":
  app.run (debug=True)