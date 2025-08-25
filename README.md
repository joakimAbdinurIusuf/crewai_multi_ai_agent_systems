# Multi-AI Agents Project with CrewAI

A comprehensive Python project demonstrating advanced AI agent orchestration using CrewAI framework. This project showcases multiple specialized AI crews working together to solve complex business problems across various domains.

## 🚀 Project Overview

This repository demonstrates the power of AI agent collaboration through five distinct crews, each designed to tackle specific business challenges:

### 1. **Research & Content Creation Crew** (`research_crew.py`)
- **Purpose**: Automated content research, planning, and creation
- **Agents**: Content Planner, Content Writer, Editor
- **Output**: Comprehensive blog posts with research-backed content
- **Use Case**: Content marketing, research documentation, thought leadership

### 2. **Customer Outreach Crew** (`customer_outreach_crew.py`)
- **Purpose**: Lead generation and personalized customer outreach
- **Agents**: Sales Representative, Lead Sales Representative
- **Output**: Targeted email campaigns and lead nurturing strategies
- **Use Case**: B2B sales, lead generation, customer relationship management

### 3. **Customer Support Crew** (`customer_support_crew.py`)
- **Purpose**: Automated customer support and issue resolution
- **Agents**: Senior Support Representative, Support Quality Assurance Specialist
- **Output**: Comprehensive support responses with quality assurance
- **Use Case**: Customer service automation, support ticket resolution

### 4. **Event Planning Crew** (`event_planning_crew.py`)
- **Purpose**: Professional event coordination and logistics management
- **Agents**: Venue Coordinator, Logistics Manager, Marketing & Communications Agent
- **Output**: Complete event plans with venue details and logistics
- **Use Case**: Conference planning, corporate events, startup meetups

### 5. **Financial Analysis Crew** (`financial_analysis_crew.py`)
- **Purpose**: Real-time financial market analysis and trading strategy development
- **Agents**: Data Analyst, Trading Strategy Developer, Trade Advisor, Risk Advisor
- **Output**: Comprehensive financial reports with risk analysis and trading strategies
- **Use Case**: Investment analysis, trading strategy development, risk management

## 📊 Sample Outputs

The `outputs/` directory contains real examples of each crew's work:

- **`ai_blog_post_v2.md`**: Comprehensive AI blog post (9KB) covering AI trends, applications, and future implications
- **`customer_outreach_result_*.md`**: Personalized email campaigns for B2B sales outreach
- **`customer_support_result_*.md`**: Detailed support responses with quality assurance
- **`event_planning_result_*.md`**: Professional venue recommendations and event logistics
- **`financial_analysis_result_*.md`**: Risk analysis reports with trading strategies and mitigation plans

## 🛠️ Technical Architecture

- **Framework**: CrewAI for multi-agent orchestration
- **AI Models**: OpenAI GPT-4o-mini integration
- **Tools**: Web scraping, search APIs, sentiment analysis
- **Output Formats**: Markdown, JSON, structured data
- **Process Management**: Sequential and hierarchical agent workflows

## 🚀 Setup Guide

1. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key:**
   
   Create a `.env` file in your project directory with:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_MODEL_NAME=gpt-4o-mini
   ```
   
   Or set it as an environment variable:
   ```bash
   export OPENAI_API_KEY=your_openai_api_key_here
   ```

## 💡 Usage Examples

### Run Research Crew
```bash
python research_crew.py
```

### Run Customer Outreach Crew
```bash
python customer_outreach_crew.py
```

### Run Customer Support Crew
```bash
python customer_support_crew.py
```

### Run Event Planning Crew
```bash
python event_planning_crew.py
```

### Run Financial Analysis Crew
```bash
python financial_analysis_crew.py
```

## 🔧 Requirements

- Python 3.8+
- OpenAI API key
- Internet connection for API calls and web scraping
- Additional API keys for enhanced functionality (Serper API for search)

## 🌟 Key Features

- **Multi-Agent Collaboration**: Agents work together with defined roles and responsibilities
- **Real-time Data Integration**: Web scraping and search APIs for current information
- **Quality Assurance**: Multi-stage review processes for output validation
- **Flexible Output Formats**: Support for markdown, JSON, and structured data
- **Professional Use Cases**: Real-world business applications across multiple domains

## 🎯 Business Value

This project demonstrates:
- **AI Orchestration**: Complex multi-agent workflows for business automation
- **Domain Expertise**: Specialized AI agents for specific business functions
- **Scalability**: Framework that can be extended to new use cases
- **Quality Control**: Built-in validation and review processes
- **Integration**: Seamless integration with external APIs and data sources

## 📈 Potential Applications

- **Marketing Automation**: Content creation and customer outreach
- **Customer Service**: Automated support with human-like interaction
- **Event Management**: End-to-end event planning and coordination
- **Financial Services**: Market analysis and trading strategy development
- **Research & Development**: Automated research and documentation
- **Sales Operations**: Lead generation and customer relationship management

---

*This project showcases advanced AI agent orchestration capabilities and demonstrates practical applications of AI in business automation and decision-making processes.*
