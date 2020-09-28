from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, date


    
class Parameter(BaseModel):
    recognite_process_id: int
    source_topic: str
    destination_topic: str
    source_servers: list = [str]
    destination_servers: list = [str]