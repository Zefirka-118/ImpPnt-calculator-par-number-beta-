from flask import Flask, render_template, request
from entidades.number import Number

app = Flask(__name__)



#request -> petición
#response -> respuesta
#client -> cliente


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/par')
def par():
    return render_template('par.html', resultado = None)

@app.route('/azador')
def azador():
    return render_template('azador.html')

@app.route('/definir_par', methods=['POST'])
def realizar_operación():
    try:
        
        num1 = int(request.form.get('value'))

        number = Number(num1)
        resultado = number.es_par()
        
    
        return render_template('par.html', resultado=resultado)
    
    except (ValueError, TypeError):
        # En caso de error 
        return render_template('par.html', resultado="Error: Ingresa números válidos")
    


    

    



if __name__ == '__main__':
    app.run(debug=True)