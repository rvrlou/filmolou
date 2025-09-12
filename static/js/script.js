function toggleDescription(film) {
    film.classList.toggle("open");
}

// Filtrage combiné (genre + plateforme)
function filterMovies() {
    const selectedGenre = document.getElementById('genreFilter').value;
    const selectedPlatform = document.getElementById('platformeFilter').value;
    const films = document.querySelectorAll('.film');

    films.forEach(film => {
        const genres = film.dataset.genre.split(",");
        const platforms = film.dataset.platform.split(",");

        const matchGenre = (selectedGenre === "all" || genres.includes(selectedGenre));
        const matchPlatform = (selectedPlatform === "all" || platforms.includes(selectedPlatform));

        // Affiche si les deux filtres correspondent
        if (matchGenre && matchPlatform) {
            film.style.display = "flex";
        } else {
            film.style.display = "none";
        }
    });
}

// Appelle filterMovies à chaque changement de menu déroulant
function filterByGenre() {
    filterMovies();
}

function filterByPlatform() {
    filterMovies();
}


