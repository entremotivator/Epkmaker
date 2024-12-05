import streamlit as st
from fpdf import FPDF
import os

# Function to generate PDF for EPK
def generate_epk_pdf(data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Arial", size=20, style="B")
    pdf.cell(200, 10, txt="Film Electronic Press Kit", ln=True, align='C')
    pdf.ln(10)

    # Film/Company Title
    pdf.set_font("Arial", size=16, style="B")
    pdf.cell(200, 10, txt=f"Title: {data['title']}", ln=True)
    pdf.ln(5)

    # Film Summary
    pdf.set_font("Arial", size=14, style="B")
    pdf.cell(200, 10, txt="Film Summary", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, data['summary'])
    pdf.ln(5)

    # Director's Statement
    pdf.set_font("Arial", size=14, style="B")
    pdf.cell(200, 10, txt="Director's Statement", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, data['director_statement'])
    pdf.ln(5)

    # Cast and Crew
    pdf.set_font("Arial", size=14, style="B")
    pdf.cell(200, 10, txt="Cast and Crew", ln=True)
    pdf.set_font("Arial", size=12)
    for role, name in data['cast_and_crew'].items():
        pdf.cell(0, 10, txt=f"{role}: {name}", ln=True)
    pdf.ln(5)

    # Contact Information
    pdf.set_font("Arial", size=14, style="B")
    pdf.cell(200, 10, txt="Contact Information", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Name: {data['contact_name']}\nEmail: {data['contact_email']}\nPhone: {data['contact_phone']}")
    pdf.ln(5)

    # Links (Outbound Links or Video Embeds)
    pdf.set_font("Arial", size=14, style="B")
    pdf.cell(200, 10, txt="Outbound Links", ln=True)
    pdf.set_font("Arial", size=12)
    for link in data['links']:
        pdf.cell(0, 10, txt=link, ln=True, link=link)
    pdf.ln(5)

    # Save the PDF
    pdf_file = "Film_EPK.pdf"
    pdf.output(pdf_file)
    return pdf_file


# App Pages
def home_page():
    st.title("Welcome to the Film Project Toolkit!")
    st.markdown("""
    This application helps filmmakers and creatives generate essential materials for their projects. Here's what you can do:
    
    - **Electronic Press Kit Generator**: Create detailed EPKs for your film.
    - **Movie Script Generator**: Develop comprehensive movie scripts.
    - **Character Development**: Create and manage detailed character profiles.
    - **Story Outline Generator**: Build structured outlines for your story.
    """)

def epk_generator_page():
    st.title("Electronic Press Kit (EPK) Generator")
    st.write("Create a professional Film EPK with detailed information about your film.")

    # Input fields
    title = st.text_input("Film Title", "")
    summary = st.text_area("Film Summary", "")
    director_statement = st.text_area("Director's Statement", "")

    # Cast and Crew
    st.subheader("Cast and Crew")
    cast_and_crew = {}
    for role in ["Director", "Lead Actor", "Producer", "Cinematographer"]:
        cast_and_crew[role] = st.text_input(role)

    # Contact Details
    st.subheader("Contact Information")
    contact_name = st.text_input("Contact Name", "")
    contact_email = st.text_input("Contact Email", "")
    contact_phone = st.text_input("Contact Phone", "")

    # Links
    st.subheader("Outbound Links")
    links = st.text_area("Add relevant links (separate by commas)", "")
    links_list = [link.strip() for link in links.split(",")]

    # Generate EPK
    if st.button("Generate EPK"):
        data = {
            "title": title,
            "summary": summary,
            "director_statement": director_statement,
            "cast_and_crew": cast_and_crew,
            "contact_name": contact_name,
            "contact_email": contact_email,
            "contact_phone": contact_phone,
            "links": links_list
        }
        pdf_file = generate_epk_pdf(data)
        st.success("EPK generated successfully!")
        with open(pdf_file, "rb") as f:
            st.download_button("Download EPK PDF", f, file_name="Film_EPK.pdf")

def movie_script_generator_page():
    st.title("Movie Script Generator")
    st.write("Develop a detailed movie script based on your ideas.")
    
    title = st.text_input("Script Title", "")
    genre = st.selectbox("Genre", ["Drama", "Comedy", "Thriller", "Action", "Sci-Fi", "Horror"])
    storyline = st.text_area("Storyline", "Enter your main storyline here...")
    characters = st.text_area("Main Characters", "List your main characters here...")
    
    if st.button("Generate Script"):
        st.write("**Title:**", title)
        st.write("**Genre:**", genre)
        st.write("**Storyline:**", storyline)
        st.write("**Characters:**", characters)

def character_development_page():
    st.title("Character Development")
    st.write("Create detailed profiles for your characters.")
    
    name = st.text_input("Character Name", "")
    age = st.number_input("Age", min_value=0, step=1)
    role = st.text_input("Role in Story", "")
    backstory = st.text_area("Backstory", "Enter character backstory...")
    personality = st.text_area("Personality Traits", "List personality traits here...")
    
    if st.button("Generate Character Profile"):
        st.write("**Name:**", name)
        st.write("**Age:**", age)
        st.write("**Role:**", role)
        st.write("**Backstory:**", backstory)
        st.write("**Personality Traits:**", personality)

def story_outline_page():
    st.title("Story Outline Generator")
    st.write("Create a structured outline for your story.")
    
    title = st.text_input("Story Title", "")
    scenes = st.text_area("Scenes", "List scenes, separated by commas...")
    theme = st.text_input("Theme", "Enter the main theme of your story...")
    
    if st.button("Generate Outline"):
        st.write("**Title:**", title)
        st.write("**Scenes:**")
        for scene in scenes.split(","):
            st.write("-", scene.strip())
        st.write("**Theme:**", theme)


# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "EPK Generator", "Movie Script Generator", "Character Development", "Story Outline Generator"])

if page == "Home":
    home_page()
elif page == "EPK Generator":
    epk_generator_page()
elif page == "Movie Script Generator":
    movie_script_generator_page()
elif page == "Character Development":
    character_development_page()
elif page == "Story Outline Generator":
    story_outline_page()
