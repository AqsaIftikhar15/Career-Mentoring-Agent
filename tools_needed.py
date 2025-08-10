from openai import function_tool
from pydantic import BaseModel


class CareerInput(BaseModel):
    route: str 

@function_tool
def get_career_roadmap(inputCareerInput) -> str:
    {
    """
Provide a comprehensive and structured career roadmap for the given professional role.

As an intelligent agent, you must dynamically generate the roadmap based on current industry trends, market demand, essential skills, learning resources, and practical experience required.

Your response should include:
- A brief overview of the role and its importance in today’s job market
- Prerequisite knowledge or background needed (if any)
- Essential skills to learn (categorized: technical, soft, business, etc.)
- Recommended tools, frameworks, or platforms used in this role
- Certifications, courses, or platforms to learn from (optional but helpful)
- Entry-level positions or internships to target
- Mid-level growth path (roles, responsibilities, specialization options)
- Senior-level progression (leadership tracks, cross-functional roles, advanced domains)
- Bonus: Mention trends or technologies shaping the future of this career path

Ensure the roadmap is:
- Updated and relevant to the current market
- Practical and achievable for someone beginning the journey
- Clearly structured in steps or stages
- Based on your own reasoning, not from any static, preloaded dataset

Avoid repeating generic advice — tailor your roadmap specifically for the provided career route."""}
    return f"Generating roadmap for: {input.route}"



