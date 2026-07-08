from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

import os


def create_pdf(topic, report):

    # Create reports folder if it doesn't exist
    if not os.path.exists("reports"):
        os.makedirs("reports")

    filename = f"reports/{topic.replace(' ', '_')}.pdf"

    document = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    # Title
    title = Paragraph(
        f"Research Report: {topic}",
        styles["Title"]
    )

    content.append(title)

    content.append(
        Spacer(1, 12)
    )

    # Report Content
    report_text = Paragraph(
        report.replace("\n", "<br/>"),
        styles["BodyText"]
    )

    content.append(report_text)

    # Build PDF
    document.build(content)

    return filename