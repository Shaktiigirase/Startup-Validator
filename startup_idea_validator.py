
import streamlit as st
from googlesearch import search
import openai

# OPTIONAL: Add your OpenAI key (if you have one)
# openai.api_key = "sk-..."

st.set_page_config(page_title="Startup Validator", page_icon="🚀")
st.title("🚀 Startup Idea Validator Tool")

idea = st.text_area("💡 What's your startup idea?", "")

if st.button("✅ Validate Idea"):
    with st.spinner("Validating..."):

        # Step 1: Google search
        query = f"{idea} startup"
        results = list(search(query, num_results=5))

        st.subheader("🔎 Similar Startups Found:")
        for i, link in enumerate(results):
            st.markdown(f"{i+1}. {link}")

        # Step 2: Optional AI Feedback
        st.subheader("🤖 AI Feedback:")
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You're a startup mentor."},
                    {"role": "user", "content": f"Evaluate this startup idea: {idea}. Give feedback in 3 bullet points."}
                ]
            )
            st.write(response['choices'][0]['message']['content'])
        except:
            st.warning("No OpenAI API key found or error occurred.")
