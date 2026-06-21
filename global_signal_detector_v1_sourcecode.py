import streamlit as st
from ollama import chat
from datetime import datetime
st.set_page_config(
    page_title="Global Signal Detector",
    page_icon="🌍",
    layout="wide"
)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #020617,
        #0f172a,
        #134e4a
    );
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Sidebar */

[data-testid="stSidebar"] {
    background-color: #0b1220;
}

</style>
""", unsafe_allow_html=True)

if "recent_articles" not in st.session_state:
    st.session_state.recent_articles = []
# -----------------------------
# Main Analysis Agent
# -----------------------------
def news_agent(article):

    response = chat(
        model="gemma4:e4b",
        messages=[
            {
                "role": "user",
                "content": f"""
You are a Global Signal Detection AI.

Analyze the following text and keep every section under 5 sentences.

Provide:

1. SUMMARY:

2. CATEGORY:
(Technology, Health, Climate, Economy, Politics, Education, Society, Other)

3. IMPACT SCOPE:
(Local, National, Global)

4. SEVERITY SCORE:
(1-10)

5. STAKEHOLDERS AFFECTED:

6. KEY INSIGHT:

7. POTENTIAL RISKS:

8. RECOMMENDED ACTIONS:

TEXT:
{article}
"""
            }
        ]
    )

    return response["message"]["content"]


# -----------------------------
# UI
# -----------------------------

if "history" not in st.session_state:
    st.session_state.history = []
    
st.markdown("""
<h1 style='text-align:center;'>
🌍 Global Signal Detector
</h1>
""", unsafe_allow_html=True)

st.markdown(
    "<h4 style='text-align:center;'>Detect • Analyze • Understand</h4>",
    unsafe_allow_html=True
)

with st.sidebar:

    st.header("⚙️ System Status")

    st.success("Online")

    st.write("Model: gemma 4:e4 b")

    st.write("Version: 1.1")

    st.markdown("---")

    st.header("📈 Statistics")

    st.metric(
        "Analyses",
        len(st.session_state.recent_articles)
    )

    st.markdown("---")

    if st.button("➕ New Analysis"):
        st.session_state.article_box = ""
        st.session_state.current_result = ""
        
        st.rerun()

    st.sidebar.subheader("📋 Recent Analyses")

    for i, item in enumerate(st.session_state.history[:5]):

        if st.sidebar.button(
            f"[{item['time']}] {item['article'][:25]}...",
            key=f"history_{i}"
        ):
            st.session_state.article_box = item["article"]
            st.session_state.current_result = item["result"]
            st.rerun()
st.info(
    "Paste any article, news report, observation, or trend and receive AI-generated insights."
)

article = st.text_area(
    "Enter article or text",
    key="article_box",
    height=250,
    placeholder="Paste article here..."
)

# Sidebar history
    
if st.button("Analyze"):

    if article.strip() == "":
        st.warning("Please enter some text first.")
    else:

        with st.spinner("Analyzing..."):
            timestamp = datetime.now().strftime("%H:%M")
            st.session_state.recent_articles.insert(
                0,
                f"[{timestamp}] {article[:25]}..."
                )
            st.session_state.recent_articles = (
                st.session_state.recent_articles[:10]
                )

            result = news_agent(article)
            
            st.session_state.current_result = result
            
            st.session_state.history.insert(
                    0,
                     {
                         "article": article,
                         "result": result,
                         "time": timestamp
                         }
                    )
            st.session_state.history = st.session_state.history[:5]
            

        st.success("Analysis Complete")

        st.markdown("---")

if st.session_state.get("current_result"):

    st.markdown("---")

    with st.expander(
        "📋 Analysis Report",
        expanded=True
    ):
        st.markdown(
            st.session_state.current_result
        )
   
