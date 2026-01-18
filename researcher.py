from duckduckgo_search import DDGS

class TrendResearcher:
    def __init__(self):
        self.ddgs = DDGS()

    def find_trends(self, query="digital marketing trends 2024", max_results=5):
        """
        Searches for trends based on the query.
        Returns a list of dictionaries with title, href, and body.
        """
        print(f"Searching for: {query}")
        results = list(self.ddgs.text(query, max_results=max_results))
        return results

if __name__ == "__main__":
    # Test
    researcher = TrendResearcher()
    trends = researcher.find_trends()
    for t in trends:
        print(f"- {t['title']}: {t['href']}")
