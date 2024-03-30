from user import User, posts

class SocialMediaPlatform:
    def __init__(self) -> None:
        """Constructor
        the platform is initialized with an empty list of users
        """
        self.users: dict = dict()

    def register_user(self, username: str) -> User | None:
        """Registering a user addes them to the users list

        Args:
            username (str): unique username of the user
        """
        if not self._is_username_taken(username):
            user = User(username)
            self.users[username] = user
            return user

    def _is_username_taken(self, username: str) -> bool:
        """An internal method that checks the existance of a specific user

        Args:
            username (str): of the user to be checked if it exists

        Returns:
            bool: True if exists False otherwise
        """
        if username not in self.users:
            return False
        return True

    def get_user_by_username(self, username: str) -> User | None:
        """returns the User object of a specific user if found

        Args:
            username (str): of the target user to be found

        Returns:
            User | None: The target User object, or None if it does not exist
        """
        if username not in self.users:
            return None
        return self.users[username]

    def generate_timeline(self, username: str):
        """creates a list of posts of users the User is following

        Args:
            username (str): of our target User

        Returns:
            List: of posts of other users our target User is following
        """
        user = self.get_user_by_username(username)
        if not user:
            return []

        timeline = []
        for followed_user in user.following:
            if followed_user in posts:
                timeline = timeline + posts[followed_user]
        return timeline