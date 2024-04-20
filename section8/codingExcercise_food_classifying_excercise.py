# NO TOUCHING ============================================
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])
# NO TOUCHING =============================================


# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if food in ['apple', 'grape']:
    print("fruit")
if food in ['bacon', 'steak']:
    print("meat")
if food in ['dirt', 'worm']:
    print("yuck")