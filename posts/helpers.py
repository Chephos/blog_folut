from . import workers


def user_has_liked(obj, user):
    if user in obj.likes.all():
        return True
    return False


def user_has_disliked(obj, user):
    if user in obj.dislikes.all():
        return True
    return False


def toggle_like_for_post(user, post_id):
    if user.is_authenticated:
        post = workers.Post._get_post_by_id(post_id)
        if user_has_disliked(obj=post, user=user):
            post.dislikes.remove(user)
        if user_has_liked(obj=post, user=user):
            post.likes.remove(user)
        else:
            post.likes.add(user)


def toggle_dislike_for_post(user, post_id):
    if user.is_authenticated:
        post = workers.Post._get_post_by_id(post_id)
        if user_has_liked(obj=post, user=user):
            post.likes.remove(user)
        if user_has_disliked(obj=post, user=user):
            post.dislikes.remove(user)
        else:
            post.dislikes.add(user)


def toggle_like_for_comment(user, comment_id):
    if user.is_authenticated:
        comment = workers.Comment.get_comment_by_id(comment_id)
        if user_has_disliked(obj=comment, user=user):
            comment.dislikes.remove(user)
        if user_has_liked(obj=comment, user=user):
            comment.likes.remove(user)
        else:
            comment.likes.add(user)


def toggle_dislike_for_comment(user, comment_id):
    if user.is_authenticated:
        comment = workers.Comment.get_comment_by_id(comment_id)
        if user_has_liked(obj=comment, user=user):
            comment.likes.remove(user)
        if user_has_disliked(obj=comment, user=user):
            comment.dislikes.remove(user)
        else:
            comment.dislikes.add(user)
