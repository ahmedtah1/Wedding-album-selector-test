import streamlit as st
import pandas as pd

st.set_page_config(page_title="Wedding Album Selection Portal", layout="wide", page_icon="📸")

st.title("📸 Wedding Album Selection Portal")
st.subheader("Design & Photo Selection")

# Tab Layout based on your spreadsheet tabs
tab1, tab2 = st.tabs(["1. Cover & Photo Selections", "2. Round-1 Layout Feedback"])

with tab1:
    st.markdown("### 🎨 Cover Customization Options")
    col1, col2 = st.columns(2)
    
    with col1:
        material = st.selectbox("Cover Material", ["Leatherette", "Genuine Leather"])
        cover_color = st.text_input("Cover Color Choice", placeholder="e.g. Saddle Brown, Cream, Ivory")
        cover_design = st.selectbox(
            "Cover Design Style", 
            [
                "Option 1: Large Cameo picture and Title in the spine",
                "Option 2: Large Cameo picture and Title on front cover",
                "Option 3: Small Cameo picture and Title on front cover"
            ]
        )
    
    with col2:
        font_choice = st.selectbox("Font Style for Cover Text", ["Classic Serif", "Modern Script", "Minimalist Sans-Serif"])
        cover_text = st.text_input("Title Text for Cover", placeholder="e.g. Maisha & Yusuf - May 18, 2024")
        cameo_link = st.text_input("Cameo Picture Link / Image #", placeholder="e.g. IMG_1024.jpg or Gallery Link")

    st.divider()

    st.markdown("### 🖼️ Photo Selections (Target: 60–65 Images)")
    st.info("Suggested selections: Decors, portraits, family groups, key moments, speeches, cake cutting, and dancing.")

    # Data editor for picture selection
    default_data = pd.DataFrame({
        "Image # / ID": [f"IMG_{i:03d}" for i in range(1, 11)] + [""] * 50,
        "Gallery Link": [""] * 60,
        "Comments / Notes": [""] * 60
    })
    
    edited_photos = st.data_editor(
        default_data,
        num_rows="dynamic",
        use_container_width=True,
        column_config={
            "Image # / ID": st.column_config.TextColumn("Gallery + Image ID", help="Enter image filename or number"),
            "Gallery Link": st.column_config.LinkColumn("Direct Image Link"),
            "Comments / Notes": st.column_config.TextColumn("Special Notes (e.g. Full spread, B&W conversion)")
        }
    )

    # Calculate selected photos count
    selected_count = len([x for x in edited_photos["Image # / ID"] if str(x).strip() != ""])
    st.metric(label="Total Selected Photos", value=f"{selected_count} / 65")

with tab2:
    st.markdown("### 📑 Spread-by-Spread Revision Feedback")
    st.caption("Review your draft album spreads and list any requested changes below.")

    spread_list = ["Cover", "Spreads 1-2", "Spreads 3-4", "Spreads 5-6", "Spreads 7-8", "Spreads 9-10",
                   "Spreads 11-12", "Spreads 13-14", "Spreads 15-16", "Spreads 17-18", "Spreads 19-20"]

    feedback_df = pd.DataFrame({
        "Spread / Pages": spread_list,
        "General Feedback": [""] * len(spread_list),
        "Remove Picture #": [""] * len(spread_list),
        "Add Picture #": [""] * len(spread_list)
    })

    edited_feedback = st.data_editor(feedback_df, use_container_width=True)

# Submit & Export
st.divider()
if st.button("Submit Final Selections", type="primary"):
    st.success("Selections saved! Downloading summary file...")
    
    # Save cover details and tables to CSV format
    cover_summary = pd.DataFrame([{
        "Material": material,
        "Color": cover_color,
        "Design": cover_design,
        "Font": font_choice,
        "Cover Text": cover_text,
        "Cameo Link": cameo_link
    }])
    
    csv_data = cover_summary.to_csv(index=False)
    st.download_button(
        label="📥 Download Selection Summary (.csv)",
        data=csv_data,
        file_name="Album_Selections_Summary.csv",
        mime="text/csv"
    )
