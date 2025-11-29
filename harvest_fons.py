"""FoNS Article Harvester
Downloads nursing resources and articles from Foundation of Nursing Studies.
"""
import os
import requests
import time
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Configuration
OUTPUT_DIR = "fons_knowledge_base"
BASE_URL = "https://www.fons.org"
DELAY_SECONDS = 2  # Be respectful to the server

# FoNS resource pages to harvest
RESOURCE_PAGES = [
    "/resources",
    "/resources/person-centred-practice",
    "/resources/practice-development",
    "/resources/workplace-culture",
    "/resources/facilitation",
    "/resources/transformation",
]

def create_output_dir():
    """Create the output directory if it doesn't exist."""
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}")

def fetch_page(url: str) -> BeautifulSoup | None:
    """Fetch a page and return a BeautifulSoup object."""
    try:
        headers = {
            "User-Agent": "NursingKnowledgeBot/1.0 (Educational Purpose)"
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except Exception as e:
        print(f"  Error fetching {url}: {e}")
        return None

def extract_text_content(soup: BeautifulSoup) -> str:
    """Extract main text content from a page."""
    # Remove script and style elements
    for element in soup(["script", "style", "nav", "footer", "header"]):
        element.decompose()
    
    # Get text
    text = soup.get_text(separator="\n", strip=True)
    
    # Clean up whitespace
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)

def save_content(filename: str, content: str, source_url: str):
    """Save content to a file with source metadata."""
    filepath = Path(OUTPUT_DIR) / filename
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# Source: {source_url}\n")
        f.write(f"# Downloaded: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(content)
    print(f"  Saved: {filename}")

def harvest_resource_page(page_path: str):
    """Harvest a single resource page."""
    url = urljoin(BASE_URL, page_path)
    print(f"\nHarvesting: {url}")
    
    soup = fetch_page(url)
    if not soup:
        return
    
    # Extract main content
    content = extract_text_content(soup)
    if content:
        # Create filename from path
        filename = page_path.strip("/").replace("/", "_") or "home"
        filename = f"{filename}.txt"
        save_content(filename, content, url)
    
    # Find links to articles/resources on this page
    links = soup.find_all("a", href=True)
    article_links = []
    
    for link in links:
        href = link.get("href", "")
        # Look for article/resource links
        if "/resources/" in href and href != page_path:
            full_url = urljoin(BASE_URL, href)
            if full_url.startswith(BASE_URL) and full_url not in article_links:
                article_links.append(full_url)
    
    # Harvest linked articles
    for article_url in article_links[:10]:  # Limit to 10 per page
        time.sleep(DELAY_SECONDS)  # Be respectful
        print(f"  Fetching article: {article_url}")
        
        article_soup = fetch_page(article_url)
        if article_soup:
            article_content = extract_text_content(article_soup)
            if article_content and len(article_content) > 200:
                # Create filename from URL
                parsed = urlparse(article_url)
                article_filename = parsed.path.strip("/").replace("/", "_") + ".txt"
                save_content(article_filename, article_content, article_url)

def download_pdf_resources():
    """Download PDF resources if available."""
    print("\nSearching for PDF resources...")
    
    for page_path in RESOURCE_PAGES:
        url = urljoin(BASE_URL, page_path)
        soup = fetch_page(url)
        if not soup:
            continue
        
        # Find PDF links
        for link in soup.find_all("a", href=True):
            href = link.get("href", "")
            if href.lower().endswith(".pdf"):
                pdf_url = urljoin(BASE_URL, href)
                pdf_name = Path(urlparse(pdf_url).path).name
                pdf_path = Path(OUTPUT_DIR) / pdf_name
                
                if not pdf_path.exists():
                    try:
                        print(f"  Downloading: {pdf_name}")
                        response = requests.get(pdf_url, timeout=60)
                        response.raise_for_status()
                        with open(pdf_path, "wb") as f:
                            f.write(response.content)
                        time.sleep(DELAY_SECONDS)
                    except Exception as e:
                        print(f"  Error downloading {pdf_name}: {e}")

def create_sample_content():
    """Create sample nursing knowledge content for testing."""
    print("\nCreating sample nursing content...")
    
    sample_content = {
        "person_centred_care.txt": """# Person-Centred Care in Nursing

Person-centred care is an approach that places the person at the centre of all care decisions.

Key principles include:
1. Treating people with dignity and respect
2. Offering coordinated care, support, or treatment
3. Offering personalised care, support, or treatment
4. Being enabling - supporting people to recognise and develop their strengths

Person-centred care recognises that patients are individuals with unique needs, 
preferences, and values that must guide all clinical decisions.
""",
        "practice_development.txt": """# Practice Development in Nursing

Practice development is a continuous process of improvement in patient care quality.

Core principles:
- Enabling practitioners to transform care through reflection
- Creating cultures that support sustainable change
- Using evidence to improve practice
- Collaborative working with patients and families
- Developing shared values and beliefs

Practice development requires commitment to ongoing learning and improvement.
""",
        "reflective_practice.txt": """# Reflective Practice for Nurses

Reflective practice is essential for professional development in nursing.

Benefits of reflection:
- Deeper understanding of clinical experiences
- Improved decision-making
- Enhanced self-awareness
- Better patient outcomes

Reflective models commonly used:
- Gibbs' Reflective Cycle
- Johns' Model of Structured Reflection  
- Driscoll's What? Model

Regular reflection helps nurses grow professionally and deliver better care.
"""
    }
    
    for filename, content in sample_content.items():
        filepath = Path(OUTPUT_DIR) / filename
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  Created: {filename}")

def main():
    print("="*60)
    print("FoNS Knowledge Base Harvester")
    print("="*60)
    
    create_output_dir()
    
    # Create sample content for testing
    create_sample_content()
    
    # Try to harvest from FoNS website
    print("\nAttempting to harvest FoNS resources...")
    print("(This may take several minutes)")
    
    for page_path in RESOURCE_PAGES:
        try:
            harvest_resource_page(page_path)
            time.sleep(DELAY_SECONDS)
        except Exception as e:
            print(f"Error harvesting {page_path}: {e}")
    
    # Try to download PDFs
    try:
        download_pdf_resources()
    except Exception as e:
        print(f"Error downloading PDFs: {e}")
    
    # Count files
    files = list(Path(OUTPUT_DIR).glob("*"))
    print(f"\n" + "="*60)
    print(f"Harvest complete! {len(files)} files in {OUTPUT_DIR}")
    print("="*60)
    print("\nNext step: Run 'python ingest_fast.py' to build the knowledge base")

if __name__ == "__main__":
    main()
