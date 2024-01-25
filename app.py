from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcola_valore', methods=['POST'])
def calcola_valore():
    # Recupera i dati inviati dalla richiesta POST
    data = request.json

    # Recupera i valori inseriti dall'utente
    colore = data['colore'].lower()
    sfumatura_colore = float(data['sfumatura_colore'])
    purezza = float(data['purezza'])
    taglio = float(data['taglio'])
    carato = float(data['carato'])
    provenienza = data['provenienza'].lower()
    trattamenti = data['trattamenti'].lower()

    # Calcola il valore dello zaffiro
    peso_colore = {
        'pappadasha': 0.3,
        'royal blue': 0.25,
        'cornflower blue': 0.2,
        'kashmir blue': 0.15,
        'ceylon blue': 0.1
    }

    peso_sfumatura_colore = 0.1
    peso_purezza = 0.15
    peso_taglio = 0.2
    peso_carato = carato < 1.0 and 0.2 or 0.3
    peso_provenienza = {
        'sri lanka': 0.3,
        'birmania': 0.25,
        'thailandia': 0.2,
        'australia': 0.15,
        'altro': 0.1
    }
    peso_trattamenti = trattamenti == 'no' and 0.1 or 0.5

    valore_ponderato = (
        peso_colore[colore] * (1 - sfumatura_colore) +
        peso_sfumatura_colore * sfumatura_colore +
        peso_purezza * purezza +
        peso_taglio * taglio +
        peso_carato * carato +
        peso_provenienza[provenienza] +
        peso_trattamenti
    )

    # Calcola il valore finale
    valore_finale = 300 * valore_ponderato

    # Ritorna il risultato come JSON
    return jsonify({'valore_finale': round(valore_finale, 2)})

if __name__ == '__main__':
    app.run(debug=True)
