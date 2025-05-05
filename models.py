from typing import List, Optional

from pydantic import BaseModel

class JobRequest(BaseModel):
    user_query: str

class JobSearchFilters(BaseModel):
    industries: List[str]
    locations: List[str]
    salary_expectation_min: Optional[int]
    funding_stage: List[str]
    days_ago: Optional[int]

class JobDetail(BaseModel):
    job_id: int
    job_title: str
    company: str
    job_description: str
    industry: Optional[str] = None
    location: Optional[str] = None
    funding_stage: Optional[str] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    distance: Optional[float] = None

class JobSearchResponse(BaseModel):
    job_details: List[JobDetail]
    filters: Optional[JobSearchFilters] = None