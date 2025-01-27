# UVU Computer Science Programs Analyzer

A web scraping tool and comprehensive guide for Utah Valley University's Computer Science programs, including career prospects and salary information.

## Overview

This project provides:
1. A Python-based web scraper to collect program information from UVU's CS department
2. A comprehensive markdown guide about each CS program
3. Up-to-date career and salary information for each program
4. Industry insights about the tech sector in Utah and nationwide

## Features

- Automated scraping of program information
- Detailed program descriptions and requirements
- Career prospects and salary data
- Industry insights and job market analysis
- Clean, formatted markdown output

## Requirements

- Python 3.7+
- Required packages:
  ```
  requests==2.31.0
  beautifulsoup4==4.12.2
  ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/uvu-cs-programs-analyzer.git
   cd uvu-cs-programs-analyzer
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the scraper:
```bash
python uvu_cs_scraper.py
```

This will:
1. Scrape information from UVU's CS department website
2. Generate a comprehensive markdown document (`uvu_cs_programs_guide.md`)
3. Include career prospects and salary information

## Output

The script generates a detailed markdown file (`uvu_cs_programs_guide.md`) containing:
- Program descriptions
- Degree requirements
- Career opportunities
- Salary information
- Industry insights
- Contact information

## Project Structure

```
uvu-cs-programs-analyzer/
├── README.md
├── requirements.txt
├── uvu_cs_scraper.py
└── uvu_cs_programs_guide.md
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Utah Valley University Computer Science Department
- Bureau of Labor Statistics for career data
- Industry salary data sources

## Contact

For questions or feedback, please open an issue in the GitHub repository.
