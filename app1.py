import streamlit as st
import google.generativeai as genai
import PyPDF2

# Function to retrieve text from PDF
def retrieve_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

# Main function to orchestrate the process
def main():
    # PDF Path
    pdf_path = (r"C:\Users\HP\Desktop\2404.07143.pdf")

    # Model Name
    model_name = "gemini-1.5-pro-latest"

    # Read API key from file
    with open(r"C:\Users\HP\Desktop\key.txt") as f:
        api_key = f.read()

    # Configure the API key
    genai.configure(api_key=api_key)

    # Create Streamlit UI
    st.title("🤖 Retrieval Augmented Generation System ")
    st.title("🧾 Leave No Context Behind")

    # User input: Question
    question = st.text_input("Ask me a question")

    if st.button("Submit"):
        if question:
            # Retrieve text
            text = retrieve_text_from_pdf(pdf_path)

            # Concatenate PDF text with question prompt
            context = text + "\n\n" + question

            # Initialize the generative model
            ai = genai.GenerativeModel(model_name=model_name)

            # Generate response
            response = ai.generate_content(context)  

            # Display results
            st.subheader("Question:")
            st.write(question)
            st.subheader("Answer:")
            st.write(response.text)
        else:
            st.warning("Please enter your question.")

if __name__ == "__main__":
    main()