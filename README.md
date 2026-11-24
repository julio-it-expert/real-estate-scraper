# Real Estate Data Pipeline 🚀

An enterprise-grade, modular web scraping architecture engineered in Python. This system parses complex DOM structures and automates data extraction, cleansing, and multi-format export pipelines using Pandas.

🔗 **[Live Interactive Demo — Try the Scraper App](https://real-estate-scraper-j.streamlit.app/)** *(Built with Streamlit)*

---

## 🛠️ Key Technical Features

* **Interactive Sandbox UI (`app.py`):** Features a cloud-hosted web interface allowing users to inspect raw HTML sources, execute the extraction engine in real time, and download structured reports directly from the browser.
* **Anti-Blocking System:** Simulates human behavior with randomized micro-delays (`time.sleep`) and dynamic HTTP header rotation using automated User-Agents.
* **Resilient Architecture:** Implements decoupled, standalone components for networking, DOM parsing, and data processing with fault-tolerant error handling (`try-except`) for incomplete listings.
* **Pandas Data Pipeline:** Executes financial field normalization (currency and numeric cleansing), handles missing data safely without crashing, and exports concurrently into Excel (`.xlsx`) and `.csv` formats.

---

## 📁 Project Structure

```text
├── core/
│   ├── network.py       # Handles secure HTTP requests and User-Agent rotation
│   ├── parser.py        # Extracts real estate fields from target DOM using BeautifulSoup4 & Regex
│   └── pipeline.py      # Pandas transformations and concurrent Excel/CSV exporting
├── mocks/               # Offline HTML sandbox fixtures for deterministic testing
├── data/                # Local directory for structured file persistence (git-ignored)
├── app.py               # Interactive Streamlit web dashboard for live portfolio demonstration
├── main.py              # CLI orchestrator for automated pipeline execution and logging
├── requirements.txt     # Project dependencies
└── README.md
```

---

## ⚙️ Installation & Local Usage

1. **Clone this repository:**
   ```bash
   git clone https://github.com/julio-it-expert/real-estate-scraper.git
   cd real-estate-scraper

   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   * **Option A — Interactive Web UI (Recommended):**
     ```bash
     streamlit run app.py
     ```
   * **Option B — Command-Line Pipeline (CLI):**
     ```bash
     python main.py
     ```
