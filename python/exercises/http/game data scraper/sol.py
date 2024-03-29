# Game data scraping
import http_client as hc, scrapper as sc, plotter as p, data_analysis as d

def get_user_input() -> str:
    return input("What tag would you like to see the percentage of it: ")


def main():
    url = "https://store.steampowered.com/"
    page_text = hc.get_page_as_text(url)
    titles_and_genres = sc.scrap_game_titles_and_genres(page_text)

    # For testing, uncomment this: and comment the scrap_game_titles_and_genres() one
    # titles_and_genres = sc.mockup_scrap_game_titles_and_genres()

    tags_counts_dict, total_num_of_tags = d.count_tags_for_each_title(titles_and_genres)
    sorted_tags = d.sort_tags(tags_counts_dict)
    # Let's get the top 10 most appeared tags:
    top_10_tags = d.get_first_n_kvps_from_dict(sorted_tags, 10)

    p.plot_tags(top_10_tags)

    user_input = get_user_input()
    user_input_percentage = d.get_percentage_of_tag(user_input.lower(), tags_counts_dict, total_num_of_tags)
    print(f"The tag: {user_input} represents {user_input_percentage:.1%} of the whole seen tags")

    p.plot_stats_of_a_tag(user_input.lower(), top_10_tags)

if __name__ == "__main__":
    main()