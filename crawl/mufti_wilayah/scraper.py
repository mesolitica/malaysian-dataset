from xtractor.utils import (
    extractor,
    read_the_json,
    dumps_the_json,
    request_page,
    multi_threading,
)

import json

BASE_URL = "https://www.muftiwp.gov.my"


def fetch_href(link: str):
    soup = extractor(link)

    a_tag = soup.find_all("a", href=True)

    buffer_main_links = []
    for aTag in a_tag:
        if "artikel" in aTag["href"]:
            link = BASE_URL + aTag["href"]
            buffer_main_links.append(link)

    links = sorted(list(set(buffer_main_links)))
    return links


def fetch_links_article(idx, link: list):
    article_links = {}

    # for link in links:
    soup = extractor(link)
    a_tag = soup.find_all("a", href=True)
    article_links[link]: list = []

    for aTag in a_tag:
        article_link = BASE_URL + aTag["href"]

        if "artikel" in article_link:
            if article_link not in article_links[link]:
                article_links[link].append(article_link)

    full_set_links = []
    keys = list(article_links.keys())
    for key in keys:
        link_list = article_links[key]
        for item in link_list:
            soup = extractor(item)
            a_tag = soup.find_all("a", href=True)
            for aTag in a_tag:
                article_link = BASE_URL + aTag["href"]
                full_set_links.append(article_link)

    full_set_links = list(set(full_set_links))
    return full_set_links


def extract_article(idx, link):
    try:
        soup = extractor(link)
        div_tag = soup.find("div", class_="body-wrapper")
        div_tag = div_tag.find("div", class_="body-innerwrapper")
        section = div_tag.find("section", {"id": "sp-main-body"})
        div_tag = section.find("div", class_="row")
        div_tag = div_tag.find(
            "div", class_="article-details-wrapper gazette-custom-font"
        )
        text = div_tag.text.replace("\n", " ").strip()
        return text
    except:
        pass


def main_fetch_link():
    link = "https://www.muftiwp.gov.my/"
    print("#" * 10, "START 1", "#" * 10)
    href_links = fetch_href(link)
    print(href_links)
    print("#" * 10, "FINISH 1", "#" * 10)
    print("#" * 10, "START 2", "#" * 10)
    article_links = multi_threading(
        todo=fetch_links_article, links=href_links, worker_num=10
    )
    article_links_dict = {"article_links": [x for x in article_links]}
    print("#" * 10, "FINISH 2", "#" * 10)
    print(article_links)
    print(len(article_links))
    dumps_the_json(
        article_links_dict, json_file_name="./mufti_wilayah/pages_links.json"
    )


# ----------------------------- MAIN -------------------------------
if __name__ == "__main__":
    pages_links = read_the_json("./mufti_wilayah/pages_links.json")
    # print(len(pages_links["article_links"]))

    # GET ARTICLE
    all_links = []
    for list_link in pages_links["article_links"]:
        for link in list_link:
            all_links.append(link)
    all_links = list(set(all_links))

    articles = multi_threading(todo=extract_article, links=all_links, worker_num=10)

    index = [x for x in range(len(articles))]
    all_articles = {"url": index, "artikel": articles}

    with open("./mufti_wilayah/mufti_wilayah_articles.json", "w") as file:
        json.dump(all_articles, file, ensure_ascii=False)

    print("COMPLETE")
