
def count_tags_for_each_title(titles_and_genres: list) -> tuple:
    result = {}
    total = 0 # to have a record of the total number of tags (will be used later)
    for game_obj in titles_and_genres:
        if game_obj["tags"]:
            for tag in game_obj["tags"]:
                if tag in result:
                    result[tag] += 1
                else:
                    result[tag] = 1
                total += 1
    return result, total

def sort_tags(tags_counts: dict):
    return {k: v for k, v in sorted(tags_counts.items(), key=lambda item: item[1], reverse=True)}

def get_first_n_kvps_from_dict(original_dict: dict, n) -> dict:
    output = {}
    for key, value in original_dict.items():
        output[key] = value
        if len(output) == n:
            break
    return output

def get_percentage_of_tag(user_input: str, tags_counts_dict: dict, total_num_of_tags: int) -> int:
    if total_num_of_tags == 0:
        raise Exception("Error: total number of tags is 0")
    elif user_input in tags_counts_dict:
        return tags_counts_dict[user_input]/total_num_of_tags
    else:
        return 0