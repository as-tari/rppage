def count_pages_for_chapters(chapters, text):
    """
    Count the number of pages for each chapter.

    Args:
        chapters (list): List of chapter titles.
        text (str): Text content of the Word document.

    Returns:
        dict: Dictionary with chapter titles as keys and page counts as values.
    """
    page_counts = {}
    current_chapter = None
    page_count = 0
    for line in text.split('\n'):
        if line in chapters:
            if current_chapter:
                page_counts[current_chapter] = page_count
            current_chapter = line
            page_count = 0
        else:
            page_count += 1
    if current_chapter:
        page_counts[current_chapter] = page_count
    return page_counts
