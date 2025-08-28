import requests

def get_post_selftext(url: str) -> str:
    """
    Given a Reddit post URL, return the raw Markdown selftext.
    """
    # Ensure .json is appended
    if not url.endswith('.json'):
        if url.endswith('/'):
            url += '.json'
        else:
            url += '/.json'

    headers = {"User-Agent": "Mozilla/5.0 (selftext-fetcher)"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()

    data = resp.json()
    
    # selftext is in the first item, second element of the listing
    try:
        selftext = data[0]['data']['children'][0]['data']['selftext']
    except (KeyError, IndexError) as e:
        selftext = ""
    
    return selftext


if __name__ == "__main__":
    test_url = "https://old.reddit.com/r/btd6/comments/1n163k9/bloons_td_6_v500_update_notes/"
    text = get_post_selftext(test_url)
    print("Raw Markdown selftext:\n")
    print(text)
