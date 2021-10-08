rom flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('app.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        ativa = request.form['ativa']
        empregada = request.form['empregada']
        estudante = request.form['estudante']
        crianca = request.form['crianca']
        adulto = request.form['adulto']
        idoso = request.form['idoso']        
    
        faculdade_ativa = float(ativa)*0.5
        faculdade_empregada = float(empregada)*0.4
        faculdade_estudante = float(estudante)
        faculdade_crianca = float(crianca)*0
        faculdade_adulto = float(adulto)*0.23
        faculdade_idoso = float(idoso)*0.05

        escola_ativa = float(ativa)*0.2
        escola_empregada = float(empregada)*0.1
        escola_estudante = float(estudante)*0
        escola_crianca = float(crianca)*0.9
        escola_adulto = float(adulto)*0.12
        escola_idoso = float(idoso)*0

        escola = escola_ativa + escola_empregada +\
        escola_estudante + escola_crianca + escola_adulto + escola_idoso

        faculdade = faculdade_ativa + faculdade_empregada + faculdade_estudante +\
            faculdade_crianca + faculdade_adulto + faculdade_idoso

        numero_escola = int(escola/40)

        fluxo_real_escola = numero_escola*40

        numero_faculdade = int(faculdade/50)

        fluxo_real_faculdade = numero_faculdade*50

        fluxo_total = fluxo_real_escola + fluxo_real_faculdade

        sum = escola + faculdade 
        return render_template('app.html', sum=sum,escola=escola,
        faculdade=faculdade, numero_escola=numero_escola, numero_faculdade=numero_faculdade,
        fluxo_real_escola=fluxo_real_escola, fluxo_real_faculdade=fluxo_real_faculdade,
        fluxo_total=fluxo_total)

        


if __name__ == ' __main__':
    app.debug = True
    app.run()
