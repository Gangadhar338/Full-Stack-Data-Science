import streamlit as st
import pandas as pd
from pathlib import Path
from io import BytesIO

st.set_page_config(page_title="Student Marks Analyzer", page_icon="📊", layout="wide")

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "students.csv"
SUBJECTS = ["subject1", "subject2", "subject3"]


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


def load_students():
    if not CSV_FILE.exists():
        raise FileNotFoundError("students.csv was not found.")

    data = pd.read_csv(CSV_FILE)
    required = ["name"] + SUBJECTS
    missing = [column for column in required if column not in data.columns]
    if missing:
        raise ValueError("Missing CSV columns: " + ", ".join(missing))
    data = data[required].copy()
    data["name"] = data["name"].astype("string").str.strip()

    if data.empty:
        raise ValueError("The CSV file contains no student records.")
    if data["name"].isna().any() or data["name"].eq("").any():
        raise ValueError("Every student must have a name.")

    for subject in SUBJECTS:
        data[subject] = pd.to_numeric(data[subject], errors="raise")
    if data[SUBJECTS].isna().any().any():
        raise ValueError("Student marks cannot be empty.")
    if ((data[SUBJECTS] < 0) | (data[SUBJECTS] > 100)).any().any():
        raise ValueError("Marks must be between 0 and 100.")

    data["total"] = data[SUBJECTS].sum(axis=1)
    data["average"] = (data["total"] / len(SUBJECTS)).round(2)
    data["grade"] = data["average"].apply(calculate_grade)
    return data


def create_excel_report(students, subject_stats, ranking):
    output = BytesIO()
    grade_distribution = (
        students["grade"].value_counts().sort_index()
        .rename_axis("Grade").reset_index(name="Student Count")
    )
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        ranking.to_excel(writer, sheet_name="Student Rankings", index=False)
        subject_stats.to_excel(writer, sheet_name="Subject Analysis", index=False)
        grade_distribution.to_excel(writer, sheet_name="Grade Distribution", index=False)
    output.seek(0)
    return output.getvalue()


st.title("📊 Student Marks Analyzer")
st.write("Analyze student marks, grades, rankings, and subject-wise performance.")

try:
    students = load_students()
except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
    st.error(f"Unable to load student data: {error}")
    st.stop()
except (OSError, UnicodeError) as error:
    st.error(f"Unable to read students.csv: {error}")
    st.stop()

st.divider()
st.sidebar.header("🔎 Dashboard Filters")
search_name = st.sidebar.text_input("Search student", placeholder="Enter student name")
available_grades = sorted(students["grade"].unique().tolist())
selected_grades = st.sidebar.multiselect(
    "Filter by grade", options=available_grades, default=available_grades
)
sort_option = st.sidebar.selectbox(
    "Sort students by",
    ["Highest total first", "Lowest total first", "Name A-Z", "Name Z-A"]
)

filtered = students.copy()
if search_name.strip():
    filtered = filtered[filtered["name"].str.contains(
        search_name.strip(), case=False, regex=False, na=False
    )]
filtered = filtered[filtered["grade"].isin(selected_grades)]

if sort_option == "Highest total first":
    filtered = filtered.sort_values(["total", "name"], ascending=[False, True])
elif sort_option == "Lowest total first":
    filtered = filtered.sort_values(["total", "name"], ascending=[True, True])
elif sort_option == "Name A-Z":
    filtered = filtered.sort_values("name")
else:
    filtered = filtered.sort_values("name", ascending=False)

st.header("📌 Class Overview")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Students", len(students))
col2.metric("Class Average", f"{students['average'].mean():.2f}")
col3.metric("Highest Average", f"{students['average'].max():.2f}")
col4.metric("Lowest Average", f"{students['average'].min():.2f}")
st.caption("Overview metrics show the full class. The table and charts use selected filters.")
st.divider()

st.header("🏆 Student Rankings")
ranking = filtered.sort_values(["total", "name"], ascending=[False, True]).copy()
ranking.insert(0, "Rank", range(1, len(ranking) + 1))
ranking = ranking.rename(columns={
    "name": "Student", "subject1": "Subject 1", "subject2": "Subject 2",
    "subject3": "Subject 3", "total": "Total", "average": "Average", "grade": "Grade"
})
st.dataframe(ranking, use_container_width=True, hide_index=True)
st.download_button(
    label="📥 Download Student Report (CSV)",
    data=ranking.to_csv(index=False).encode("utf-8"),
    file_name="student_performance_report.csv",
    mime="text/csv"
)
st.divider()

st.header("📚 Subject-wise Analysis")
subject_stats = pd.DataFrame({
    "Subject": ["Subject 1", "Subject 2", "Subject 3"],
    "Class Average": [round(students[subject].mean(), 2) for subject in SUBJECTS],
    "Highest Mark": [students[subject].max() for subject in SUBJECTS],
    "Lowest Mark": [students[subject].min() for subject in SUBJECTS]
})
st.dataframe(subject_stats, use_container_width=True, hide_index=True)
st.subheader("Class Average by Subject")
st.bar_chart(subject_stats.set_index("Subject")[["Class Average"]])
st.divider()

st.header("📈 Student Performance Charts")
if not filtered.empty:
    chart_data = filtered.set_index("name")[SUBJECTS].copy()
    chart_data.columns = ["Subject 1", "Subject 2", "Subject 3"]
    st.subheader("Marks by Student and Subject")
    st.bar_chart(chart_data)
    st.subheader("Average Marks by Student")
    st.bar_chart(filtered.set_index("name")[["average"]])
    st.subheader("Grade Distribution")
    st.bar_chart(filtered["grade"].value_counts().sort_index())
else:
    st.info("No students match the selected filters.")

st.divider()
st.header("🥇 Top Performer")
top_student = students.sort_values(["total", "name"], ascending=[False, True]).iloc[0]
col1, col2, col3 = st.columns(3)
col1.metric("Student", str(top_student["name"]))
col2.metric("Total Marks", f"{top_student['total']:.0f} / 300")
col3.metric("Average", f"{top_student['average']:.2f}")
st.write(f"**Grade:** {top_student['grade']}")

st.divider()
st.header("📊 Download Complete Excel Report")
try:
    excel_data = create_excel_report(students, subject_stats, ranking)
    st.download_button(
        label="Download Excel Report (.xlsx)",
        data=excel_data,
        file_name="student_performance_report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    st.caption("Workbook sheets: Student Rankings, Subject Analysis, and Grade Distribution.")
except (ValueError, OSError, ImportError) as error:
    st.error(f"Could not create the Excel report: {error}")

st.divider()
st.caption("Student Marks Analyzer | Python • Pandas • Streamlit")
