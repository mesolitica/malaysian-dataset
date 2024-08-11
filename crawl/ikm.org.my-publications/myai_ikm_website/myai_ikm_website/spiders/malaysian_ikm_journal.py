import scrapy
import html

class MalaysianJournalSpider(scrapy.Spider):
    name = 'malaysian_ikm_journal'
    start_urls = ['https://ikm.org.my/publications/malaysian-journal-of-chemistry/archives.php']

    def parse(self, response):
        # Extract Article Details Links
        article_links = response.xpath("//div[@class='col-md-9']/ul[@class='journal-listing']/li/strong/a/@href").getall()
        article_links = [response.urljoin(link) for link in article_links]

        for link in article_links:
            yield scrapy.Request(url=link, callback=self.parse_article)

        # Handle pagination
        next_page = response.xpath("//div[@class='paging']/a[contains(text(), 'Next')]/@href").get()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_article(self, response):
        # Extract Research Titles and their Detail Links
        research_titles = response.xpath("//div[@class='col-xs-10']/a[not(@class='btn btn-primary')]/text()").getall()
        research_links = response.xpath("//div[@class='col-xs-10']/a[not(@class='btn btn-primary')]/@href").getall()
        research_links = [response.urljoin(link) for link in research_links]

        for title, link in zip(research_titles, research_links):
            yield scrapy.Request(url=link, callback=self.parse_research, meta={
                'Article_Details_Link': response.url,
                'Research_Title': title,
                'Research_Title_Details_Link': link
            })

    def parse_research(self, response):
        # Extract Main Title
        main_title = response.xpath("//div[@class='col-md-9']/h3/strong/text()").get()
        main_title = self.clean_data(main_title)

        # Extract Author and Affiliation Information using XPath
        names = response.xpath("//div[@class='author-info']/text()").getall()
        affiliations = response.xpath("//div[@class='author-info']/h5/text()").getall()
        authors_and_affiliations = [self.clean_data(f"{name} - {affiliation}") for name, affiliation in zip(names, affiliations)]
        
        # Extract DOI
        doi = response.xpath("//div[@class='main-info-container']/p/a/@href").get()
        
        # Extract Keywords
        keywords = response.xpath("(//div[@class='main-info-container']/p)[2]/text()").get()
        keywords = self.clean_data(keywords)

        # Extract Abstract
        abstract = response.xpath("(//div[@class='main-info-container']/p)[4]/text()").get()
        abstract = self.clean_data(abstract)

        # Extract Published
        published_dt = response.xpath("(//div[@class='side-info']/p/text())[1]").get()
        published_dt = self.clean_data(published_dt)

        # Extract Issue
        issue = response.xpath("//div[@class='side-info']/p/a/text()").get()
        
        # Extract Issue Link
        issue_link = response.xpath("//div[@class='side-info']/p/a/@href").get()
        if issue_link:
            issue_link = response.urljoin(issue_link)

        # Extract PDF Link
        pdf_link = response.xpath("//div[@class='side-info']/a[@class='btn btn-primary']/@href").get()
        if pdf_link:
            pdf_link = response.urljoin(pdf_link)

        yield {
            'Article_Details_Link': response.meta['Article_Details_Link'],
            'Research_Title': response.meta['Research_Title'],
            'Research_Title_Details_Link': response.meta['Research_Title_Details_Link'],
            'Main_Title': main_title,
            'Authors_and_Affiliations': authors_and_affiliations,
            'Digital_Object_Identifier': doi,
            'Keywords': keywords,
            'Abstract': abstract,
            'Published': published_dt,
            'Issue': issue,
            'Issue_Link': issue_link,
            'Research_PDF_Link': pdf_link
        }

    def clean_data(self, data):
        if data:
            # Decode HTML entities and remove delimiters
            data = html.unescape(data).replace('\n', ' ').replace('\r', '').strip()
        return data

# To run this spider, save the code in a file named `malaysian_journal_spider.py` and run the following command:
# scrapy runspider malaysian_journal_spider.py -o research_articles.json
