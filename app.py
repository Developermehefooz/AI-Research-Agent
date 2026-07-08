from flask import Flask, render_template, request, send_file

from utils.search import search_web
from utils.scraper import extract_content
from utils.summarizer import generate_report
from utils.database import (
    initialize_database,
    save_research,
    get_all_research
)
from utils.pdf_generator import create_pdf

app = Flask(__name__)

# Initialize database
initialize_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/research", methods=["POST"])
def research():

    topic = request.form.get("topic")

    if not topic:
        return render_template(
            "index.html",
            error="Please enter a research topic."
        )

    try:

        # Search web
        urls = search_web(topic)

        print("\n========== SEARCH RESULTS ==========")
        print("Topic:", topic)
        print("URLs Found:", urls)

        if not urls:
            return render_template(
                "index.html",
                error="No sources found for this topic."
            )

        combined_text = ""

        # Extract content
        for url in urls:

            try:

                content = extract_content(url)

                print(
                    f"Extracted {len(content) if content else 0} characters from:",
                    url
                )

                if content:
                    combined_text += content + "\n\n"

            except Exception as scrape_error:

                print(
                    "Scraping Error:",
                    scrape_error
                )

        print(
            "Total Text Length:",
            len(combined_text)
        )

        if not combined_text.strip():

            return render_template(
                "index.html",
                error="Could not collect enough research data."
            )

        # Generate AI Report
        report = generate_report(
            topic,
            combined_text
        )

        # Save to database
        save_research(
            topic,
            report
        )

        return render_template(
            "index.html",
            topic=topic,
            report=report,
            sources=urls
        )

    except Exception as e:

        print("Research Error:", e)

        return render_template(
            "index.html",
            error=f"Error: {str(e)}"
        )


@app.route("/history")
def history():

    records = get_all_research()

    return render_template(
        "history.html",
        records=records
    )


@app.route("/download", methods=["POST"])
def download():

    topic = request.form.get("topic")

    report = request.form.get("report")

    pdf_file = create_pdf(
        topic,
        report
    )

    return send_file(
        pdf_file,
        as_attachment=True,
        download_name=f"{topic}_report.pdf"
    )


if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )