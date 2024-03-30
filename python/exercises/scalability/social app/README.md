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
in class **SocialMediaPlatform**: method **register_user**

1. Registering 50,000 new users:
- Before: 41 seconds
- After: 0.042 seconds

2. Finding a user in a 50,000 users pool:
- Before: 0.003 seconds
- After:
