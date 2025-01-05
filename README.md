# Smart_course_finder_Application
The Smart Course Finder is an AI-driven application designed to help users discover online courses based on their interests. By leveraging machine learning and natural language processing, the tool offers personalized and accurate course recommendations.

The application features a user-friendly interface where users can input their preferences and receive curated suggestions. This project demonstrates how advanced AI technologies can simplify the process of finding relevant educational content, making learning more accessible and personalized.

![img alt](https://github.com/Tridibesh-033/Smart_course_finder_Application/blob/main/ws.jpeg?raw=true)

## Proposed Methodology
1. Data Collection: Scraped course details (title, description, and link) from Analytics Vidhya using BeautifulSoup and saved to a CSV file.
2. Embedding Creation: Converted course descriptions to numerical embeddings using the SentenceTransformer model (all-MiniLM-L6-v2).
3. Index Building: Built a FAISS index for efficient similarity searches and saved it along with updated course data.
4. Streamlit App Development: Designed a user-friendly interface to take user queries and display search results (title, description, link).
5. Search Functionality: Implemented a feature to match user queries with top courses using embeddings and the FAISS index.

![img alt](https://raw.githubusercontent.com/Tridibesh-033/Smart_course_finder_Application/refs/heads/main/ws_cycle.webp)

## User Application

![img alt](https://github.com/Tridibesh-033/Smart_course_finder_Application/blob/main/stm.png?raw=true)

## Streamlit in HuggingFace

![img alt]()
