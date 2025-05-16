# 🔗 BibLinker

Manually cleaning references and searching papers wastes time.
BibLinker automates this process with natural language understanding, even when citations are imprecise or poorly formatted.

**BibLinker** is a very simple and efficient app to extract paper titles from messy bibliographic references and find the corresponding article links using the [Semantic Scholar API](https://api.semanticscholar.org/).

Built with [Streamlit](https://streamlit.io/) and powered by a lightweight open-source LLM (`google/flan-t5-base`), BibLinker helps you clean up citations and locate articles in seconds.

## ✨ Features

- 🧠 Extracts clean paper titles from raw APA/MLA-style references using a local LLM.
- 🔍 Finds corresponding papers via Semantic Scholar.
- 💡 Designed for researchers, students, and anyone working with academic references.
- 📦 No login or API key required.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/biblinker.git
cd biblinker
```

### 2. Install the dependencies
I recommend using a virtual environment. Make sure you have miniconda or anaconda installed.
```
conda env create -f environment.yaml
conda activate bibtopdf
```

### 3. Run the app
```
streamlit run bib_to_links_agent.py
```
Then open the app in your browser (usually http://localhost:8501).



### 🖼️ Example 
Paste this citation:

Davinder Singh, Naman Jain, Pranjali Jain, Pratik Kayal, Sudhakar Kumawat, and Nipun Batra. Plantdoc: A dataset for visual plant disease detection. In Proceedings of the 7th ACM IKDD CoDS and 25th COMAD, pages 249–253. 2020.

Get this clean output:

Extracted title: Extracted title: Plantdoc: A dataset for visual plant disease detection.
🔗 [Link to article](https://www.semanticscholar.org/paper/PlantDoc%3A-A-Dataset-for-Visual-Plant-Disease-Singh-Jain/149720bb953c385f950fae3c68ab5a11c0af952d)

You can try with multiple references at once !

### 🧠 Under the Hood

- 🗃️ **Model**: google/flan-t5-base
- 🔍 **Search API**: Semantic Scholar Graph API
- 🖥️ **Interface**: Streamlit
- ⚙️ **Language**: Python 3.10+

### 📁 Project Structure
```
biblinker/
├── bib_to_links_agent.py               # Main Streamlit app
├── environment.yaml     # Conda environment specification
└── README.md            # Project documentation
```



