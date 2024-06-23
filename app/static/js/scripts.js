document.addEventListener("DOMContentLoaded", function () {
    // Prikazivanje popupa kada se klikne na sliku igre
    const games = document.querySelectorAll('.game img');
    games.forEach(game => {
        game.addEventListener('click', function () {
            const gameName = this.alt;
            openPopup(gameName);
        });
    });

    // Zatvaranje popupa kada se klikne na dugme za zatvaranje ili van popupa
    const closeBtn = document.querySelector('.popup .close');
    closeBtn.addEventListener('click', closePopup);

    window.addEventListener('click', function (event) {
        const popup = document.getElementById('gamePopup');
        if (event.target === popup) {
            closePopup();
        }
    });

    // Slanje forme prilikom prijave
    const submitBtn = document.querySelector('.popup-content button');
    submitBtn.addEventListener('click', submitForm);
});

function openPopup(gameName) {
    document.getElementById('gameName').textContent = gameName;
    document.getElementById('gamePopup').style.display = 'flex';
}

function closePopup() {
    document.getElementById('gamePopup').style.display = 'none';
}

function submitForm() {
    // Prikupljanje podataka iz forme
    const ime = document.getElementById('ime').value;
    const prezime = document.getElementById('prezime').value;
    const korisnickoIme = document.getElementById('korisnicko_ime').value;
    const trener = document.getElementById('trener').value;
    const gameName = document.getElementById('gameName').textContent;

    // Priprema podataka za slanje
    const formData = {
        ime: ime,
        prezime: prezime,
        korisnicko_ime: korisnickoIme,
        igra: gameName,
        trener: trener
    };

    // Slanje AJAX POST zahteva
    fetch('/registracija', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert(data.message);
            closePopup();
        } else {
            alert('Došlo je do greške. Molimo pokušajte ponovo.');
        }
    })
    .catch(error => {
        console.error('Greška:', error);
        alert('Došlo je do greške. Molimo pokušajte ponovo.');
    });
}
