# Warning control
import warnings
warnings.filterwarnings('ignore')

from crewai import Agent, Crew, Task
import os
from utils import get_openai_api_key
from dotenv import load_dotenv

# Load environment variables
load_dotenv() # This will load the SERPER_API_KEY from .env

openai_api_key = get_openai_api_key()
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o-mini'

# Import required tools
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

# Agent 1: Venue Coordinator
venue_coordinator = Agent(
    role="Venue Coordinator",
    goal="Identify and book PROFESSIONAL venues specifically designed for tech conferences, startup meetups, and business events",
    tools=[search_tool, scrape_tool],
    verbose=True,
    backstory=(
        "You are a specialized venue coordinator with expertise in tech and startup events. "
        "You ONLY work with professional venues: conference centers, tech hubs, innovation centers, "
        "co-working spaces with event facilities, university tech centers, and business centers. "
        "You NEVER recommend bars, restaurants, or casual venues for professional events. "
        "You understand the specific needs of AI/tech meetups: proper AV equipment, presentation facilities, "
        "networking areas, and professional meeting rooms. Your reputation depends on finding "
        "legitimate, professional venues that meet the highest standards for business events."
    )
)

# Agent 2: Logistics Manager
logistics_manager = Agent(
    role='Logistics Manager',
    goal=(
        "Manage all logistics for the event "
        "including catering and equipment"
    ),
    tools=[search_tool, scrape_tool],
    verbose=True,
    backstory=(
        "Organized and detail-oriented, "
        "you ensure that every logistical aspect of the event "
        "from catering to equipment setup "
        "is flawlessly executed to create a seamless experience."
    )
)

# Agent 3: Marketing and Communications Agent
marketing_communications_agent = Agent(
    role="Marketing and Communications Agent",
    goal="Effectively market the event and "
         "communicate with participants",
    tools=[search_tool, scrape_tool],
    verbose=True,
    backstory=(
        "Creative and communicative, "
        "you craft compelling messages and "
        "engage with potential attendees "
        "to maximize event exposure and participation."
    )
)

from pydantic import BaseModel

# Define a Pydantic model for venue details 
# (demonstrating Output as Pydantic)
class VenueDetails(BaseModel):
    name: str
    address: str
    capacity: int
    booking_status: str

venue_task = Task(
    description=(
        "Find a PROFESSIONAL venue in {event_city} specifically designed for "
        "tech conferences, startup meetups, and business events. "
        "The venue must be suitable for an AI startup meetup with {expected_participants} participants. "
        "Focus on: conference centers, tech hubs, co-working spaces with event facilities, "
        "university innovation centers, or professional business centers. "
        "AVOID bars, restaurants, or casual venues. "
        "The venue should have proper AV equipment, presentation facilities, "
        "networking areas, and professional meeting rooms. "
        "Search for venues like 'Stockholm Tech Hub', 'Innovation Center', "
        "'Conference Center', 'Business Center', 'Tech Campus', etc."
    ),
    expected_output=(
        "A professional venue specifically chosen for tech/startup events with: "
        "proper name, full address, realistic capacity (minimum {expected_participants}), "
        "and confirmed availability. Must be a legitimate business venue, not a casual establishment."
    ),
    human_input=True,
    output_json=VenueDetails,
    output_file="venue_details.json",
    agent=venue_coordinator
)

logistics_task = Task(
    description="Coordinate catering and "
                "equipment for an event "
                "with {expected_participants} participants "
                "on {tentative_date}.",
    expected_output="Confirmation of all logistics arrangements "
                    "including catering and equipment setup.",
    human_input=True,
    async_execution=True,
    agent=logistics_manager
)

marketing_task = Task(
    description="Promote the {event_topic} "
                "aiming to engage at least "
                "{expected_participants} potential attendees.",
    expected_output="Report on marketing activities "
                    "and attendee engagement formatted as markdown.",
    async_execution=True,
    output_file="marketing_report.md",  # Outputs the report as a text file
    agent=marketing_communications_agent
)

# Define the crew with agents and tasks
event_management_crew = Crew(
    agents=[venue_coordinator, 
            logistics_manager, 
            marketing_communications_agent],
    
    tasks=[venue_task, 
           logistics_task, 
           marketing_task],
    
    verbose=True
)

event_details = {
    'event_topic': "AI Startup Meetup",
    'event_description': "A gathering of AI startups "
                         "and people interested in creating one ",
    'event_city': "Stockholm",
    'tentative_date': "2025-09-15",
    'expected_participants': 100,
    'budget': 50000,
    'venue_type': "Conference Hall"
}

# Import required modules for file output
import os
from datetime import datetime

# Create outputs directory if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Execute the crew and wait for completion
result = event_management_crew.kickoff(inputs=event_details)

# Wait for the crew to fully complete, then save the final result
print("\n🔄 Crew execution completed. Processing final result...")

# Generate filename with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"outputs/event_planning_result_{timestamp}.md"

# Save the FINAL result as Markdown (after all agents complete)
with open(filename, "w", encoding="utf-8") as f:
    f.write("# Event Planning Crew Result\n\n")
    f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    f.write("---\n\n")
    f.write("## Event Planning Summary\n\n")
    f.write("This result has been generated by the Venue Coordinator, Logistics Manager, and Marketing Communications Agent.\n\n")
    f.write("---\n\n")
    f.write(result)

print(f"\n✅ FINAL RESULT saved as Markdown file: {filename}")
print("📋 This file contains the complete event planning result after all agents completed their tasks.")

# Also try IPython display if available
try:
    from IPython.display import Markdown
    Markdown(result)
except ImportError:
    print("IPython display not available, final result saved as Markdown above")

# Read and display venue details from JSON file
import json
from pprint import pprint

try:
    with open('venue_details.json') as f:
        data = json.load(f)
    print("\n📋 Venue Details:")
    pprint(data)
except FileNotFoundError:
    print("\n⚠️  Venue details file not found yet")

# Try to read and display marketing report
try:
    with open('marketing_report.md', 'r') as f:
        marketing_content = f.read()
    print(f"\n📋 Marketing Report Content:\n{marketing_content}")
except FileNotFoundError:
    print("\n⚠️  Marketing report file not found yet")
