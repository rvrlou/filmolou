from flask import Flask, render_template, url_for

app = Flask(__name__)

# ✅ Liste des films
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
        "titre": "Will Hunting",
        "annee": 1997,
        "genre": ["Drame"],
        "plateforme": ["Netflix"],
        "image": "WillHunting.jpg",
        "description": "Will Hunting, un jeune homme brillant mais perturbé, travaille comme concierge au MIT. Lorsqu'il résout un problème mathématique complexe, un professeur le prend sous son aile et l'aide à surmonter ses démons intérieurs."
    },
    {
        "titre": "Les Larmes du soleil",
        "annee": 2003,
        "genre": ["Guerre", "Drame", "Action"],
        "plateforme": ["Payant"],
        "image": "LesLarmesDuSoleil.jpg",
        "description": "Un groupe de Navy SEALs est envoyé au Nigéria pour sauver une médecin américaine. Ils décident de protéger également des civils africains, mettant leur mission en danger."
    },
    {
        "titre": "The Revenant",
        "annee": 2015,
        "genre": ["Drame", "Aventure"],
        "plateforme": ["Disney+"],
        "image": "therevenant.jpg",
        "description": "Hugh Glass, un trappeur du XIXe siècle, survit à une attaque d'ours et à une trahison. Il lutte pour sa survie et cherche à se venger de ceux qui l'ont abandonné."
    },
    {
        "titre": "Le Brio",
        "annee": 2017,
        "genre": ["Comédie", "Drame"],
        "plateforme": ["Prime Video","Disney+","Canal+"],
        "image": "LeBrio.jpg",
        "description": "Une étudiante brillante mais impulsive et son professeur exigeant apprennent à se respecter et à travailler ensemble lorsqu'elle participe à un concours d'éloquence prestigieux."
    },
    {
        "titre": "American History X",
        "annee": 1998,
        "genre": ["Social", "Drame"],
        "plateforme": ["Payant"],
        "image": "AmericanHistoryX.jpg",
        "description": "Derek Vinyard, skinhead néonazi, purge une peine de prison pour un meurtre. Transformé, il tente d’empêcher son frère de suivre le même chemin de haine et d’extrémisme."
    },
    {
        "titre": "Parasite",
        "annee": 2019,
        "genre": ["Drame", "Thriller"],
        "plateforme": ["Payant"],
        "image": "Parasite.jpg",
        "description": "Une famille pauvre s'infiltre progressivement dans la vie d'une famille riche en se faisant engager comme employés, mais leur plan dérape dans une série d’événements inattendus et sombres."
    },
    {
        "titre": "Nous trois ou rien",
        "annee": 2015,
        "genre": ["Comédie dramatique"],
        "plateforme": ["Payant"],
        "image": "Nous3ouRien.jpg",
        "description": "Inspiré de l’histoire vraie du père de Kheiron : Hibat Tabib, militant démocrate en Iran. Le film retrace son combat politique, son emprisonnement, puis l’exil de sa famille vers la France."
    },
    {
        "titre": "Zodiac",
        "annee": 2007,
        "genre": ["Policier", "Thriller"],
        "plateforme": ["Paramount+", "HBO Max"],
        "image": "Zodiac.jpg",
        "description": "Inspiré d’une histoire vraie, un dessinateur de presse et deux journalistes enquêtent sur le mystérieux tueur du Zodiac qui terrorisait San Francisco dans les années 60-70."
    }
]

# Route principale
@app.route('/')
def index():
    return render_template('index.html', films=films)

# Lancer l'application
if __name__ == "__main__":
    app.run(debug=True)
