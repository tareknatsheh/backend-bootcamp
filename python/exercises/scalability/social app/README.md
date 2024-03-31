# Social media platform

The platform allow users to post messages, follow other users, and view a timeline of posts from users they follow. However, the initial implementation of the platform is inefficient, causing performance issues as the user base grows.

## *Features*
1. User Registration: Allow users to register with a unique username.
2. Posting Messages: Allow registered users to post messages.
3. Following Users: Allow users to follow other users.
4. Timeline: Provide each user with a timeline of posts from users they follow.

## Quick start
```bash
python main.py
```

## Performance improvement changes
in classes **SocialMediaPlatform** and **User** methods and data structures were changed to
get a better performance

1. Registering 50,000 new users:
- Before: 41 seconds

    O(n) because it needed to loop over all of the existing users to make sure that the username is unique

- After: 0.042 seconds

    O(1) after using a hashtable


2. Finding a user in a 50,000 users pool:
- Before: 0.003 seconds

    O(n)

- After: 0.0000025 seconds

    O(1)

3. Generating a timeline for a user that is following 500 users, where each user has 500 posts
- Before: 5.2 seconds

    O(n^2)

- After: 1.02 seconds

    O(n)

It was done by making self.users a dict with the unique usernames as the keys instead of a list of dicts.
this way you don't need to loop over all of the list items until you find the target user.

Also, the same approuch was done for the posts list.
It was converted from a list of objects/posts to a dictionary with the unique usernames as the keys
