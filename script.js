function caricaSfumature() {
    const colore = document.getElementById('colore').value.toLowerCase();
    const sfumaturaContainer = document.getElementById('sfumatura-container');
    sfumaturaContainer.style.display = (colore === 'pappadasha') ? 'none' : 'block';
}

function calcolaValore() {
    const colore = document.getElementById('colore').value.toLowerCase();
    const sfumaturaColore = parseFloat(document.getElementById('sfumatura').value) || 0;
    const purezza = parseFloat(document.getElementById('purezza').value) || 0;
    const taglio = parseFloat(document.getElementById('taglio').value);
    const carato = parseFloat(document.getElementById('carato').value) || 0;
    const provenienza = document.getElementById('provenienza').value.toLowerCase();
    const trattamenti = document.getElementById('trattamenti').value.toLowerCase();

    if (isNaN(sfumaturaColore) || isNaN(purezza) || isNaN(taglio) || isNaN(carato)) {
        console.error('Valori numerici non validi.');
        return;
    }

    fetch('/calcola_valore', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            colore,
            sfumatura_colore: sfumaturaColore,
            purezza,
            taglio,
            carato,
            provenienza,
            trattamenti,
        }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Errore HTTP! Codice: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('risultato-container').classList.remove('hidden');
        document.getElementById('valore-finale').textContent = data.valore_finale;
    })
    .catch(error => {
        console.error('Errore durante la richiesta fetch:', error);
    });
}
