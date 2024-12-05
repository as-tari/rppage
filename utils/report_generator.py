import pandas as pd

def generate_report(page_counts):
    """
    Generate a report from the page counts.

    Args:
        page_counts (dict): Dictionary with chapter titles as keys and page counts as values.

    Returns:
        pd.DataFrame: DataFrame containing the report.
    """
    report_data = {
        'Chapter': list(page_counts.keys()),
        'Page Count': list(page_counts.values())
    }
    report_df = pd.DataFrame(report_data)
    return report_df
