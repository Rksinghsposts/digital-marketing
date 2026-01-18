import streamlit as st
import os
from researcher import TrendResearcher
from writer import ContentWriter
from dotenv import load_dotenv

# Load env variables
load_dotenv()

def main():
    st.set_page_config(page_title="Digital Marketing AI Agent", page_icon="🚀", layout="wide")
    
    st.title("🚀 Digital Marketing AI Agent")
    st.markdown("Find trending topics and generate high-quality blog posts instantly.")
    
    # Sidebar for configuration
    st.sidebar.header("Configuration")
    
    api_key = os.getenv("OPENAI_API_KEY")
    user_api_key = st.sidebar.text_input("OpenAI API Key", value=api_key if api_key else "", type="password")
    
    if user_api_key:
        os.environ["OPENAI_API_KEY"] = user_api_key
    
    niche = st.sidebar.text_input("Niche / Topic", value="Digital Marketing Trends 2024")
    
    if "trends" not in st.session_state:
        st.session_state.trends = []
    
    # Step 1: Research
    st.header("1. Find Trends")
    if st.button("Search for Trends"):
        with st.spinner("Searching for latest trends..."):
            researcher = TrendResearcher()
            try:
                results = researcher.find_trends(query=niche, max_results=5)
                st.session_state.trends = results
                st.success(f"Found {len(results)} trends!")
            except Exception as e:
                st.error(f"Error during research: {e}")
    
    # Display Results
    if st.session_state.trends:
        st.subheader("Select a Topic to Write About")
        for i, trend in enumerate(st.session_state.trends):
            with st.expander(f"{i+1}. {trend['title']}"):
                st.write(f"**Snippet:** {trend['body']}")
                st.write(f"**Source:** {trend['href']}")
                if st.button(f"Generate Blog for #{i+1}", key=f"btn_{i}"):
                    st.session_state.selected_trend = trend
                    st.rerun()

    # Step 2: Write
    if "selected_trend" in st.session_state:
        st.divider()
        st.header("2. Content Generation")
        trend = st.session_state.selected_trend
        
        st.info(f"Generating content for: **{trend['title']}**")
        
        if not user_api_key:
            st.warning("Please enter your OpenAI API Key in the sidebar to generate content.")
        else:
            with st.spinner("Writing blog post... (This may take a minute)"):
                try:
                    writer = ContentWriter()
                    blog_post = writer.write_blog_post(trend, f"{trend['title']} - {trend['body']}")
                    st.markdown(blog_post)
                    st.download_button("Download Markdown", blog_post, file_name="blog_post.md")
                except Exception as e:
                    st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
