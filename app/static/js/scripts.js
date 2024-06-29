function openPopup(gameName) {
    document.getElementById('gameName').textContent = gameName;
    document.getElementById('gamePopup').style.display = 'flex';
}

function closePopup() {
    document.getElementById('gamePopup').style.display = 'none';
}

function submitForm() {
    const ime = document.getElementById('ime').value;
    const prezime = document.getElementById('prezime').value;
    const korisnickoIme = document.getElementById('korisnicko_ime').value;
    const trenerId = document.getElementById('trener').value;
    const gameName = document.getElementById('gameName').textContent;

    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            ime,
            prezime,
            korisnickoIme,
            trenerId,
            gameName
        })
    }).then(response => {
        if (response.ok) {
            closePopup();
        } else {
            alert('Failed to submit form');
        }
    });
}
