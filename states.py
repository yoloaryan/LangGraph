#so now we are creating a graph
# and first thing you create is a state

from pydantic import dataclasses
import os

#1) typed DICT. -> for creating the state
#this is most common approach

from typing import TypedDict


class State(TypedDict):
    topic: str
    summary: str
    score: int


#2 pydantic approach
#it is a good at data visualization and type checking at
#runtime

from pydantic import BaseModel, field_validator


class State(BaseModel):
    topic: str
    summary: str = ""
    score: int

    @field_validator
    def score_positive(cls, v):
        if v < 0:
            raise ValueError("score must be positive")


#python datasclasses
# standard python dataclass but it is used very rarelty

from dataclasses import dataclass, field


@dataclass
class State:
    topic: str = ""
    summary: str = ""
    messages: list = field(default_factory=list)


#3) dataclss approach
