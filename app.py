import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Wedding Album Selection Portal",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# High-End Luxury Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Montserrat:wght@300;400;500;600&display=swap');

    /* Global Body & Background */
    .stApp {
        background-color: #FAF7F2;
        color: #2C2A29;
        font-family: 'Montserrat', sans-serif;
    }

    /* Headings */
    h1, h2, h3, h4, .main-header-title {
        font-family: 'Cormorant Garamond', serif !important;
        font-weight: 600 !important;
        color: #1A1918 !important;
        letter-spacing: 0.5px;
    }

    h1 {
        font-size: 2.8rem !important;
        margin-bottom: 0.2rem !important;
    }

    h2 {
        font-size: 2.0rem !important;
        border-bottom: 1px solid #E5DEC9;
        padding-bottom: 8px;
        margin-top: 1.5rem !important;
    }

    /* Subtitle & Accent Text */
    .subtitle-text {
        font-family: 'Montserrat', sans-serif;
        font-size: 0.95rem;
        color: #7A7365;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 25px;
    }

    /* Luxury Card Containers */
    .luxury-card {
        background-color: #FFFFFF;
        border: 1px solid #EAE4D9;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 4px 16px rgba(184, 153, 91, 0.06);
        margin-bottom: 20px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .luxury-card:hover {
        box-shadow: 0 6px 20px rgba(184, 153, 91, 0.12);
    }

    /* Selection Badge */
    .selection-badge {
        background: #C5A059;
        color: #FFFFFF;
        font-size: 0.75rem;
        padding: 4px 10px;
        border-radius: 20px;
        text-transform: uppercase;
        letter-spacing: 1px;
        display: inline-block;
        margin-bottom: 10px;
    }

    /* Style for Buttons */
    .stButton>button {
        background-color: #C5A059 !important;
        color: #FFFFFF !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 500 !important;
        font-size: 0.85rem !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
        border-radius: 6px !important;
        border: none !important;
        padding: 10px 24px !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }

    .stButton>button:hover {
        background-color: #A8833E !important;
        box-shadow: 0 4px 12px rgba(168, 131, 62, 0.25) !important;
    }

    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        border-bottom: 1px solid #EAE4D9;
    }

    .stTabs [data-baseweb="tab"] {
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 1.3rem !important;
        font-weight: 600 !important;
        color: #7A7365 !important;
        padding-bottom: 12px;
    }

    .stTabs [aria-selected="true"] {
        color: #C5A059 !important;
        border-bottom-color: #C5A059 !important;
    }

    /* Swatch image container */
    .swatch-box {
        border-radius: 8px;
        overflow: hidden;
        border: 2px solid #EAE4D9;
        margin-bottom: 8px;
    }

    /* Custom Info Callout */
    .stAlert {
        background-color: #F6F2EA;
        border: 1px solid #E5DEC9;
        color: #5C5548;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Application Header
st.markdown("<p class='subtitle-text'>Bespoke Heirloom Album Selection</p>", unsafe_allow_html=True)
st.title("Tahmid's Wedding Photography & Videography")
st.caption("Welcome! Please customize your album cover options and curate your favorite wedding images below.")

# Session State Initialization for selections
if 'cover_design' not in st.session_state:
    st.session_state.cover_design = "Option 1: Cameo Picture with Spine Title"
if 'material_type' not in st.session_state:
    st.session_state.material_type = "Genuine Leather"
if 'color_choice' not in st.session_state:
    st.session_state.color_choice = "Saddle Tan Leather"

# Sidebar Live Summary
with st.sidebar:
    st.markdown("### 💍 Your Album Selection")
    st.markdown("---")
    st.markdown(f"**Cover Style:**  \n*{st.session_state.cover_design}*")
    st.markdown(f"**Material:**  \n*{st.session_state.material_type}*")
    st.markdown(f"**Color Choice:**  \n*{st.session_state.color_choice}*")
    st.markdown("---")
    
    gallery_link_sidebar = st.text_input("SmugMug Gallery Link", value="https://ketanuva.smugmug.com/2024/Maisha-Yusuf/n-cDQT47")
    gallery_pw_sidebar = st.text_input("Gallery Password", value="M&Y2024!", type="password")
    
    st.markdown("---")
    st.info("💡 **Tip:** Keep your SmugMug gallery open in another tab to view image reference numbers while filling out the table.")

# Main Navigation Tabs
tab_cover, tab_photos, tab_revisions = st.tabs([
    "1. Cover Style & Swatches", 
    "2. Photo Selections", 
    "3. Round-1 Layout Feedback"
])

# -----------------------------------------------------------------------------
# TAB 1: COVER DESIGN & COLOR SWATCHES
# -----------------------------------------------------------------------------
with tab_cover:
    st.markdown("## 1. Select Your Cover Cameo & Layout")
    st.write("Choose the layout for your cameo picture window and title placement:")

    col_opt1, col_opt2, col_opt3 = st.columns(3)

    with col_opt1:
        st.markdown("<div class='luxury-card'>", unsafe_allow_html=True)
        st.image(
            "https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=600&q=80",
            caption="Option 1: Large Cameo & Spine Title",
            use_container_width=True
        )
        st.markdown("**Option 1**")
        st.caption("Large front-cover cameo picture window with elegant title debossed along the spine.")
        if st.button("Select Option 1", key="btn_opt1"):
            st.session_state.cover_design = "Option 1: Cameo Picture with Spine Title"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with col_opt2:
        st.markdown("<div class='luxury-card'>", unsafe_allow_html=True)
        st.image(
            "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=600&q=80",
            caption="Option 2: Large Cameo & Front Title",
            use_container_width=True
        )
        st.markdown("**Option 2**")
        st.caption("Large prominent front-cover cameo picture window with custom title centered below.")
        if st.button("Select Option 2", key="btn_opt2"):
            st.session_state.cover_design = "Option 2: Large Cameo with Front Title"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with col_opt3:
        st.markdown("<div class='luxury-card'>", unsafe_allow_html=True)
        st.image(
            "https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=600&q=80",
            caption="Option 3: Small Cameo & Front Title",
            use_container_width=True
        )
        st.markdown("**Option 3**")
        st.caption("Minimalist small square cameo picture window paired with refined typography on the front cover.")
        if st.button("Select Option 3", key="btn_opt3"):
            st.session_state.cover_design = "Option 3: Small Cameo with Front Title"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("## 2. Cover Material & Color Swatches")

    # Material Type Selector
    material_choice = st.radio(
        "Select Material Collection:",
        ["Genuine Leather", "Leatherette / Vegan Leather", "Linen Fabric"],
        horizontal=True
    )
    st.session_state.material_type = material_choice

    if material_choice in ["Genuine Leather", "Leatherette / Vegan Leather"]:
        st.write("#### Available Leather Swatches")
        l_col1, l_col2, l_col3, l_col4 = st.columns(4)

        with l_col1:
            st.image("https://images.unsplash.com/photo-1558769132-cb1aea458c5e?auto=format&fit=crop&w=400&q=80", use_container_width=True)
            if st.button("Saddle Tan Leather", key="swatch_tan"):
                st.session_state.color_choice = "Saddle Tan Leather"
                st.rerun()

        with l_col2:
            st.image("https://images.unsplash.com/photo-1550684848-fac1c5b4e853?auto=format&fit=crop&w=400&q=80", use_container_width=True)
            if st.button("Classic Onyx Black", key="swatch_black"):
                st.session_state.color_choice = "Classic Onyx Black"
                st.rerun()

        with l_col3:
            st.image("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=400&q=80", use_container_width=True)
            if st.button("Forest Emerald", key="swatch_green"):
                st.session_state.color_choice = "Forest Emerald"
                st.rerun()

        with l_col4:
            st.image("https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=400&q=80", use_container_width=True)
            if st.button("Deep Wine Burgundy", key="swatch_burgundy"):
                st.session_state.color_choice = "Deep Wine Burgundy"
                st.rerun()

    else:
        st.write("#### Available Linen Fabric Swatches")
        f_col1, f_col2, f_col3, f_col4 = st.columns(4)

        with f_col1:
            st.image("https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?auto=format&fit=crop&w=400&q=80", use_container_width=True)
            if st.button("Natural Ivory Linen", key="swatch_ivory"):
                st.session_state.color_choice = "Natural Ivory Linen"
                st.rerun()

        with f_col2:
            st.image("https://images.unsplash.com/photo-1604014237800-1c9102c219da?auto=format&fit=crop&w=400&q=80", use_container_width=True)
            if st.button("Sand Oat Linen", key="swatch_sand"):
                st.session_state.color_choice = "Sand Oat Linen"
                st.rerun()

        with f_col3:
            st.image("https://images.unsplash.com/photo-1579546929518-9e396f3cc809?auto=format&fit=crop&w=400&q=80", use_container_width=True)
            if st.button("Slate Grey Linen", key="swatch_grey"):
                st.session_state.color_choice = "Slate Grey Linen"
                st.rerun()

        with f_col4:
            st.image("https://images.unsplash.com/photo-1557683316-973673baf926?auto=format&fit=crop&w=400&q=80", use_container_width=True)
            if st.button("Royal Sapphire Blue", key="swatch_navy"):
                st.session_state.color_choice = "Royal Sapphire Blue"
                st.rerun()

    st.markdown("---")
    st.markdown("## 3. Title Debossing & Cameo Details")

    c1, c2 = st.columns(2)
    with c1:
        cover_text = st.text_input("Cover Title Text", value="Maisha & Yusuf • May 18, 2024", help="Exact names and date to deboss on the album cover")
        font_style = st.selectbox("Cover Font Typography", ["Classic Elegant Serif", "Modern Script", "Minimalist Roman"])
    
    with c2:
        cameo_img_link = st.text_input("Cameo Picture Reference Number / Link", placeholder="e.g. MY_COVER_001.jpg or SmugMug link")
        album_size = st.selectbox("Album Size / Page Count", ["10 x 10 inches (40 Pages / Flush Mount)", "12 x 12 inches (50 Pages / Flush Mount)"])

# -----------------------------------------------------------------------------
# TAB 2: PHOTO SELECTION TABLE
# -----------------------------------------------------------------------------
with tab_photos:
    st.markdown("## Curate Your Album Photos")
    st.markdown("Select approx **60 – 65 images** to tell the complete story of your wedding day.")
    
    st.info("""
    ✨ **Recommended Variety:**
    Decorations & Details | Fine Art Portraits | Family & Parents | Moments & Ceremony | Reception & Toasts | Cake-Cutting & Dancing
    """)

    # Initial data list
    initial_data = []
    for i in range(1, 66):
        initial_data.append({
            "#": i,
            "Gallery Name + Image ID": f"MY_WEDDING_{i:03d}" if i <= 12 else "",
            "Image Link (Optional)": "",
            "Comments / Notes": "Must include full page spread" if i == 1 else ""
        })

    photos_df = pd.DataFrame(initial_data)

    edited_photos_df = st.data_editor(
        photos_df,
        use_container_width=True,
        num_rows="dynamic",
        column_config={
            "#": st.column_config.NumberColumn("No.", disabled=True, width="small"),
            "Gallery Name + Image ID": st.column_config.TextColumn("Gallery Reference / Image ID *", help="Enter image filename or ID"),
            "Image Link (Optional)": st.column_config.TextColumn("Direct Link"),
            "Comments / Notes": st.column_config.TextColumn("Notes (e.g. Convert to B&W, key family moment)")
        },
        height=500
    )

    # Counter calculation
    filled_rows = [x for x in edited_photos_df["Gallery Name + Image ID"] if str(x).strip() != ""]
    count_selected = len(filled_rows)

    c_metric1, c_metric2 = st.columns([1, 3])
    with c_metric1:
        st.metric("Total Selected Images", f"{count_selected} / 65")
    with c_metric2:
        st.progress(min(count_selected / 65, 1.0))

# -----------------------------------------------------------------------------
# TAB 3: ROUND-1 REVISION FEEDBACK
# -----------------------------------------------------------------------------
with tab_revisions:
    st.markdown("## Round-1 Album Spread Revisions")
    st.write("Once your initial draft spread design is ready, review each page spread and request changes below.")

    spreads = ["Cover"] + [f"Spreads {i}-{i+1}" for i in range(1, 40, 2)]
    
    revision_data = []
    for s in spreads:
        revision_data.append({
            "Pages / Spread": s,
            "General Feedback": "",
            "Remove Picture Number": "",
            "Add Picture Number": ""
        })

    revision_df = pd.DataFrame(revision_data)

    edited_revisions_df = st.data_editor(
        revision_df,
        use_container_width=True,
        column_config={
            "Pages / Spread": st.column_config.TextColumn("Page Spread", disabled=True),
            "General Feedback": st.column_config.TextColumn("Design Feedback"),
            "Remove Picture Number": st.column_config.TextColumn("Remove Image #"),
            "Add Picture Number": st.column_config.TextColumn("Add Image #")
        },
        height=450
    )

# -----------------------------------------------------------------------------
# SUBMISSION & EXPORT
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown("### 📩 Complete Selection")

if st.button("Submit Final Selections & Generate Summary"):
    st.balloons()
    st.success("✨ Your selections have been compiled successfully!")

    # Summary dataframe compilation
    summary_cover = pd.DataFrame([{
        "Cover Design": st.session_state.cover_design,
        "Material Type": st.session_state.material_type,
        "Color Choice": st.session_state.color_choice,
        "Cover Title Text": cover_text,
        "Font Choice": font_style,
        "Cameo Link": cameo_img_link,
        "Album Size": album_size,
        "Total Photos Selected": count_selected
    }])

    csv_data = summary_cover.to_csv(index=False)

    st.download_button(
        label="📥 Download Album Selection Summary (.csv)",
        data=csv_data,
        file_name="Wedding_Album_Selections.csv",
        mime="text/csv"
    )
