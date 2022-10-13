"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    items =  [str(i) for i in items]
    frequencies = {i:items.count(i) for i in items}
    
    
    # Your code goes here
    return frequencies

items = [100, 'Hello', '100', '100', 100]

print(frequencies(items)) 