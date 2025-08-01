function formatDate(dateStr) {
    if (!dateStr) return '';
    const date = new Date(dateStr);
    if (isNaN(date)) return dateStr;  // fallback if date invalid
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    return date.toLocaleDateString('en-US', options);
}


$(document).ready(function () {
    $('.load-more-btn').on('click', function () {
        var genre = $(this).data('genre');
        var container = $(`#genre-${genre} .movie-list`)
        var page = parseInt(container.data('page')) + 1

        $.get(`/movies/genre-movies/?genre=${genre}&page=${page}`, function (data) {
           const $loadMoreBtn = container.find(`.load-more-btn[data-genre="${genre}"]`);
            data.movies.forEach(function (movie) {
                col = $(`<div class="me-3 movie-card" >
            <a class = 'text-decoration-none text-reset' href="/movies/movies-details/${movie.id}">
            <img src="https://image.tmdb.org/t/p/w500/${movie.poster_path}" class="img-fluid rounded"
                alt="${movie.title}">

            <div class="movie-title mt-2" data-title="${movie.title}">
                <strong>${movie.title}</strong>
            </div></a>

            <div class="text-muted small light">${formatDate(movie.release_date)}</div>
        </div>`)





                // container.children().last().before(col);
                // container.append(col);
                $loadMoreBtn.before(col);
                container.data('page', page);
                if (!data.has_next) {
                    $(`.load-more-btn[data-genre="${genre}"]`).remove();
                }

            })

        })
    });


    // Create tooltip once and reuse

    const $tooltip = $('<div id="movie-tooltip"></div>').css({
        position: 'fixed',
        padding: '6px 10px',
        background: 'rgba(0, 0, 0, 0.85)',
        color: '#fff',
        fontSize: '0.75rem',
        borderRadius: '4px',
        whiteSpace: 'nowrap',
        zIndex: 9999,
        pointerEvents: 'none',
        opacity: 0,
        transition: 'opacity 0.2s ease'
    }).appendTo('body');



    $(document).on('mouseenter', '.movie-title', function (e) {
        const title = $(this).data('title');
        $(this).css({
            color: '#10B981',
        });
        $tooltip.text(title).css({ opacity: 1 });
    }).on('mousemove', '.movie-title', function (e) {
        $tooltip.css({
            top: e.clientY - 40,
            left: e.clientX + 10
        });
    }).on('mouseleave', '.movie-title', function () {
        $tooltip.css({ opacity: 0 });
    }).on('mouseleave', '.movie-title', function (e) {
        $(this).css({
            color: 'rgba(0, 0, 0, 0.85)',
        });
    })






})