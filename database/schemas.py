from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, date

""" For base database """
    
class Cluster(BaseModel):
    id: int
    name: str
    description: str


class Broker(BaseModel):
    id: int
    cluster_id: int
    name: str
    server: str
    description: str
    

class Topic(BaseModel):
    id: int
    name: str
    cluster_id: int
    description: str
    

""" For recognite database """

class Recognite(BaseModel):
    id: int
    name: str
    source_topic: int
    destination_topic: int
    
    
    
    