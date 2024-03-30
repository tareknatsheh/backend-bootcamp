from social_media import SocialMediaPlatform
import time

def main():

    # 1. Registering a lot of users:
    start = time.perf_counter()

    my_plat = SocialMediaPlatform()

    users_list = []
    TOAL_NUM_NEW_USERS = 50000
    for i in range(TOAL_NUM_NEW_USERS):
        users_list.append(my_plat.register_user(f"user{i}"))

    end = time.perf_counter()

    print(f"It took {end-start} seconds to register {TOAL_NUM_NEW_USERS} new users")

    # 2. finding one user in a very big list of users
    start = time.perf_counter()

    user50000 = my_plat.get_user_by_username("user50000")
    if user50000:
        print(user50000.username)

    end = time.perf_counter()

    print(f"It took {end-start} seconds to find user50000")

    # 3. generating timeline
    # let's generate some 1000 random posts for a 1000 users:
    user2000 = my_plat.get_user_by_username("user2000")
    if user2000:
        for i in range(500):
            user = my_plat.get_user_by_username(f"user{i}")
            if user:
                user2000.follow(f"user{i}")
                for _ in range(500):
                    if user: user.post_message("xxxxxxxxxxxxxxxxxxxxxxxx")

    start = time.perf_counter()
    user2000_timeline = my_plat.generate_timeline("user2000")
    end = time.perf_counter()
    print(f"It took {end-start} seconds to generate user2000 timeline")

    print(len(user2000_timeline))
 
    pass

if __name__ == "__main__":
    main()