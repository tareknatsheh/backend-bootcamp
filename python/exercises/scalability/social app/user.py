from __future__ import annotations

class User:
    """The basic domain of the application
    """
    def __init__(self, username: str) -> None:
        """Constructor

        Args:
            username (str): every user must have a username
        """
        self.username = username
        self.following = []

    def follow(self, other_user: User) -> None:
        """A User can follow other Users

        Args:
            other_user (User): the other user object to follow
        """
        if other_user not in self.following:
            self.following.append(other_user)

    def post_message(self, message: str) -> None:
        """A user can post a message, with is a string added to the 'posts' global vaiable

        Args:
            message (str): the message
        """
        post = {'username': self.username, 'message': message}
        posts.append(post)


# Assume posts are stored in a global list
posts = []