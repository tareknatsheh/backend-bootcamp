from __future__ import annotations

class User:
    """The basic domain of the application
    """
    def __init__(self, username: str) -> None:
        """Constructor

        Args:
            username (str): every user must have a unique username
        """
        self.username = username
        self.following: list[str] = []

    def follow(self, other_user: str) -> None:
        """A User can follow other users

        Args:
            other_user (str): the other user unique username to follow
        """
        if other_user not in self.following:
            self.following.append(other_user)

    def post_message(self, message: str) -> None:
        """A user can post a message, which is a string added to the 'posts' global vaiable

        Args:
            message (str): the message
        """
        post = {'message': message}
        user_posts = posts.get(self.username, [])
        user_posts.append(post)
        posts[self.username] = user_posts


# Assume posts are stored in a global list
"""
posts = {
 "user1": [{}, {}, {}],
 "user2": [{}, {}, {}],
 ... etc
}
"""
posts = dict()