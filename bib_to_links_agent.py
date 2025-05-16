# app.py

import streamlit as st
import requests
from transformers import pipeline



# Load the lightweight LLM once
@st.cache_resource
def load_llm():
    return pipeline("text2text-generation", model="google/flan-t5-base")

llm = load_llm()

# Function to extract title using the LLM
def extract_title_llm(citation: str) -> str:
    prompt = f"""You are an expert at parsing academic references.
From the following APA/MLA-like citation, extract only the actual paper title from this citation, without any conference or journal name. Delete the segments like 'In <conf name>' or In 'conference info' from the end of the title.
    uniquement s'ils semblent décrire un contexte de publication.
Return just the title without quotation marks.


Citation: {citation}
Title:
for example:
Giorgio Angelotti, Nicolas Drougard, and Caroline Ponzoni Carvalho Chanel. Offline learning for planning: A summary. In Bridging the Gap Between AI Planning and Reinforcement Learning (PRL), ICAPS 2020 Workshop, pages 153–161, 2020.
becomes:
Offline learning for planning: A summary


"""

    try:
        return llm(prompt, max_new_tokens=50)[0]['generated_text'].strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Function to query Semantic Scholar API
def search_semantic_scholar(title):
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={title}&limit=1&fields=url,title"
    try:
        response = requests.get(url)
        data = response.json()
        if data["total"] > 0:
            paper = data["data"][0]
            return paper["title"], paper["url"]
        else:
            return None, None
    except Exception as e:
        return None, f"❌ API error: {str(e)}"

# --- Streamlit UI ---
st.title("🔗 BibLinker: Find Links from Bibliographic References")
st.markdown("Paste your bibliography references below, and get direct links to the articles!")

input_text = st.text_area("📚 References (one per line)", height=300)

if st.button("🔍 Find Article Links"):
    if not input_text.strip():
        st.warning("Please enter at least one reference.")
    else:
        references = input_text.strip().split('\n')
        with st.spinner("⏳ Extracting titles and searching for articles..."):
            for ref in references:
                if ref.strip():
                    title = extract_title_llm(ref)
                    st.markdown(f"**Extracted title:** _{title}_")

                    found_title, link = search_semantic_scholar(title)
                    if link:
                        st.markdown(f"🔗 [Read the article]({link})")
                    else:
                        st.warning(f"No link found for: _{title}_")