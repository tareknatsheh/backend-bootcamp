from social_media import SocialMediaPlatform
import time

def main():

    start = time.perf_counter()

    my_plat = SocialMediaPlatform()

    users_list = []
    for i in range(50000):
        users_list.append(my_plat.register_user(f"user{i}"))

    end = time.perf_counter()

    print(f"It took {end-start} seconds")

    pass

if __name__ == "__main__":
    main()