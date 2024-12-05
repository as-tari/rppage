import streamlit as st
from word_document_parser import parse_word_document, identify_chapters
from page_counter import count_pages_for_chapters
from report_generator import generate_report

def main():
    st.title("Word Document Page Detector")

    file_uploader = st.file_uploader("Upload a Word document (.docx)", type="docx")
    if file_uploader is not None:
        file_path = file_uploader.name
        text = parse_word_document(file_uploader)
        chapters = identify_chapters(text)
        page_counts = count_pages_for_chapters(chapters)
        report = generate_report(page_counts)

        st.write("Report:")
        st.write(report)

        @st.cache
        def convert_df(report):
            return report.to_csv(index=False)

        csv = convert_df(report)

        st.download_button(
            label="Download report as CSV",
            data=csv,
            file_name="report.csv",
            mime="text/csv",
        )

if __name__ == "__main__":
    main()