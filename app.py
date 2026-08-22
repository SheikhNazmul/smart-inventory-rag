import os

import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Text Assistant", page_icon="🤖", layout="centered")

st.title("🤖 Simple GenAI Text Assistant")
st.caption("A beginner-friendly Generative AI project using OpenAI's API and Streamlit.")

api_key = os.getenv("OPENAI_API_KEY")

with st.sidebar:
    st.header("Settings")
    model = st.selectbox("Model", ["gpt-4o-mini", "gpt-4.1-mini"], index=0)
    temperature = st.slider("Creativity", 0.0, 1.0, 0.4, 0.1)

prompt = st.text_area(
    "Enter a prompt",
    placeholder="Explain machine learning to a beginner in 5 bullet points.",
    height=150,
)

if st.button("Generate", type="primary"):
    if not api_key:
        st.error("OPENAI_API_KEY is not configured. Add it as an environment variable before running the app.")
    elif not prompt.strip():
        st.warning("Please enter a prompt first.")
    else:
        try:
            client = OpenAI(api_key=api_key)
            with st.spinner("Generating response..."):
                response = client.responses.create(
                    model=model,
                    input=prompt.strip(),
                    temperature=temperature,
                )
            st.subheader("AI Response")
            st.write(response.output_text)
        except Exception as exc:
            st.error(f"Generation failed: {exc}")

st.divider()
st.caption("API keys are never stored in the repository. Use environment variables or Streamlit secrets.")
