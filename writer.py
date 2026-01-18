import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class ContentWriter:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables.")
        self.client = OpenAI(api_key=api_key)

    def write_blog_post(self, topic, research_summary):
        """
        Generates a blog post based on the topic and research summary.
        """
        prompt = f"""
        You are an expert digital marketing content writer.
        
        Topic: {topic['title']}
        Source Context: {topic['body']}
        Link: {topic['href']}
        
        Task: Write a comprehensive, engaging, and SEO-optimized blog post about the above topic.
        The blog post should include:
        - A catchy title
        - An engaging introduction
        - Key takeaways (bullet points)
        - In-depth sections with headers
        - A conclusion
        
        Format the output in Markdown.
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo", # Or gpt-4 if available/preferred
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that writes high-quality marketing content."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating content: {e}"

if __name__ == "__main__":
    # Test placeholder (requires key)
    pass
