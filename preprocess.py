import requests
from bs4 import BeautifulSoup
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss


def scrape_courses():
    base_url = "https://courses.analyticsvidhya.com/collections/courses"
    courses = []

    
    for page in range(1, 101):  
        print(f"Scraping page {page}...")
        response = requests.get(f"{base_url}?page={page}")
        
        if response.status_code != 200:
            print(f"Failed to fetch page {page}, status code: {response.status_code}")
            continue
        
        soup = BeautifulSoup(response.text, "html.parser")

        for course in soup.find_all("li", class_="products__list-item"):
            title = course.find("h3").text.strip()
            relative_link = course.find("a")['href']
            course_url = f"https://courses.analyticsvidhya.com{relative_link}" if not relative_link.startswith("http") else relative_link

            course_page = requests.get(course_url)
            course_soup = BeautifulSoup(course_page.text, "html.parser")
            description_tag = course_soup.find("section", class_="section__body")
            description = description_tag.text.strip() if description_tag else "No description available"
            description = ' '.join(description.split())  # Clean description

            courses.append({"Title": title, "Description": description, "Link": course_url})

    df = pd.DataFrame(courses)
    df.to_csv("courses.csv", index=False)
    print("Courses data saved to courses.csv.")
    return df

# Step 2: Generate embeddings and build FAISS index
def build_faiss_index(df):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("Generating embeddings...")
    embeddings = model.encode(df['Description'].tolist())

    print("Building FAISS index...")
    embedding_dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(embedding_dim)
    index.add(embeddings)

    faiss.write_index(index, "course_index.faiss")
    df.to_csv("courses_with_embeddings.csv", index=False)
    print("FAISS index and embeddings saved successfully.")

# Run the preprocessing steps
if __name__ == "__main__":
    df = scrape_courses()
    build_faiss_index(df)
