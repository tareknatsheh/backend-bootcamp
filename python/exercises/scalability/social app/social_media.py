from user import User, posts

class SocialMediaPlatform:
    def __init__(self) -> None:
        """Constructor
        the platform is initialized with an empty list of users
        """
        self.users: list = []

    def register_user(self, username: str) -> None:
        """Registering a user addes them to the users list

        Args:
            username (str): unique username of the user
        """
        if not self._is_username_taken(username):
            user = User(username)
            self.users.append(user)

    def _is_username_taken(self, username: str) -> bool:
        """An internal method that checks the existance of a specific user

        Args:
            username (str): of the user to be checked if it exists

        Returns:
            bool: True if exists False otherwise
        """
        for user in self.users:
            if user.username == username:
                return True
        return False

    def get_user_by_username(self, username: str) -> User | None:
        """returns the User object of a specific user if found

        Args:
            username (str): of the target user to be found

        Returns:
            User | None: The target User object, or None if it does not exist
        """
        for user in self.users:
            if user.username == username:
                return user
        return None

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
            for post in posts:
                if post['username'] == followed_user.username:
                    timeline.append(post)
        return timeline