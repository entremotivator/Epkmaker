import streamlit as st
from fpdf import FPDF
import json

# Helper function to generate Sports EPK PDF
def generate_sports_epk_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt=data["title"], ln=True, align="C")
    pdf.ln(10)

    # Summary
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Event/Team Summary:", ln=True, align="L")
    pdf.multi_cell(0, 10, data["summary"])
    pdf.ln(5)

    # Coach/Athlete Statement
    pdf.cell(200, 10, txt="Coach/Athlete Statement:", ln=True, align="L")
    pdf.multi_cell(0, 10, data["statement"])
    pdf.ln(5)

    # Event/Team Details
    pdf.cell(200, 10, txt="Event/Team Details:", ln=True, align="L")
    pdf.multi_cell(0, 10, f"Budget: {data['budget']}")
    pdf.multi_cell(0, 10, f"Location: {data['location']}")
    pdf.multi_cell(0, 10, f"Event Date: {data['event_date']}")
    pdf.multi_cell(0, 10, f"Year Founded: {data['year_founded']}")
    pdf.ln(5)

    # Team and Roster
    pdf.cell(200, 10, txt="Team Roster:", ln=True, align="L")
    for role, name in data["team_roster"].items():
        pdf.multi_cell(0, 10, f"{role}: {name}")
    pdf.ln(5)

    # Achievements
    pdf.cell(200, 10, txt="Achievements and Awards:", ln=True, align="L")
    pdf.multi_cell(0, 10, data["achievements"])
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
    pdf_file = "Sports_EPK.pdf"
    pdf.output(pdf_file)
    return pdf_file

# Page: Home
def home_page():
    st.title("Sports EPK Toolkit")
    st.write("Welcome to the Sports EPK Toolkit! This app includes multiple features to help teams, athletes, and event organizers:")
    st.markdown("""
    - **Sports EPK Generator**: Create a professional press kit for your team, athlete, or event.
    - **Game Plan Generator**: Develop detailed game plans with strategies.
    - **Player Profile Development**: Create detailed profiles for players with key statistics and traits.
    - **Event Overview Generator**: Generate a comprehensive outline for sports events.
    """)

# Page: Sports EPK Generator
def sports_epk_generator_page():
    st.title("Sports EPK Generator")
    st.write("Create a professional Sports EPK with detailed information about your team, athlete, or event.")

    # Input fields
    title = st.text_input("Event/Team Name", "")
    summary = st.text_area("Event/Team Summary", "")
    statement = st.text_area("Coach/Athlete Statement", "")
    budget = st.text_input("Event Budget (e.g., $50K, $1M)", "")
    location = st.text_input("Location(s)", "")
    event_date = st.text_input("Event Date", "")
    year_founded = st.text_input("Year Founded", "")

    # Team Roster
    st.subheader("Team Roster")
    team_roster = {}
    for role in ["Coach", "Captain", "Goalkeeper", "Forward", "Defender", "Midfielder"]:
        team_roster[role] = st.text_input(role)

    # Achievements
    achievements = st.text_area("List Achievements and Awards (if any)", "")

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
    if st.button("Generate Sports EPK"):
        data = {
            "title": title,
            "summary": summary,
            "statement": statement,
            "budget": budget,
            "location": location,
            "event_date": event_date,
            "year_founded": year_founded,
            "team_roster": team_roster,
            "achievements": achievements,
            "contact_name": contact_name,
            "contact_email": contact_email,
            "contact_phone": contact_phone,
            "links": links_list
        }
        pdf_file = generate_sports_epk_pdf(data)
        st.success("Sports EPK generated successfully!")
        with open(pdf_file, "rb") as f:
            st.download_button("Download Sports EPK PDF", f, file_name="Sports_EPK.pdf")

# Page: Game Plan Generator
def game_plan_generator_page():
    st.title("Game Plan Generator")
    st.write("Develop a detailed game plan with strategies and goals.")

    team_name = st.text_input("Team Name", "")
    strategy = st.text_area("Overall Strategy", "")
    goals = st.text_area("Game Goals", "")
    challenges = st.text_area("Anticipated Challenges", "")
    st.button("Generate Game Plan")

# Page: Player Profile Development
def player_profile_page():
    st.title("Player Profile Development")
    st.write("Create detailed profiles for players with statistics and traits.")

    name = st.text_input("Player Name", "")
    position = st.text_input("Position", "")
    stats = st.text_area("Player Statistics (e.g., goals, assists, saves)", "")
    traits = st.text_area("Player Traits and Strengths", "")
    st.button("Save Player Profile")

# Page: Event Overview Generator
def event_overview_page():
    st.title("Event Overview Generator")
    st.write("Generate a comprehensive overview for your sports event.")

    event_name = st.text_input("Event Name", "")
    theme = st.text_input("Event Theme", "")
    schedule = st.text_area("Event Schedule", "")
    expected_audience = st.text_input("Expected Audience (e.g., 500 attendees)", "")
    sponsors = st.text_area("Sponsors and Partners", "")
    st.button("Generate Event Overview")

# Main app
def main():
    st.sidebar.title("Sports EPK Toolkit Navigation")
    page = st.sidebar.selectbox(
        "Go to",
        ["Home", "Sports EPK Generator", "Game Plan Generator", "Player Profile Development", "Event Overview Generator"]
    )

    if page == "Home":
        home_page()
    elif page == "Sports EPK Generator":
        sports_epk_generator_page()
    elif page == "Game Plan Generator":
        game_plan_generator_page()
    elif page == "Player Profile Development":
        player_profile_page()
    elif page == "Event Overview Generator":
        event_overview_page()

if __name__ == "__main__":
    main()
