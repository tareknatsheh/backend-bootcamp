from bs4 import BeautifulSoup

def scrap_game_titles_and_genres(page_text) -> list[dict]:
    titles_with_genres_list = []
    soup = BeautifulSoup(page_text, "html.parser")
    all_items = soup.find_all("div", class_="tab_item_content")
    
    for game in all_items:
        title_text = game.find('div', class_="tab_item_name").text
        item_tags_list = game.find_all('span', class_="top_tag")
        game_obj = {
            "title": title_text,
            "tags": [tag.text.strip(", ").lower() for tag in item_tags_list]
        }
        titles_with_genres_list.append(game_obj)
    
    return titles_with_genres_list

def mockup_scrap_game_titles_and_genres():
    return [
        {
            "title": "game1",
            "tags": ["action", "strat", "sim"]
        },
        {
            "title": "game2",
            "tags": ["action"]
        },
        {
            "title": "game3",
            "tags": ["kids", "strat"]
        }
    ]