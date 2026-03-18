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
        "image": "Willhunting.jpg",
        "description": "Will Hunting, un jeune homme brillant mais perturbé, travaille comme concierge au MIT. Lorsqu'il résout un problème mathématique complexe, un professeur le prend sous son aile et l'aide à surmonter ses démons intérieurs."
    },
    {
        "titre": "Les Larmes du soleil",
        "annee": 2003,
        "genre": ["Guerre", "Drame", "Action"],
        "plateforme": ["Payant"],
        "image": "leslarmesdusoleil.jpg",
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
        "titre": "Boîte noire",
        "annee": 2021,
        "genre": ["Thriller"],
        "plateforme": ["Payant"],
        "image": "boitenoire.jpg",
        "description": "Après un crash aérien, un technicien de l'aviation civile découvre des anomalies dans les boîtes noires et mène une enquête secrète pour découvrir la vérité."
    },
    {
        "titre": "Spider-Man: New Generation",
        "annee": 2018,
        "genre": ["Animation", "Action"],
        "plateforme": ["Amazon Prime Video"],
        "image": "spiderman.jpg",
        "description": "Miles Morales devient Spider-Man et rencontre d'autres versions de Spider-Man venant de dimensions parallèles pour combattre un ennemi commun."
    },
    {
        "titre": "PRISONERS",
        "annee": 2013,
        "genre": ["Thriller", "Policier"],
        "plateforme": ["Amazon Prime Video"],
        "image": "Prisoners.jpg",
        "description": "Après la disparition de sa fille et de son amie, un père dévasté se brouille avec le policier chargé de l'affaire et décide de prendre les choses en main."
    },
       {
        "titre": "Silenced",
        "annee": 2011,
        "genre": ["Drame", "Thriller"],
        "plateforme": ["Netflix"],
        "image": "silenced.jpg",
        "description": "Basé sur des faits réels, ce film dénonce les abus sexuels et la corruption dans un internat pour enfants sourds en Corée du Sud."
    },
     {
        "titre": "Sauver ou périr   ",
        "annee": 2018,
        "genre": ["Drame",],
        "plateforme": ["Netflix"],
        "image": "sauverouperir.jpg",
        "description": "Un pompier parisien, grièvement blessé lors d'une intervention, lutte pour retrouver sa place dans son équipe et sa vie personnelle."    
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
        "image": "Americanhistoryx.jpg",
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
        "genre": ["Comédie", "dramatique"],
        "plateforme": ["Payant"],
        "image": "Nous3ourien.jpg",
        "description": "Inspiré de l’histoire vraie du père de Kheiron : Hibat Tabib, militant démocrate en Iran. Le film retrace son combat politique, son emprisonnement, puis l’exil de sa famille vers la France."
    },
    {
        "titre": "Zodiac",
        "annee": 2007,
        "genre": ["Policier", "Thriller"],
        "plateforme": ["Paramount+", "HBO Max"],
        "image": "Zodiac.jpg",
        "description": "Inspiré d’une histoire vraie, un dessinateur de presse et deux journalistes enquêtent sur le mystérieux tueur du Zodiac qui terrorisait San Francisco dans les années 60-70."
    },
#ajouter les photo
    {    "titre": "La ligne verte",
        "annee": 1999,
        "genre": ["Drame"],
        "plateforme": ["Payant"],
        "image": "laligne.jpg",
        "description": "Un gardien de prison découvre que l'un de ses détenus possède des pouvoirs surnaturels qui pourraient changer le cours de sa vie."
    },
     {    "titre": "Polisse",
        "annee": 2011,
        "genre": ["Drame","Policier"],
        "plateforme": ["Payant"],
        "image": "polisse.jpg",
        "description": "Au sein de la Brigade de Protection des Mineurs, des policiers confrontent quotidiennement la violence, la souffrance et leurs propres limites."
    },
     {    "titre": "Les blancs ne savent pas sauter",
        "annee": 2011,
        "genre": ["Comeddie"],
        "plateforme": ["Payant"],
        "image": "lesblancs.jpg",
        "description": "Au sein de la Brigade de Protection des Mineurs, des policiers confrontent quotidiennement la violence, la souffrance et leurs propres limites."
    },
    {
    "titre": "Caddo Lake",
    "annee": 2024,
    "genre": ["Drame", "Thriller"],
    "plateforme": ["HBO MAX"],
    "image": "caddo.jpg",
    "description": "Après la disparition mystérieuse d’une petite fille, une connexion inquiétante s’établit avec d’anciennes affaires de meurtres et d’énigmes non résolues." 
},
    {
    "titre": "Je verrai toujours vos visages",
    "annee": 2023,
    "genre": ["Drame"],
    "plateforme": ["Canal+", "Apple TV+"],
    "image": "jever.jpg",
    "description": "Un film dramatique français explorant la justice réparatrice en suivant victimes et auteurs d’infractions qui tentent de dialoguer et de se reconstruire après des actes traumatisants." 
},{
    "titre": "Je verrai toujours vos visages",
    "annee": 2023,
    "genre": ["Drame"],
    "plateforme": ["Canal+", "Apple TV+"],
    "image": "jever.jpg",
    "description": "Un film dramatique français explorant la justice réparatrice en suivant victimes et auteurs d’infractions qui tentent de dialoguer et de se reconstruire après des actes traumatisants." 
},
{
    "titre": "Peur primale",
    "annee": 1996,
    "genre": ["Drame", "Policier", "Thriller"],
    "plateforme": ["Paramount+"],
    "image": "peurprimal.jpg",
    "description": "Un brillant avocat défend un jeune homme accusé du meurtre d’un archevêque et découvre une affaire pleine de manipulations et de vérités choquantes." 
}
]

# Route principale
@app.route('/')
def index():
    return render_template('index.html', films=films)

# Lancer l'application
if __name__ == "__main__":
    app.run(debug=True)
