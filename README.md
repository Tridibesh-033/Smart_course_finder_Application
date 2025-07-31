## 🎯 Smart Course Finder
A powerful course recommendation tool that scrapes online course data, encodes content using NLP, builds a semantic search index, and lets users search relevant courses via an interactive Streamlit app.

![img alt](https://github.com/Tridibesh-033/Smart_course_finder_Application/blob/main/ws.jpeg?raw=true)

## 📌 Overview
The Smart Course Finder helps users discover the most relevant courses from Analytics Vidhya's platform based on their interests (e.g., Data Science, Machine Learning, etc.).
It leverages web scraping, semantic embeddings with Sentence Transformers, FAISS for efficient similarity search, and Streamlit for a clean UI.

## 🚀 Features
🔍 Semantic Search: Understands meaning beyond keywords using all-MiniLM-L6-v2.
🧠 Embeddings + FAISS Index: Enables lightning-fast similarity search.
🕸️ Web Scraper: Extracts 100 pages of course titles and descriptions.
📦 Streamlit App: User-friendly interface to search and display top course matches.
🧾 Export: Courses and embeddings saved in CSV for reuse.

## 🛠️ Tech Stack
### Purpose	Tool / Library
- Web Scraping--requests, BeautifulSoup
- Data Handling--pandas
- NLP Embeddings--sentence-transformers (MiniLM)
- Similarity Index--FAISS
- UI--Streamlit

## Proposed Methodology
1. Data Collection: Scraped course details (title, description, and link) from Analytics Vidhya using BeautifulSoup and saved to a CSV file.
2. Embedding Creation: Converted course descriptions to numerical embeddings using the SentenceTransformer model (all-MiniLM-L6-v2).
3. Index Building: Built a FAISS index for efficient similarity searches and saved it along with updated course data.
4. Streamlit App Development: Designed a user-friendly interface to take user queries and display search results (title, description, link).
5. Search Functionality: Implemented a feature to match user queries with top courses using embeddings and the FAISS index.

📂 Project Structure

<img width="406" height="141" alt="{6E484D34-00FD-4D66-BADC-90625F3DD798}" src="https://github.com/user-attachments/assets/e6c530ce-7999-444f-b54f-8a8dabffe233" />

## 🧪 How It Works
### Step 1: Scraping and Indexing
*python preprocess.py*
- Scrapes course data (titles, descriptions, URLs)
- Generates sentence embeddings
- Builds a FAISS index and stores embeddings

### Step 2: Run the App
*streamlit run main.py*
### Type in your interest
![img alt](https://github.com/Tridibesh-033/Smart_course_finder_Application/blob/main/stm.png?raw=true)
### Get the top 5 semantically relevant courses
![img alt](https://github.com/Tridibesh-033/Smart_course_finder_Application/blob/main/stm1.png?raw=true)

## Streamlit in HuggingFace
Public link: https://huggingface.co/spaces/tridibesh033/course_finder

## 📥 Requirements
pip install -r requirements.txt

- requests
- beautifulsoup4
- pandas
- sentence-transformers
- faiss-cpu
- streamlit
- huggingface_hub

## 📬 Contact
- Tridibesh Debnath
- 📧 tridibeshdebnath@gmail.com
- Linkedin: https://www.linkedin.com/in/tridibesh-debnath-46b37924a/
