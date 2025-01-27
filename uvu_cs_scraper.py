import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import re

def get_base_program_details():
    """Returns the base dictionary of program details"""
    return {
        "Computational Data Science": {
            "degree_type": "Bachelor of Science",
            "department": "Computer Science",
            "key_areas": [
                "Mathematics",
                "Statistics",
                "Database Theory",
                "Causal Inference",
                "Data Visualization",
                "Machine Learning",
                "Artificial Intelligence"
            ],
            "career_paths": [
                "Data Scientist",
                "Machine Learning Engineer",
                "Data Analyst",
                "AI Researcher"
            ]
        },
        "Computer Science": {
            "degree_type": "Bachelor of Science",
            "department": "Computer Science",
            "key_areas": [
                "Software Development",
                "Computer Theory",
                "Artificial Intelligence",
                "Programming",
                "Computer Engineering",
                "Robotics",
                "Game Development"
            ],
            "career_paths": [
                "Software Engineer",
                "AI Developer",
                "Game Developer",
                "Robotics Engineer",
                "Systems Architect"
            ]
        },
        "Computer Science Education": {
            "degree_type": "Bachelor of Science",
            "department": "Computer Science",
            "key_areas": [
                "Software Development",
                "Web Development",
                "Education Principles",
                "Teaching Methods",
                "Curriculum Development"
            ],
            "career_paths": [
                "Secondary Education Teacher",
                "Computer Science Teacher",
                "Web Development Instructor",
                "Educational Technology Specialist"
            ]
        },
        "Master of Computer Science": {
            "degree_type": "Master's Degree",
            "department": "Computer Science",
            "key_areas": [
                "Cybersecurity Operations",
                "Law and Ethics",
                "Privacy in Cybersecurity",
                "Penetration Testing",
                "Vulnerability Assessment",
                "Network Defense",
                "Risk Management"
            ],
            "career_paths": [
                "Cybersecurity Specialist",
                "Security Analyst",
                "Security Engineer",
                "Risk Manager",
                "Security Consultant"
            ]
        },
        "Software Development": {
            "degree_type": "Bachelor of Science",
            "department": "Computer Science",
            "key_areas": [
                "Software Development",
                "Programming",
                "Agile Methodologies",
                "Scrum",
                "Quality Assurance",
                "Team Collaboration"
            ],
            "career_paths": [
                "Software Developer",
                "Application Developer",
                "Quality Assurance Engineer",
                "Software Development Team Lead"
            ]
        },
        "Software Engineering": {
            "degree_type": "Bachelor of Science",
            "department": "Computer Science",
            "key_areas": [
                "Large-scale Software Systems",
                "Software Architecture",
                "Project Management",
                "Agile Development",
                "Team Leadership",
                "System Design"
            ],
            "career_paths": [
                "Software Engineer",
                "Software Architect",
                "Technical Lead",
                "Project Manager",
                "Development Manager"
            ]
        }
    }

def get_page_content(url, headers):
    """Fetch page content with error handling and rate limiting"""
    try:
        time.sleep(1)  # Rate limiting
        response = requests.get(url if url.startswith('http') else f"https://www.uvu.edu{url}", headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def get_salary_data():
    """Returns salary and job market data for CS-related careers"""
    return {
        "Computational Data Science": {
            "median_salary": "$108,000",
            "salary_range": "$85,000 - $150,000",
            "job_growth": "36% (Much faster than average)",
            "top_employers": ["Amazon", "Google", "Microsoft", "Meta", "Financial Institutions"],
            "job_titles": ["Data Scientist", "ML Engineer", "AI Researcher", "Data Analyst"],
            "industry_demand": "Very High"
        },
        "Computer Science": {
            "median_salary": "$105,000",
            "salary_range": "$75,000 - $160,000",
            "job_growth": "25% (Much faster than average)",
            "top_employers": ["Tech Companies", "Software Firms", "Research Labs", "Government"],
            "job_titles": ["Software Engineer", "Systems Architect", "AI Developer"],
            "industry_demand": "Very High"
        },
        "Computer Science Education": {
            "median_salary": "$75,000",
            "salary_range": "$55,000 - $95,000",
            "job_growth": "12% (Faster than average)",
            "top_employers": ["K-12 Schools", "Technical Schools", "Educational Technology Companies"],
            "job_titles": ["CS Teacher", "Educational Technology Specialist", "Curriculum Developer"],
            "industry_demand": "High"
        },
        "Master of Computer Science": {
            "median_salary": "$131,500",
            "salary_range": "$95,000 - $185,000",
            "job_growth": "31% (Much faster than average)",
            "top_employers": ["Major Tech Companies", "Research Institutions", "Government Agencies"],
            "job_titles": ["Senior Software Engineer", "Research Scientist", "Technical Architect"],
            "industry_demand": "Very High"
        },
        "Software Development": {
            "median_salary": "$98,000",
            "salary_range": "$70,000 - $140,000",
            "job_growth": "26% (Much faster than average)",
            "top_employers": ["Software Companies", "Tech Startups", "Enterprise IT"],
            "job_titles": ["Software Developer", "Application Developer", "Full-stack Developer"],
            "industry_demand": "Very High"
        },
        "Software Engineering": {
            "median_salary": "$115,000",
            "salary_range": "$85,000 - $170,000",
            "job_growth": "28% (Much faster than average)",
            "top_employers": ["Tech Giants", "Defense Contractors", "Financial Services"],
            "job_titles": ["Software Engineer", "Systems Architect", "Technical Lead"],
            "industry_demand": "Very High"
        }
    }

def clean_text(text):
    """Clean and normalize text content"""
    if not text:
        return ""
    # Remove extra whitespace
    text = ' '.join(text.split())
    # Remove common navigation/footer items
    remove_items = ['Admissions', 'Campus Life', 'Current Student', 'Athletics', 
                   'Contact Us', 'Privacy Statement', 'Terms of Use', '© Utah Valley University']
    for item in remove_items:
        text = text.replace(item, '')
    return text.strip()

def extract_program_details(soup):
    """Extract relevant program details from the program page"""
    details = {
        'courses': [],
        'requirements': [],
        'learning_outcomes': [],
        'additional_info': []
    }
    
    # Look for course information
    course_sections = soup.find_all(['div', 'section'], string=lambda x: x and any(word in x.lower() for word in ['course', 'curriculum', 'classes']))
    for section in course_sections:
        courses = section.find_all(['li', 'p'])
        for course in courses:
            course_text = clean_text(course.get_text())
            if course_text and len(course_text) > 10:  # Filter out short texts
                details['courses'].append(course_text)
    
    # Look for program requirements
    req_sections = soup.find_all(['div', 'section'], string=lambda x: x and 'requirement' in x.lower())
    for section in req_sections:
        reqs = section.find_all(['li', 'p'])
        for req in reqs:
            req_text = clean_text(req.get_text())
            if req_text and len(req_text) > 10:
                details['requirements'].append(req_text)
    
    # Look for learning outcomes
    outcome_sections = soup.find_all(['div', 'section'], string=lambda x: x and any(word in x.lower() for word in ['outcome', 'learn', 'skill', 'objective']))
    for section in outcome_sections:
        outcomes = section.find_all(['li', 'p'])
        for outcome in outcomes:
            outcome_text = clean_text(outcome.get_text())
            if outcome_text and len(outcome_text) > 10:
                details['learning_outcomes'].append(outcome_text)
    
    # Look for additional relevant information
    for p in soup.find_all('p'):
        text = clean_text(p.get_text())
        if text and len(text) > 50 and not any(text in item for item in details['courses'] + details['requirements'] + details['learning_outcomes']):
            details['additional_info'].append(text)
    
    return details

def scrape_uvu_cs_programs():
    base_url = "https://www.uvu.edu/cs/degrees/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        main_content = get_page_content(base_url, headers)
        if not main_content:
            return []
        
        soup = BeautifulSoup(main_content, 'html.parser')
        programs = []
        program_details = get_base_program_details()
        
        # Find all program sections
        for name in program_details.keys():
            section = soup.find('h2', string=lambda x: x and name in x)
            if section:
                print(f"\nProcessing program: {name}")
                
                # Get the description from the next paragraph
                description = ""
                next_p = section.find_next('p')
                if next_p:
                    description = next_p.text.strip()
                
                # Get the view link
                view_link = None
                next_a = section.find_next('a')
                if next_a and 'View' in next_a.text:
                    view_link = next_a.get('href', '')
                    print(f"Found program link: {view_link}")
                
                program_info = {
                    'name': name,
                    'description': description,
                    'link': view_link,
                    'degree_type': program_details[name]['degree_type'],
                    'department': program_details[name]['department'],
                    'key_areas': program_details[name]['key_areas'],
                    'career_paths': program_details[name]['career_paths']
                }
                
                # Fetch additional details from program page
                if view_link:
                    print(f"Fetching additional details from {view_link}")
                    program_page_content = get_page_content(view_link, headers)
                    if program_page_content:
                        program_soup = BeautifulSoup(program_page_content, 'html.parser')
                        additional_details = extract_program_details(program_soup)
                        program_info.update(additional_details)
                
                programs.append(program_info)
                print(f"Successfully processed {name}")
        
        return programs
    
    except Exception as e:
        print(f"Error in scraping: {e}")
        return []

def create_knowledge_base(programs):
    content_parts = []
    salary_data = get_salary_data()
    
    # Header
    content_parts.extend([
        "# UVU Computer Science Programs - Comprehensive Guide",
        f"Last Updated: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "## Introduction",
        "This comprehensive guide provides detailed information about the Computer Science programs offered at Utah Valley University, including program details, career prospects, and salary information. The data is compiled from UVU's official resources and industry statistics.",
        "",
        "## Table of Contents",
        generate_toc(programs),
        "",
        "## Quick Facts - Computer Science at UVU",
        "- Located in the heart of Utah's Silicon Slopes",
        "- ABET-accredited programs",
        "- Strong industry connections",
        "- Modern curriculum aligned with industry needs",
        "- Hands-on learning opportunities",
        ""
    ])
    
    # Programs
    for program in programs:
        name = program['name']
        salary_info = salary_data.get(name, {})
        
        content_parts.extend([
            f"## {name}",
            "",
            "### Program Overview",
            f"**Degree Type:** {program['degree_type']}",
            f"**Department:** {program['department']}",
            "",
            "### Description",
            program['description'] if program['description'] else "A comprehensive program preparing students for careers in computing and technology.",
            "",
            "### Career Prospects",
            f"- **Median Salary:** {salary_info.get('median_salary', 'Varies by position and location')}",
            f"- **Salary Range:** {salary_info.get('salary_range', 'Varies by experience and location')}",
            f"- **Job Growth:** {salary_info.get('job_growth', 'Data not available')}",
            f"- **Industry Demand:** {salary_info.get('industry_demand', 'High')}",
            "",
            "### Top Employers",
            *[f"- {employer}" for employer in salary_info.get('top_employers', [])],
            "",
            "### Common Job Titles",
            *[f"- {title}" for title in salary_info.get('job_titles', [])],
            "",
            "### Key Areas of Study",
            *[f"- {area}" for area in program['key_areas']],
            ""
        ])
        
        if program.get('courses'):
            content_parts.extend([
                "### Core Courses",
                *[f"- {course}" for course in program['courses']],
                ""
            ])
        
        if program.get('learning_outcomes'):
            content_parts.extend([
                "### Learning Outcomes",
                *[f"- {outcome}" for outcome in program['learning_outcomes']],
                ""
            ])
        
        if program.get('requirements'):
            content_parts.extend([
                "### Program Requirements",
                *[f"- {req}" for req in program['requirements']],
                ""
            ])
        
        if program.get('additional_info'):
            content_parts.extend([
                "### Additional Information",
                *[info for info in program['additional_info'] if len(info) > 50],
                ""
            ])
        
        content_parts.extend(["---", ""])
    
    # Industry Insights
    content_parts.extend([
        "## Industry Insights",
        "",
        "### Utah's Silicon Slopes",
        "- Utah's tech sector is growing rapidly, with many opportunities for CS graduates",
        "- Major tech companies have established offices in the region",
        "- Strong startup ecosystem with numerous opportunities",
        "- High demand for software developers and data scientists",
        "",
        "### National Trends",
        "- Computing occupations are among the fastest-growing job categories",
        "- Continued growth in AI, machine learning, and data science",
        "- Increasing demand for cybersecurity professionals",
        "- Remote work opportunities expanding the job market",
        "",
        "## Contact Information",
        "- Department: Computer Science",
        "- Email: [cs@uvu.edu](mailto:cs@uvu.edu)",
        "- Phone: (801) 863-8218",
        "- Location: Room CS-520",
        "",
        "## Additional Resources",
        "- [UVU Admissions](https://www.uvu.edu/admissions/)",
        "- [Financial Aid](https://www.uvu.edu/financialaid/)",
        "- [Career Services](https://www.uvu.edu/careers/)",
        "- [Computer Science Department](https://www.uvu.edu/cs/)",
        ""
    ])
    
    # Write to file
    with open('uvu_cs_programs_guide.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(content_parts))

def generate_toc(programs):
    toc_lines = []
    for idx, program in enumerate(programs, 1):
        link = program['name'].lower().replace(' ', '-')
        toc_lines.append(f"{idx}. [{program['name']}](#{link})")
    return '\n'.join(toc_lines)

def main():
    print("Scraping UVU CS program information...")
    programs = scrape_uvu_cs_programs()
    
    if programs:
        print("\nCreating knowledge base document...")
        create_knowledge_base(programs)
        print("Knowledge base created successfully: uvu_cs_programs_guide.md")
        print(f"Documented {len(programs)} programs with detailed information")
    else:
        print("No program information was found.")

if __name__ == "__main__":
    main() 