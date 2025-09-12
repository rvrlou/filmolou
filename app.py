from flask import Flask, render_template

app = Flask(__name__)

films = [
    {
        "titre": "Fury",
        "annee": 2014,
        "genre": ["Guerre", "Drame", "Action"],
        "plateforme": ["Netflix"],
        "image": "fury.jpg",
        "description": "Pendant les derniers mois de la Seconde Guerre mondiale, un équipage de char américain dirigé par le sergent 'Wardaddy' (Brad Pitt) affronte les forces nazies dans une mission désespérée derrière les lignes ennemies."
    },
    {
        "titre": "Le brio",
        "annee": 2017,
        "genre": ["Comédie", "Drame"],
        "plateforme": ["Prime Video","Disney+","Canal+"],  # ✅ Ajout de la plateforme
        "image": "LeBrio.jpg",
        "description": "Une étudiante brillante mais impulsive et son professeur exigeant apprennent à se respecter et à travailler ensemble lorsqu'elle participe à un concours d'éloquence prestigieux."
    },
    {
        "titre": "American History X",
        "annee": 1998,
        "genre": ["Social", "Drame"],
        "plateforme": ["Payant"],  # ✅ Ajout de la plateforme
        "image": "Americanhistoryx.jpg",
        "description": "Derek Vinyard, skinhead néonazi, purge une peine de prison pour un meurtre. Transformé, il tente d’empêcher son frère de suivre le même chemin de haine et d’extrémisme."
    },
    {
        "titre": "Parasite",
        "annee": 2019,
        "genre": ["Drame", "Thriller"],   # toujours une LISTE
        "plateforme": ["Payant"],  # LISTE aussi
        "image": "Parasite.jpg",
        "description": "Une famille pauvre s'infiltre progressivement dans la vie d'une famille riche en se faisant engager comme employés, mais leur plan dérape dans une série d’événements inattendus et sombres."
    },{
        "titre": "Nous trois ou rien",
        "annee": 2015,
        "genre": ["comedie dramatique"],   # toujours une LISTE
        "plateforme": ["Payant"],  # LISTE aussi
        "image": "Nous3ourien.jpg",
        "description": "Inspiré de l’histoire vraie du père de Kheiron : Hibat Tabib, militant démocrate en Iran. Le film retrace son combat politique, son emprisonnement, puis l’exil de sa famille vers la France."
    },
    {   "titre": "Zodiac",
        "annee": 2007,
        "genre": ["Policier", "Thriller"],  
        "plateforme": ["Paramont+","HBO Max"],  
        "image": "Zodiac.jpg",
        "description": "Inspiré d’une histoire vraie, un dessinateur de presse et deux journalistes enquêtent sur le mystérieux tueur du Zodiac qui terrorisait San Francisco dans les années 60-70."
    }

]

@app.route('/')
def index():
    return render_template('index.html', films=films)

if __name__ == "__main__":
    app.run(debug=True)
