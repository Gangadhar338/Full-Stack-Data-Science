
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Student Marks Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Student Marks Analyzer")
st.write("Analyze student performance, grades, and class rankings.")

# Load student data
csv_file = Path(__file__).parent / "students.csv"

try:
    df = pd.read_csv(csv_file)

    required_columns = ["name", "subject1", "subject2", "subject3"]

    if not all(col in df.columns for col in required_columns):
        st.error(
            "students.csv must contain: "
            "name, subject1, subject2, subject3"
        )
        st.stop()

    # Calculate marks and grades
    subjects = ["subject1", "subject2", "subject3"]

    for subject in subjects:
        df[subject] = pd.to_numeric(df[subject], errors="raise")

    if df[subjects].isna().any().any():
        st.error("Student marks cannot be empty.")
        st.stop()

    if ((df[subjects] < 0) | (df[subjects] > 100)).any().any():
        st.error("Marks must be between 0 and 100.")
        st.stop()

    df["total"] = df[subjects].sum(axis=1)
    df["average"] = (df["total"] / len(subjects)).round(2)

    def calculate_grade(average):
        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 40:
            return "D"
        return "F"

    df["grade"] = df["average"].apply(calculate_grade)

    # Sidebar filters
    st.sidebar.header("Dashboard Filters")

    grades = ["All"] + sorted(df["grade"].unique().tolist())
    selected_grade = st.sidebar.selectbox(
        "Filter by grade",
        grades
    )

    search_name = st.sidebar.text_input("Search student name")

    filtered_df = df.copy()

    if selected_grade != "All":
        filtered_df = filtered_df[
            filtered_df["grade"] == selected_grade
        ]

    if search_name.strip():
        filtered_df = filtered_df[
            filtered_df["name"].str.contains(
                search_name.strip(),
                case=False,
                na=False
            )
        ]

    # Summary metrics
    st.subheader("Class Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Students", len(df))
    col2.metric(
        "Class Average",
        f"{df['average'].mean():.2f}"
    )
    col3.metric(
        "Highest Average",
        f"{df['average'].max():.2f}"
    )
    col4.metric(
        "Lowest Average",
        f"{df['average'].min():.2f}"
    )

    st.divider()

    # Ranking table
    st.subheader("🏆 Student Rankings")

    ranking = filtered_df.sort_values(
        by=["total", "name"],
        ascending=[False, True]
    ).reset_index(drop=True)

    ranking.index = ranking.index + 1
    ranking.index.name = "Rank"

    st.dataframe(
        ranking,
        use_container_width=True
    )

    if ranking.empty:
        st.info("No students match your filters.")

    # Performance chart
    st.subheader("📈 Student Performance")

    if not filtered_df.empty:
        chart_data = filtered_df.set_index("name")[
            ["subject1", "subject2", "subject3"]
        ]

        chart_data.columns = [
            "Subject 1",
            "Subject 2",
            "Subject 3"
        ]

        st.bar_chart(chart_data)

        average_chart = filtered_df.set_index("name")[["average"]]
        st.subheader("Average Marks")
        st.bar_chart(average_chart)

    # Download report
    st.subheader("📥 Download Report")

    report = ranking.reset_index()

    csv_data = report.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Student Report (CSV)",
        data=csv_data,
        file_name="student_performance_report.csv",
        mime="text/csv"
    )

    st.caption("Student Marks Analyzer | Built with Python, Pandas and Streamlit")

except FileNotFoundError:
    st.error("students.csv was not found in the project folder.")

except (ValueError, TypeError):
    st.error("Check students.csv: marks must be valid numbers.")

except Exception as error:
    st.error(f"An unexpected error occurred: {error}")
