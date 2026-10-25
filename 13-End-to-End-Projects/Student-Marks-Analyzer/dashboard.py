
import streamlit as st
import pandas as pd
from pathlib import Path

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Student Marks Analyzer",
    page_icon="📊",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "students.csv"

SUBJECTS = ["subject1", "subject2", "subject3"]

# ---------------- GRADE CALCULATION ----------------

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


# ---------------- LOAD AND VALIDATE DATA ----------------

@st.cache_data
def load_data(file_path, modified_time):
    data = pd.read_csv(file_path)

    required_columns = ["name"] + SUBJECTS

    missing_columns = [
        column for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            "Missing columns: " + ", ".join(missing_columns)
        )

    data = data[required_columns].copy()

    data["name"] = data["name"].astype("string").str.strip()

    if data.empty:
        raise ValueError("students.csv contains no student records.")

    if data["name"].isna().any() or data["name"].eq("").any():
        raise ValueError("Every student must have a name.")

    for subject in SUBJECTS:
        data[subject] = pd.to_numeric(
            data[subject],
            errors="raise"
        )

    if data[SUBJECTS].isna().any().any():
        raise ValueError("Student marks cannot be empty.")

    if ((data[SUBJECTS] < 0) | (data[SUBJECTS] > 100)).any().any():
        raise ValueError("All subject marks must be between 0 and 100.")

    data["total"] = data[SUBJECTS].sum(axis=1)
    data["average"] = (data["total"] / len(SUBJECTS)).round(2)
    data["grade"] = data["average"].apply(calculate_grade)

    return data


# ---------------- DASHBOARD HEADER ----------------

st.title("📊 Student Marks Analyzer")
st.write(
    "A student performance dashboard built with Python, "
    "Pandas, and Streamlit."
)

st.divider()

# ---------------- READ DATA ----------------

try:
    if not CSV_FILE.exists():
        st.error(f"File not found: {CSV_FILE.name}")
        st.info("Place students.csv in the same folder as dashboard.py.")
        st.stop()

    students = load_data(
        str(CSV_FILE),
        CSV_FILE.stat().st_mtime
    )

except (ValueError, TypeError, pd.errors.ParserError) as error:
    st.error(f"Unable to read student data: {error}")
    st.stop()

except (OSError, UnicodeError) as error:
    st.error(f"Unable to open students.csv: {error}")
    st.stop()

# ---------------- SIDEBAR FILTERS ----------------

st.sidebar.title("🔎 Dashboard Filters")

search_name = st.sidebar.text_input(
    "Search student",
    placeholder="Enter a student name"
)

available_grades = sorted(students["grade"].unique().tolist())

selected_grades = st.sidebar.multiselect(
    "Filter by grade",
    options=available_grades,
    default=available_grades
)

sort_option = st.sidebar.selectbox(
    "Sort students by",
    [
        "Highest total first",
        "Lowest total first",
        "Name A-Z",
        "Name Z-A"
    ]
)

# ---------------- APPLY FILTERS ----------------

filtered = students.copy()

if search_name.strip():
    filtered = filtered[
        filtered["name"].str.contains(
            search_name.strip(),
            case=False,
            regex=False,
            na=False
        )
    ]

filtered = filtered[filtered["grade"].isin(selected_grades)]

if sort_option == "Highest total first":
    filtered = filtered.sort_values(
        ["total", "name"],
        ascending=[False, True]
    )
elif sort_option == "Lowest total first":
    filtered = filtered.sort_values(
        ["total", "name"],
        ascending=[True, True]
    )
elif sort_option == "Name A-Z":
    filtered = filtered.sort_values("name")
else:
    filtered = filtered.sort_values("name", ascending=False)

# ---------------- CLASS OVERVIEW ----------------

st.header("📌 Class Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Students", len(students))
col2.metric("Class Average", f"{students['average'].mean():.2f}")
col3.metric("Highest Average", f"{students['average'].max():.2f}")
col4.metric("Lowest Average", f"{students['average'].min():.2f}")

st.caption(
    "Overview metrics use the full class. "
    "Tables and charts below use your selected filters."
)

st.divider()

# ---------------- STUDENT RANKINGS ----------------

st.header("🏆 Student Rankings")

if filtered.empty:
    st.warning("No students match the selected filters.")
else:
    ranking = filtered.sort_values(
        ["total", "name"],
        ascending=[False, True]
    ).copy()

    ranking.insert(
        0,
        "rank",
        range(1, len(ranking) + 1)
    )

    ranking = ranking.rename(
        columns={
            "rank": "Rank",
            "name": "Student",
            "subject1": "Subject 1",
            "subject2": "Subject 2",
            "subject3": "Subject 3",
            "total": "Total",
            "average": "Average",
            "grade": "Grade"
        }
    )

    st.dataframe(
        ranking,
        use_container_width=True,
        hide_index=True
    )

    csv_report = ranking.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Student Report (CSV)",
        data=csv_report,
        file_name="student_performance_report.csv",
        mime="text/csv"
    )

st.divider()

# ---------------- SUBJECT-WISE ANALYSIS ----------------

st.header("📚 Subject-wise Analysis")

subject_stats = pd.DataFrame({
    "Subject": ["Subject 1", "Subject 2", "Subject 3"],
    "Class Average": [
        students[subject].mean()
        for subject in SUBJECTS
    ],
    "Highest Mark": [
        students[subject].max()
        for subject in SUBJECTS
    ],
    "Lowest Mark": [
        students[subject].min()
        for subject in SUBJECTS
    ]
})

subject_stats["Class Average"] = subject_stats[
    "Class Average"
].round(2)

st.dataframe(
    subject_stats,
    use_container_width=True,
    hide_index=True
)

st.subheader("Class Average by Subject")

average_chart = subject_stats.set_index("Subject")[["Class Average"]]
st.bar_chart(average_chart)

st.divider()

# ---------------- STUDENT PERFORMANCE CHARTS ----------------

st.header("📈 Student Performance Charts")

if not filtered.empty:
    chart_data = filtered.set_index("name")[SUBJECTS].copy()

    chart_data.columns = [
        "Subject 1",
        "Subject 2",
        "Subject 3"
    ]

    st.subheader("Marks by Student and Subject")
    st.bar_chart(chart_data)

    st.subheader("Average Marks by Student")

    average_data = filtered.set_index("name")[["average"]].copy()
    average_data.columns = ["Average"]

    st.bar_chart(average_data)

    st.subheader("Grade Distribution")

    grade_counts = (
        filtered["grade"]
        .value_counts()
        .sort_index()
    )

    st.bar_chart(grade_counts)

else:
    st.info("Charts will appear when students match your filters.")

# ---------------- TOP PERFORMER ----------------

st.divider()
st.header("🥇 Top Performer")

top_student = students.sort_values(
    ["total", "name"],
    ascending=[False, True]
).iloc[0]

col1, col2, col3 = st.columns(3)

col1.metric("Student", top_student["name"])
col2.metric("Total Marks", f"{top_student['total']:.0f} / 300")
col3.metric("Average", f"{top_student['average']:.2f}")

st.write(f"**Grade:** {top_student['grade']}")

# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "Student Marks Analyzer | Python • Pandas • Streamlit"
)
