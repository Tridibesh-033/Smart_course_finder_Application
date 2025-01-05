
import pandas as pd
import faiss
import streamlit as st
from huggingface_hub import HfApi
from sentence_transformers import SentenceTransformer

# Load precomputed files
@st.cache_data
def load_data():
    return pd.read_csv("courses_with_embeddings.csv")

@st.cache_resource
def load_faiss_index():
    return faiss.read_index("course_index.faiss")

@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

# Search function
def search_courses(query, index, df, model):
    query_embedding = model.encode([query])
    _, top_indices = index.search(query_embedding, k=5)
    results = df.iloc[top_indices[0]].to_dict(orient="records")
    return results

# Load CSS
def load_css(file_path):
    with open(file_path, "r") as f:
        return f"<style>{f.read()}</style>"

css_styles = load_css("style.css")
st.markdown(css_styles, unsafe_allow_html=True)

# Streamlit User Interface
def main():
    st.title("Smart Course Finder")
    st.write("Search for courses on the Analytics Vidhya platform")

    
    df = load_data()
    index = load_faiss_index()
    model = load_model()

   
    query = st.text_input("Enter your Interest (e.g., Machine Learning, Data Science, Deep Learning):")
    
    
    if st.button("Search"):
        if query.strip():  
            
            results = search_courses(query, index, df, model)

            
            if results:
                st.subheader("Top 5 Relevant Courses")
                for res in results:
                    st.markdown(f"**Title:** {res['Title']}")  
                    st.markdown(f"**Description:** {res['Description']}")  
                    st.markdown(f"[**Link:**]({res['Link']})")  
                    st.markdown("---")
            else:
                st.write("No courses found for the given query.")
        else:
            st.write("Please enter a valid query before searching.")

if __name__ == "__main__":
    main()
