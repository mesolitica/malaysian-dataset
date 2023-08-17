# TLDR

* website: [theedgemalaysia](https://theedgemalaysia.com/)
* num. of webpages scraped: 432,374 (inclusive of articles with no text)
* link to dataset: https://huggingface.co/datasets/wanadzhar913/crawl-theedgemalaysia
* last date of scraping: 14th August 2023
* status: **complete**

# Note

The **"language" column for the data set has errors** as it miscategorizes articles in the Mandarin language. This is primarily because I was searching for the string "English version" in the text. This will need to be accounted for if type of language used is important. 

# Methodology

For [The Edge Malaysia](https://theedgemalaysia.com/), each of their articles seem to have a unique ID at the end of the url e.g., "677590" in "https://theedgemalaysia.com/node/677590". Hence, since we won't be able to do this by month, page no., etc., we'll use a **brute force** approach that tests every combination of numbers, such that we'll only scrape from a valid url.

# Progress

- [x] batch1
- [x] batch2
- [x] batch3
- [x] batch4
- [x] batch5
- [x] batch6
- [x] batch7
- [x] batch8
- [x] batch9
- [x] batch10
- [x] batch11
- [x] batch12
- [x] batch13
- [x] batch14