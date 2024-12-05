import streamlit as st
from fpdf import FPDF
import json

# Helper function to generate EPK PDF
def generate_epk_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt=data["title"], ln=True, align="C")
    pdf.ln(10)

    # Summary
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Film Summary:", ln=True, align="L")
    pdf.multi_cell(0, 10, data["summary"])
    pdf.ln(5)

    # Director's Statement
    pdf.cell(200, 10, txt="Director's Statement:", ln=True, align="L")
    pdf.multi_cell(0, 10, data["director_statement"])
    pdf.ln(5)

    # Film Details
    pdf.cell(200, 10, txt="Film Details:", ln=True, align="L")
    pdf.multi_cell(0, 10, f"Budget: {data['budget']}")
    pdf.multi_cell(0, 10, f"Location: {data['location']}")
    pdf.multi_cell(0, 10, f"Runtime: {data['runtime']}")
    pdf.multi_cell(0, 10, f"Production Year: {data['year']}")
    pdf.ln(5)

    # Cast and Crew
    pdf.cell(200, 10, txt="Cast and Crew:", ln=True, align="L")
    for role, name in data["cast_and_crew"].items():
        pdf.multi_cell(0, 10, f"{role}: {name}")
    pdf.ln(5)

    # Awards
    pdf.cell(200, 10, txt="Awards and Nominations:", ln=True, align="L")
    pdf.multi_cell(0, 10, data["awards"])
    pdf.ln(5)

    # Contact Information
    pdf.cell(200, 10, txt="Contact Information:", ln=True, align="L")
    pdf.multi_cell(0, 10, f"Name: {data['contact_name']}")
    pdf.multi_cell(0, 10, f"Email: {data['contact_email']}")
    pdf.multi_cell(0, 10, f"Phone: {data['contact_phone']}")
    pdf.ln(5)

    # Links
    pdf.cell(200, 10, txt="Relevant Links:", ln=True, align="L")
    for link in data["links"]:
        pdf.multi_cell(0, 10, link)
    pdf.ln(5)

    # Save PDF
    pdf_file = "EPK.pdf"
    pdf.output(pdf_file)
    return pdf_file

# Page: Home
def home_page():
    st.title("Film Toolkit")
    st.write("Welcome to the Film Toolkit app! This app includes multiple features to help filmmakers and creative professionals:")
    st.markdown("""
    - **Electronic Press Kit (EPK) Generator**: Create a professional press kit for your film.
    - **Movie Script Generator**: Generate detailed movie scripts with structured scenes.
    - **Character Development**: Build deep and realistic characters with extensive details.
    - **Story Outline Generator**: Develop a comprehensive outline for your story.
    """)

# Page: EPK Generator
def epk_generator_page():
    st.title("Electronic Press Kit (EPK) Generator")
    st.write("Create a professional Film EPK with detailed information about your film.")

    # Input fields
    title = st.text_input("Film Title", "")
    summary = st.text_area("Film Summary", "")
    director_statement = st.text_area("Director's Statement", "")
    budget = st.text_input("Film Budget (e.g., $1M, $500K)", "")
    location = st.text_input("Shooting Location(s)", "")
    runtime = st.text_input("Runtime (e.g., 120 minutes)", "")
    year = st.text_input("Production Year", "")

    # Cast and Crew
    st.subheader("Cast and Crew")
    cast_and_crew = {}
    for role in ["Director", "Lead Actor", "Producer", "Cinematographer", "Costume Designer", "Editor"]:
        cast_and_crew[role] = st.text_input(role)

    # Awards and Nominations
    awards = st.text_area("List Awards or Festivals (if any)", "")

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
            "budget": budget,
            "location": location,
            "runtime": runtime,
            "year": year,
            "cast_and_crew": cast_and_crew,
            "awards": awards,
            "contact_name": contact_name,
            "contact_email": contact_email,
            "contact_phone": contact_phone,
            "links": links_list
        }
        pdf_file = generate_epk_pdf(data)
        st.success("EPK generated successfully!")
        with open(pdf_file, "rb") as f:
            st.download_button("Download EPK PDF", f, file_name="Film_EPK.pdf")

# Page: Movie Script Generator
def script_generator_page():
    st.title("Movie Script Generator")
    st.write("Generate a detailed movie script with structured scenes and dialogue.")

    title = st.text_input("Script Title", "")
    act1 = st.text_area("Act 1: Setup", "")
    act2 = st.text_area("Act 2: Confrontation", "")
    act3 = st.text_area("Act 3: Resolution", "")
    st.button("Generate Script")

# Page: Character Development
def character_development_page():
    st.title("Character Development")
    st.write("Create detailed character profiles for your film.")

    name = st.text_input("Character Name", "")
    role = st.text_input("Role in Story", "")
    backstory = st.text_area("Backstory", "")
    quirks = st.text_area("Quirks and Habits", "")
    st.button("Save Character")

# Page: Story Outline Generator
def story_outline_page():
    st.title("Story Outline Generator")
    st.write("Develop a detailed story outline for your film.")

    theme = st.text_input("Story Theme", "")
    tone = st.text_input("Tone and Style", "")
    conflict = st.text_area("Key Conflict", "")
    resolution = st.text_area("Resolution", "")
    st.button("Generate Outline")

# Main app
def main():
    st.sidebar.title("Film Toolkit Navigation")
    page = st.sidebar.selectbox(
        "Go to",
        ["Home", "EPK Generator", "Movie Script Generator", "Character Development", "Story Outline Generator"]
    )

    if page == "Home":
        home_page()
    elif page == "EPK Generator":
        epk_generator_page()
    elif page == "Movie Script Generator":
        script_generator_page()
    elif page == "Character Development":
        character_development_page()
    elif page == "Story Outline Generator":
        story_outline_page()

if __name__ == "__main__":
    main()
