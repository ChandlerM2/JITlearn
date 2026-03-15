# Just in time learning system

## what this project does

It seems that LLM's are only as good as the person who uses them. In order to get better responses and eventually guide agents a person must learn the material.

This tool does semantic search on books in your collection, as well as the past 3 months on the internet, to help your AI agent or LLM respond with where to find the information (as well as what the information is). If it's a foundational concept and we have a book the LLM will point us to the books subjections and pages, but if that tool or technique is obsolete it uses the internet search and gives resources. 

Basicly, the LLM / agent takes the question query, compacts it, then searches for relevant and new sources so the user can learn the skills just in time for the project.

This idea hinges on the phycology that the brain tends to remember solutions to pain rather than passive learning.

## Tech stack

- Python version 3.13: scripting
- ChromeDB: vector database
- ChromeDB: Normal Database
- MCP tooling
- Server?


## How to set it up on a new machine

Download uv through pip install uv if you don't have it.. then in the terminal do UV sync to download all dependencies

run the embedding model on your computer and then connect it with the MCP tool

## What goes in the data folder

the chromaDB or csv file 

## Data format

"AI", "MATH", "ROBOTICS", "SAFETY", "DATA_ENG", "FINANCE", "COMPSCI", "PHILOSOPHY", "ML", "DS"