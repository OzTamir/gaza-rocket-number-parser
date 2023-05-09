# gaza-rocket-number-parser
Parse the number of rockets from Gaza into CSV files by year

This Python script downloads a website and extracts tables as CSV files. The script uses the content of the preceding `h3` tag as the CSV file name.

## Prerequisites

Make sure you have Python 3.x installed on your system. You also need the following libraries:

- requests
- beautifulsoup4

## Installation

1. Clone the repository or download the source code.

2. Install the required libraries by running the following command in your terminal or command prompt:

```bash
pip install -r requirements.txt
```

## Usage
1. Run the script:

```bash
python rocket_parser.py
```

The script will download the site content, extract the tables, and save them as CSV files with the content of the preceding `h3` tags as file names.

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for more details.