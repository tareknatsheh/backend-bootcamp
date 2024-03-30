from social_media import SocialMediaPlatform

def main():

    my_plat = SocialMediaPlatform()

    my_plat.register_user("tarek")
    my_plat.register_user("ahmad")

    tarek = my_plat.get_user_by_username("tarek")
    ahmad = my_plat.get_user_by_username("ahmad")


    if tarek and ahmad:
        tarek.post_message("Hello from the other side")
        tarek.post_message("what is this place!?")
        ahmad.follow(tarek)
        ahmad_tl = my_plat.generate_timeline("ahmad")
        print(ahmad_tl)

    pass

if __name__ == "__main__":
    main()