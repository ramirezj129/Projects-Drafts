import re

twttr_url = input("Enter Twitter URL: ").strip()


if matches := re.search(
    r"(^https?://)?(?:www\.)?twitter\.com/(.+)$", twttr_url, re.IGNORECASE
):
    print(f"Username: ", matches.group(1))
