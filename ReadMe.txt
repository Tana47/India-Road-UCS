=============================================================================
              INDIAN CITIES ROUTE PLANNER (UNIFORM-COST SEARCH)
=============================================================================

DESCRIPTION
-----------------------------------------------------------------------------
This project implements Uniform-Cost Search (Dijkstra's Algorithm) to find 
the shortest road distance between various cities in India. The algorithm 
evaluates the path cost from the start node to the current node to guarantee 
the shortest route. It reads an open-source CSV dataset and processes the 
graph using Python's heapq module for efficiency.

PREREQUISITES
-----------------------------------------------------------------------------
- Python 3.x
- pandas module

SETUP INSTRUCTIONS
-----------------------------------------------------------------------------
1. Install pandas if you haven't already:
   pip install pandas

2. Ensure that "indian-cities-dataset.csv" is placed in the exact same 
   folder as your Python script.

HOW TO RUN
-----------------------------------------------------------------------------
1. Open your terminal or command prompt.
2. Change your directory to the folder containing the script.
3. Execute the script by typing: python program.py
4. Follow the on-screen prompts to enter your start and target cities. 
   (Input is case-insensitive).

EXAMPLE
-----------------------------------------------------------------------------
Enter the starting city: mumbai
Enter the destination city: chennai

Optimal Route from Mumbai to Chennai:
Mumbai -> Pune -> Bangalore -> Chennai
Total Road Distance: 1335.0 km

