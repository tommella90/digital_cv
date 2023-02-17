from pathlib import Path
import streamlit as st
from PIL import Image


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic (6).png"


PAGE_TITLE = "Digital CV - Tommaso Ramella"
PAGE_ICON = ":🧊:"
NAME = "Tommaso Ramella"
DESCRIPTION = """
Data scientist & postdoctoral researcher in economics
"""
EMAIL = "tommaso.ramella90@gmail.com"
SOCIAL_MEDIA = {"LINKEDIN": "https://www.linkedin.com/in/tommaso-ramella/",
                "GITHUB": "https://github.com/tommella90",
                "PORTFOLIO": "https://github.com/tommella90/Tommy_Portfolio"
                }
PROJECTS = {
    "🤙🏻 Rock Scissor Paper with OpenCV and Touchdesigner": "https://github.com/tommella90/Rock-Scissor-Paper-move-recognition",
    "📊 Gradient descent visualization with Touchdesigner": "https://github.com/tommella90/Gradient-descent-Linear-Regression",
    "✒️ Wordckoud generator web app": "https://tommella90-word-count-generator-app-2tkhtd.streamlit.app/"
}

st.set_page_config(page_title=PAGE_TITLE,
                   page_icon=PAGE_ICON
                   )

st.title("TOMMASO RAMELLA - CV")

col1, col2 = st.columns([6,1])
with col1:
    st.markdown("#### Data scientist & postdoctoral researcher in economics")

    st.write("#")
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        st.write(f"[{platform}]({link})")

with col2:
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)
    st.image(profile_pic, width=200)


# SKILLS
st.write('\n')
st.subheader("SKILLS")
st.write(
    """
- 👩‍💻 **Software and languages**: Python, R, MySQL, Tableau, Git, Linux, Docker
- 📚 **Statistics and data science**: econometrics, inferential statistics, time-series and longitudinal analysis, ML, hypothesis testing, NLP. Tools: Scikitlearn, Stastmodels, TensorFlow. Exploring: OpenCV, Mediapipe
- 📊 **Data analytics**: Data cleaning, data visualization, management of complex administrative data and population-level surveys, web scraping. Tools: Pandas, Pyspark, Matplotlib, Seaborn, Plotly, Beautiful Soup.
"""
)

# ABOUT ME
st.write('\n')
st.subheader("ABOUT ME")
st.write(
    """
I’m an academic researcher in economics now seeking a career in data science. I have several years of experience in statistics, data analytics, and econometrics with Python, Stata, and R, with a focus on causal inference, policy evaluation, longitudinal analysis, and management of complex datasets. I strongly believe that the next decades will be shaped by ML and AI, and even though this might seem scary, I feel really excited about it and I want to be part of this change. 
For these reasons, I’m looking for a new junior position as junior data scientist in a consultancy or startup in Berlin. I mostly value diversity (racial, sexual, and any non-conforming and non-harmful lifestyle) and human curiosity and I want to see where humans can get within my life cycle. 
"""
)


st.write("---")
# --- WORK HISTORY ---
st.write('\n')
st.subheader("WORK HISTORY")
st.write("---")

# --- JOB 1
st.write("🔵", "**DATA SCIENTIST, SOFTWARE DEVELOPER | VectorLab (freelance)**")
st.write("10/2022 - Present")
st.write(
    """
- 🔲 Developed innovative software connecting medical texts to codes, reducing coding errors with NLP and embedding methods
- 🔲 Architected a data structure for efficient navigation of hierarchical structures involving medical text data
- 🔲 Tested different models to improve resaerch speed and user exeperience 
"""
)

# --- JOB 2
st.write("#")
st.write("🔵", "**POSTDOCTORAL RESEARCHER IN ECONOMICS | University of Milan, Bicocca**")
st.write("09/2020 – Present")
st.write(
    """
- 🔲 Conducted extensive econometric and network analysis on international trade network to understand the reasons for the productivity gap between the US and the EU
- 🔲 Constructions of a complex database merging information from multinational firms and their relative connections with other firms
- 🔲 Conducted an extensive analysis of bilateral trade treaties, created clusters based on NLP techniques and embedding methods saving months of work 
"""
)

# --- JOB 3
st.write("#")
st.write("🔵", "**TEACHER ASSISTANT - DATA ANALYTICS BOOTCAMP | Ironhack (freelance)**")
st.write("09/2022 – 12/2022")
st.write(
    """
- 🔲 Delivered lectures on Python, SQL, inferential statistics & ML lifecycle to over 20 students
- 🔲 Guided ML and BI projects; maintained quality standards while adhering to deadlines
- 🔲 Instructed exercises on advanced topics such as web scraping, ML, EDA, BI & data visualization
"""
)

# --- JOB 4
st.write("#")
st.write("🔵", "**DATA ANALYST | Various**")
st.write(
    """
- **Regione Lombardia** - 02/2021 - 08/2021
- 🔲 Effectively managed the primary analysis of the "Youth Guarantee" policy in Lombardia, leveraging over 10 Gb of collected data. Merged and cleaned two data sources accessing individual employment histories.
- 🔲 Unveiled that the positive influence of the policy on employability substantially decreases after 6 months of internships.
- 🔲 Disclosed possibility for multinational companies to utilize the policy as an inexpensive hiring method.
"""
)

st.write("#")
st.write(
    """
- **Bicocca University** - 10/2020 – 04/2021
- 🔲 Statistically demonstrated that participating in ITS initiative increases firms' productivity over time
- 🔲 Created an artificial 'counterfactual' for firms participating in ITS through a matching procedure. This allowed classical econometric modeling.
- 🔲 Delivered a final project and presentation to a political audience
"""
)

st.write("#")
st.write(
    """
- **Piazza dei Mestieri** - 09/2021 – 12/2021
- 🔲 Conducted a descriptive analysis of the educational initiative **La piazza dei Mestieri** 
- 🔲 Statistically demonstrated the positive impact of the initiative on the employability of the participants
- 🔲 Written a report for the stakeholders of the initiative

"""
)

st.write("---")
# EDU
st.write('\n')
st.subheader("EDUCATION")

# --- EDU 1
st.write("#")
st.write("🔵", "**DATA ANALYTICS BOOTCAMP - Ironhack**")
st.write("05/2022 - 08/2022")
st.write(
    """
- 🔲 Data analysis, data science: ML, BI, EDA, SQL, data visualization, Tableau
- 🔲 Winner of the best project of the course (“Rock, Scissor, Paper with Computer Vision”)
"""
)

# --- EDU 2
st.write("#")
st.write("🔵", "**PH.D. IN ANALYSIS OF SOCIAL AND ECONOMIC PROCESSES - University of Milan, Bicocca**")
st.write("11/2017 - 11/2020")
st.write(
    """
- 🔲 Research topic: the role of personality traits on unemployment and over-employment
- 🔲 Delivered lectures and labs on statistical inference, econometrics, Stata, Python
- 🔲 Finished my thesis 3 months in advance  
- 🔲 Visiting period at longitudinal survey centers: HILDA (Melbourne) and SOEP (Berlin)
- 🔲 Ph.D. student leader
"""
)

# --- EDU 3
st.write("#")
st.write("🔵", "**MA IN CULTURAL ANTHROPOLGY - University of Milan, Bicocca**")
st.write("2014 - 2016")
st.write(
    """
- 🔲 Cultural Anthropology, philosophical approach in modern anthropology
- 🔲 Qualitative methods (participant-observation, ethnography, qualitative interviews)
- 🔲 2 months internship in the Nilgiri Mountains, India, delivering an ethnographic study for KEYSTONE FOUNDATION N.G.O.
"""
)

# --- EDU 4
st.write("#")
st.write("🔵", "**BA IN COGNITIVE PSYCHOLOGY  - University of Genova**")
st.write("2010 - 2014")
st.write(
    """
- 🔲 Cognitive and dynamic psychology
- 🔲 Construction and validation of psychometric tests
"""
)



st.write("---")
# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")




#%%
