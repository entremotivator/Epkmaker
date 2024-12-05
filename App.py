import streamlit as st
from fpdf import FPDF
import os
from PIL import Image

# Function to generate PDF EPK
def generate_epk_pdf(data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Arial", size=20, style="B")
    pdf.cell(200, 10, txt="Electronic Press Kit", ln=True, align='C')
    pdf.ln(10)

    # Artist/Company Bio
    pdf.set_font("Arial", size=14, style="B")
    pdf.cell(200, 10, txt="Artist/Company Bio", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, data['bio'])
    pdf.ln(5)

    # Services/Industry Placement
    pdf.set_font("Arial", size=14, style="B")
    pdf.cell(200, 10, txt="Services/Industry Placement", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, data['services'])
    pdf.ln(5)

    # Contact Information
    pdf.set_font("Arial", size=14, style="B")
    pdf.cell(200, 10, txt="Contact Information", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Name: {data['contact_name']}\nEmail: {data['contact_email']}\nPhone: {data['contact_phone']}")
    pdf.ln(5)

    # Outbound Links
    pdf.set_font("Arial", size=14, style="B")
    pdf.cell(200, 10, txt="Outbound Links", ln=True)
    pdf.set_font("Arial", size=12)
    for link in data['links']:
        pdf.cell(0, 10, txt=link, ln=True, link=link)
    pdf.ln(5)

    # Add Press Shot if available
    if data['press_shot']:
        pdf.add_page()
        pdf.set_font("Arial", size=14, style="B")
        pdf.cell(200, 10, txt="Press Shot", ln=True)
        pdf.ln(5)
        pdf.image(data['press_shot'], x=10, y=None, w=180)

    # Save the PDF
    pdf_file = "EPK.pdf"
    pdf.output(pdf_file)
    return pdf_file

# Streamlit App
st.title("Electronic Press Kit (EPK) Generator")
st.write("Create a professional EPK for your project or brand.")

# Form inputs
with st.form("epk_form"):
    st.header("Step 1: Add Details")

    bio = st.text_area("Artist/Company Bio", "")
    services = st.text_area("Services/Industry Placement", "")
    contact_name = st.text_input("Contact Name", "")
    contact_email = st.text_input("Contact Email", "")
    contact_phone = st.text_input("Contact Phone", "")

    st.header("Step 2: Add Media")
    press_shot = st.file_uploader("Upload a Press Shot (optional)", type=["jpg", "jpeg", "png"])

    st.header("Step 3: Add Links")
    links = st.text_area("Outbound Links (one per line)", "")

    submit = st.form_submit_button("Generate EPK")

# Process form data
if submit:
    # Save uploaded press shot locally
    press_shot_path = None
    if press_shot:
        press_shot_image = Image.open(press_shot)
        press_shot_path = os.path.join("temp_press_shot.jpg")
        press_shot_image.save(press_shot_path)

    # Prepare data
    epk_data = {
        "bio": bio,
        "services": services,
        "contact_name": contact_name,
        "contact_email": contact_email,
        "contact_phone": contact_phone,
        "links": links.splitlines(),
        "press_shot": press_shot_path
    }

    # Generate PDF
    pdf_file = generate_epk_pdf(epk_data)

    # Display download link
    with open(pdf_file, "rb") as file:
        st.download_button(
            label="Download EPK",
            data=file,
            file_name="EPK.pdf",
            mime="application/pdf"
        )

    # Clean up
    if press_shot_path:
        os.remove(press_shot_path)
    st.success("Your EPK has been generated!")
