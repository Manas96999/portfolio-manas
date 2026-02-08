import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# -----------------------------------------------------------------------------
# 1. USER CONFIGURATION (EDIT THIS SECTION ONLY)
# -----------------------------------------------------------------------------
NAME = "Manas Hitendra Bramhankar"
TITLE = "Data Analyst | AI & ML Engineer"
LOCATION = "Nashik, Maharashtra"
EMAIL = "manasbramhankar@gmail.com"
LINKEDIN_URL = "www.linkedin.com/in/manas-bramhankar-73831628b"
GITHUB_URL = "https://github.com/Manas96999"

# PROFILE IMAGE:
# Replace 'profile.png' with your actual file name (put it in the same folder).
# If you don't have one yet, leave it as None to show a placeholder.
PROFILE_IMAGE_PATH = "manasprofile.png" 

# RESUME:
# Put your PDF in the folder and name it 'resume.pdf'
RESUME_PATH = "R1.pdf"

# SUMMARY:
ABOUT_ME = """
I am a Data Analyst focused on turning messy, raw data into clear business strategies. 
Currently a B.Tech student at Sandip Foundation (CGPA: 8.0), I specialize in the full data lifecycle:

* **SQL:** I write complex queries to extract, filter, and aggregate large datasets from relational databases.
* **Python (Pandas/NumPy):** I use Python for advanced data cleaning, exploratory data analysis (EDA), and automating repetitive workflows.
* **Excel:** I leverage Excel for financial modeling, pivot tables, and quick ad-hoc analysis.
* **Power BI:** I transform processed data into interactive, storytelling dashboards that stakeholders use to make decisions.

My goal is to secure a 6-month internship where I can apply these skills to solve real-world business problems. 

My experience ranges from building hardware-integrated AI models (Drone Weapon Detection) 
to crafting business intelligence dashboards for real-world industries (Healthcare & Fashion Retail).
Currently seeking a 6-month internship to apply my skills in Data Analytics and Machine Learning.
"""

# -----------------------------------------------------------------------------
# 2. PROJECT DATABASE (EASY ADD SLOT)
# -----------------------------------------------------------------------------
# To add a NEW project, just copy one of these blocks ({...}), paste it, 
# and change the text. The app handles the design automatically.

PROJECTS = [
    {
        "title": "World Class Healthcare Dashboard",
        "type": "Data Analytics & Visualization",
        "tech": ["Tableau", "PythonSQL", "Data Modeling"],
        "desc": "Designed an end-to-end BI solution to track hospital KPIs. Modeled complex patient data to visualize treatment outcomes, reducing reporting time by 40%. Features interactive slicers for departmental analysis.",
        "link": "#",  # Put your Power BI public link here
        "image_placeholder": "📊"  # You can replace this with an image path later
    },
    {
        "title": "Drone Weapon Detection System",
        "type": "Computer Vision / AI",
        "tech": ["YOLOv8", "Python", "Raspberry Pi", "OpenCV"],
        "desc": "Developed a real-time object detection system for surveillance drones during my internship at Skycircuit Innovation. Optimized the YOLO model to run efficiently on edge devices (Raspberry Pi) with high accuracy.",
        "link": "https://github.com/Manas96999/Weapon-detection-model-",
        "image_placeholder": "🚁"
    },
    {
        "title": "'7 Vogue' Market Analysis",
        "type": "Business Intelligence / Entrepreneurship",
        "tech": ["Python", "Pandas", "Matplotlib", "Excel"],
        "desc": "Problem: Unpredictable inventory costs were eating into profits. \nAction: Built an automated sales tracker using Python to forecast demand.\n\nResult: Reduced dead stock by 20% and identified the top 3 best-selling designs for the upcoming season. Analyzed customer purchase behavior and market trends to optimize inventory stocking, directly improving profit margins.",
        "link": "https://github.com/Manas96999/7-Vogue-Market-Analysis",
        "image_placeholder": "👕"
        
    }
]

# -----------------------------------------------------------------------------
# 3. PAGE SETUP & CUSTOM CSS (THE "LOOK")
# -----------------------------------------------------------------------------
st.set_page_config(page_title=f"{NAME} Portfolio", layout="wide", page_icon="📊")

# Custom CSS for the "Dark Tech" Aesthetic
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Headings */
    h1, h2, h3 {
        color: #00ADB5 !important;
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* Project Cards (Glassmorphism) */
    .project-container {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        transition: transform 0.2s;
    }
    .project-container:hover {
        transform: scale(1.01);
        border-color: #00ADB5;
    }
    
    /* Tags for Skills */
    .tech-tag {
        background-color: #238636;
        color: white;
        padding: 4px 10px;
        border-radius: 15px;
        font-size: 0.8rem;
        margin-right: 5px;
        display: inline-block;
        margin-bottom: 5px;
    }
    
    /* Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        background-color: #00ADB5;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #007B81;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. SIDEBAR NAVIGATION
# -----------------------------------------------------------------------------
with st.sidebar:
    # Navigation Menu
    selected = option_menu(
        menu_title=None,
        options=["Home", "Projects", "Resume & Skills", "Contact"],
        icons=["house", "code-slash", "file-earmark-person", "envelope"],
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#0E1117"},
            "icon": {"color": "#00ADB5", "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#262730"},
            "nav-link-selected": {"background-color": "#262730"},
        }
    )
    
    st.write("---")
    
    # CORRECTED SECTION: Using Markdown for clickable badges
    st.markdown(f"""
    <a href="{LINKEDIN_URL}" target="_blank">
        <img src="https://img.shields.io/badge/-LinkedIn-0077B5?style=flat&logo=Linkedin&logoColor=white" alt="LinkedIn">
    </a>
    &nbsp; 
    <a href="{GITHUB_URL}" target="_blank">
        <img src="https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github&logoColor=white" alt="GitHub">
    </a>
    """, unsafe_allow_html=True)
    
    st.write(f"📍 {LOCATION}")

# -----------------------------------------------------------------------------
# 5. PAGE CONTENT LOGIC
# -----------------------------------------------------------------------------

# --- HOME SECTION ---
if selected == "Home":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"<h1 style='font-size: 60px; margin-bottom: 0;'>Hi, I'm Manas.</h1>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: #8b949e !important;'>{TITLE}</h3>", unsafe_allow_html=True)
        st.write("---")
        # NEW CODE FOR BIGGER FONT
        st.markdown(f"""
        <div style="font-size: 20px; line-height: 1.6; color: #E0E0E0;">
            {ABOUT_ME}
        """, unsafe_allow_html=True)
        
        # Call to Action Buttons
        c1, c2 = st.columns(2)
        with c1:
            st.info("💡 **Open to 6-Month Internships**")
        with c2:
            # Resume Download Logic
            try:
                with open(RESUME_PATH, "rb") as pdf_file:
                    st.download_button(
                        label="📄 Download Resume",
                        data=pdf_file,
                        file_name="Manas_Bramhankar_Resume.pdf",
                        mime="application/pdf"
                    )
            except FileNotFoundError:
                st.warning("⚠️ Resume file not found. Please add 'resume.pdf' to the folder.")

    with col2:
        # Profile Image Logic
        try:
            if PROFILE_IMAGE_PATH:
                image = Image.open(PROFILE_IMAGE_PATH)
                st.image(image, width=300)
        except:
            # Fallback if no image is found
            st.markdown("""
            <div style="background-color: #161b22; height: 300px; display: flex; align-items: center; justify-content: center; border-radius: 50%; border: 2px solid #00ADB5;">
                <span style="font-size: 80px;">👨‍💻</span>
            </div>
            """, unsafe_allow_html=True)

# --- PROJECTS SECTION ---
elif selected == "Projects":
    st.title("💻 Featured Projects")
    st.write("A selection of my work in Data Analytics, Machine Learning, and Business Intelligence.")
    st.write("---")

    # Loop through the PROJECTS list defined at the top
    for project in PROJECTS:
        # Create a container for each project
        with st.container():
            st.markdown(f"""
            <div class="project-container">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h2 style="margin: 0; font-size: 24px;">{project['title']}</h2>
                    <span style="background-color: #1f6feb; padding: 5px 10px; border-radius: 5px; font-size: 12px; font-weight: bold;">{project['type']}</span>
                </div>
                <p style="margin-top: 10px; font-size: 16px; color: #c9d1d9;">{project['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Tech Stack Tags
            tags_html = ""
            for tech in project['tech']:
                tags_html += f'<span class="tech-tag">{tech}</span>'
            st.markdown(tags_html, unsafe_allow_html=True)
            
            # Link / Image
            c1, c2 = st.columns([1, 4])
            with c1:
                if st.button(f"View Project 🔗", key=project['title']):
                    st.write(f"Redirecting to {project['link']}...")
            st.write("---")

# --- RESUME & SKILLS SECTION ---
elif selected == "Resume & Skills":
    st.title("🚀 Skills & Qualifications")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🛠 Technical Arsenal")
        st.markdown("""
        * **Languages:** Python 🐍, SQL 🗄️, C++
        * **Visualization:** Power BI 📊, Tableau, Matplotlib
        * **Machine Learning:** YOLOv8 🤖, Scikit-Learn, Pandas
        * **Tools:** Git, Excel, Raspberry Pi 🍓
        """)
        
    with col2:
        st.subheader("🎓 Education")
        st.markdown(f"""
        **B.Tech in AI & Data Science**
        *Sandip Foundation (2027)*
        * **CGPA:** 8.0
        * **Relevant Coursework:** DBMS, Data Structures, Neural Networks
        """)
        
    st.write("---")
    st.subheader("💼 Experience")
    st.info("""
    **Drone Engineer Intern | Skycircuit Innovation**
    *6 Months*
    * Engineered hardware-software integration for drone flight stabilization.
    * Collaborated with a team of 4 to deploy real-time object detection models.
    """)

# --- CONTACT SECTION ---
elif selected == "Contact":
    st.title("📬 Get In Touch")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("I am currently available for **6-month internships**.")
        st.write(f"📧 **Email:** {EMAIL}")
        st.write(f"🔗 **LinkedIn:** {LINKEDIN_URL}")
        st.write(f"🐙 **GitHub:** {GITHUB_URL}")
        
    with col2:
        st.markdown("### Send a Message")
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Message")
            submit = st.form_submit_button("Send Message")
            
            if submit:
                st.success("Thanks! I'll get back to you soon.")