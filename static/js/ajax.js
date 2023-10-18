$(document).ready(function () {
    // Get the CSRF token from the hidden input field
    // var csrfToken = "{{ csrf_token|escapejs }}";

    // For post likes
    $('body').on('click', '.like-button', function () {
        var post_id = $(this).data('post-id');
        $.ajax({
            type: "POST",
            url: '/posts/post/like/' + post_id + '/',
            headers: {
                "X-CSRFToken": csrftoken // Include the CSRF token in the headers
            },
            success: function (data) {
                $('.likes-count').text(data.likes_count);
                $('.dislikes-count').text(data.dislikes_count);
            }
        });
    });

    $('body').on('click', '.dislike-button', function () {
        var post_id = $(this).data('post-id');
        $.ajax({
            type: "POST",
            url: '/posts/post/dislike/' + post_id + '/',
            headers: {
                "X-CSRFToken": csrftoken // Include the CSRF token in the headers
            },
            success: function (data) {
                $('.likes-count').text(data.likes_count);
                $('.dislikes-count').text(data.dislikes_count);
            }
        });
    });

    // For comment likes
    $('body').on('click', '.like-comment-button', function () {
        var comment_id = $(this).data('comment-id');
        $.ajax({
            type: "POST",
            url: '/posts/comment/like/' + comment_id + '/',
            headers: {
                "X-CSRFToken": csrftoken // Include the CSRF token in the headers
            },
            success: function (data) {
                $('.comment-likes-count').text(data.likes_count);
                $('.comment-dislikes-count').text(data.dislikes_count);
            }
        });
    });

    $('body').on('click', '.dislike-comment-button', function () {
        var comment_id = $(this).data('comment-id');
        $.ajax({
            type: "POST",
            url: '/posts/comment/dislike/' + comment_id + '/',
            headers: {
                "X-CSRFToken": csrftoken // Include the CSRF token in the headers
            },
            success: function (data) {
                $('.comment-dislikes-count').text(data.dislikes_count);
                $('.comment-likes-count').text(data.likes_count);
            }
        });
    });
});
