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

@app.route('/definir_par', methods=['POST'])
def realizar_operación():
    try:
        
        num1 = int(request.form.get('value'))

        number = Number(num1)
        resultado = number.es_par()
        
        # Los valores ahuevo tienen que ser int para ser par
        num1 = int(float(request.form.get('value1')))
        num2 = int(float(request.form.get('value2')))

        # wachar si cada uno es par (True) o impar (False)
        es_par1 = (num1 % 2 == 0)
        es_par2 = (num2 % 2 == 0)

        
        resultado = f"El {num1} es {'par' if es_par1 else 'impar'} y el {num2} es {'par' if es_par2 else 'impar'}"

        return render_template('calculadora.html', resultado=resultado)
    
    except (ValueError, TypeError):
        # En caso de error 
        return render_template('par.html', resultado="Error: Ingresa números válidos")
    

    



if __name__ == '__main__':
    app.run(debug=True)