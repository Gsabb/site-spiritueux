
const infosAlignement = [
    { name: 'Guillaume Sabourin', numero: 0, img: 'static/images/pdp_guillaume.jpg', role: 'Capitaine / coach' },
    { name: 'Laurent Courville', numero: 17, img: 'static/images/pdp_laurent.jpg', role: 'Assistant coach' },
    { name: 'Charles-Étienne Gagné', numero: 3, img: 'static/images/pdp_charlie.png', role: 'Capitaine Spirit' },
    { name: 'Nathan Dugal', numero: 7, img: 'static/images/pdp_nathan.jpg', role: 'Joueur/euse' },
    { name: 'Alexis Vazquez', numero: 8, img: 'static/images/pdp_vazquez.jpg', role: 'Joueur/euse' },
    { name: 'Anais Rhéaume-Gravel', numero:22 , img: 'static/images/pdp_anais.jpg', role: 'Joueur/euse' },
    { name: 'Camille Beauchamp', numero:26 , img: 'static/images/pdp_camille.jpg', role: 'Joueur/euse' },
    { name: 'Elisabeth Courville', numero:6 , img: 'static/images/pdp_eli.jpg', role: 'Joueur/euse' },
    { name: 'Émilie Anson', numero:36 , img: 'static/images/pdp_emilie.jpg', role: 'Joueur/euse' },
    { name: 'Francis Ronco', numero:911 , img: 'static/images/pdp_frank.jpg', role: 'Joueur/euse' },
    { name: 'Fred Gaudet', numero:88 , img: 'static/images/pdp_fred.jpg', role: 'Joueur/euse' },
    { name: 'Julien Novak-Bélanger', numero:12 , img: 'static/images/pdp_julien.jpg', role: 'Joueur/euse' },
    { name: 'Mégane Favreau', numero:5 , img: 'static/images/blankAvatar.png', role: 'Joueur/euse' },
    { name: 'Mélodie Marceau', numero:13 , img: 'static/images/pdp_melo.jpg', role: 'Joueur/euse' },
    { name: 'Rosalie Dugas', numero:10 , img: 'static/images/pdp_rosa.jpg', role: 'Joueur/euse' },
    { name: 'Thomas Savage-Duguay', numero:66 , img: 'static/images/pdp_thomas.jpg', role: 'Joueur/euse' },
    { name: 'Tai Yang-Larochelle', numero:1 , img: 'static/images/pdp_tai.jpg', role: 'Joueur/euse' },
];

/**
 *  Crée les éléments html correspondants à l'alignement
 */
const infosContainer = document.getElementById('alignement');
for (let i = 0; i < infosAlignement.length; i++) {
    const info = infosAlignement[i];
    const listItem = document.createElement('li');
    const avatarDiv = document.createElement('div');
    avatarDiv.classList.add('avatar');
    const img = document.createElement('img');
    img.src = info.img;
    const h3 = document.createElement('h3');
    h3.innerText = info.name;
    const h4 = document.createElement('h4');
    h4.innerText = info.numero;
    avatarDiv.appendChild(img);
    avatarDiv.appendChild(h3);
    if (info.role != null) {
        const h5 = document.createElement('h5');
        h5.innerText = info.role;
        avatarDiv.appendChild(h5);
        h5.setAttribute('id', 'role_joueur');
    }
    avatarDiv.appendChild(h4);
    listItem.appendChild(avatarDiv);
    infosContainer.appendChild(listItem);
}