# Streamlit Dashboards

## App structure
Streamlit turns a Python script into an interactive web app. Widgets return user selections; Streamlit reruns the script when a widget changes. Use caching for expensive deterministic work, not for user-specific secrets.

## Dashboard workflow
1. Define the audience and decisions the dashboard supports.
2. Load and validate data.
3. Add filters and meaningful summary metrics.
4. Visualize trends and comparisons.
5. Explain missing data and limitations.
6. Test empty selections, invalid uploads, and large inputs.

## Good practice
Use clear labels, avoid misleading axes, display units and date ranges, and separate raw data from calculated metrics. Do not upload sensitive data without permission. Keep secrets in environment variables or Streamlit secrets rather than source files.

## Run
Install with `python -m pip install streamlit pandas`. Save the example and run `streamlit run examples/02_dashboard.py`.
