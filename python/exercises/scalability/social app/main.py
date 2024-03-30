from social_media import SocialMediaPlatform

def main():

    my_plat = SocialMediaPlatform()

    my_plat.register_user("tarek")
    my_plat.register_user("ahmad")

    target_user = my_plat.get_user_by_username("tarek")

    if target_user:
        print(target_user.username)
        print(target_user.following)

    pass

if __name__ == "__main__":
    main()