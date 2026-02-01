import requests
import xml.etree.ElementTree as ET

def search_arxiv(query, max_results=5):
    """
    Search arXiv for papers matching the query.
    """
    base_url = 'http://export.arxiv.org/api/query?'
    params = {
        'search_query': f'all:{query}',
        'start': 0,
        'max_results': max_results
    }
    
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        return f"Error: {response.status_code}"

    # Parse the Atom feed
    root = ET.fromstring(response.content)
    
    # Namespaces
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    
    results = []
    for entry in root.findall('atom:entry', ns):
        title = entry.find('atom:title', ns).text.strip()
        summary = entry.find('atom:summary', ns).text.strip()
        link = entry.find('atom:id', ns).text
        published = entry.find('atom:published', ns).text
        
        results.append({
            'title': title,
            'summary': summary,
            'link': link,
            'published': published
        })
        
    return results

if __name__ == "__main__":
    import sys
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "LLM Agents"
    papers = search_arxiv(query)
    
    if isinstance(papers, str):
        print(papers)
        sys.exit(1)
        
    if not papers:
        print(f"\nNo results found for: {query}")
        sys.exit(0)
    
    print(f"\n--- Search results for: {query} ---\n")
    for i, paper in enumerate(papers, 1):
        print(f"{i}. {paper['title']}")
        print(f"   Published: {paper['published']}")
        print(f"   Link: {paper['link']}")
        print(f"   Summary: {paper['summary'][:200]}...\n")
