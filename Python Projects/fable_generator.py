#Fable generator
import random
when = ['In the days of old', 'Once upon a time', 'In a land far away', 'During the era of magic', 'In the kingdom of legends']
who = ['a wise owl', 'a brave lion', 'a cunning fox', 'a humble mouse', 'a kind-hearted rabbit']
name = ['Aldric', 'Seraphina', 'Thorn', 'Marigold', 'Quill']
residence = ['the Enchanted Forest', 'the Mystic Mountains', 'the Emerald Valley', 'the Whispering Meadows', 'the Golden Glade']
went = ['a magical quest', 'seeking advice from a wizard', 'a gathering of the animal council', 'exploring a hidden cave', 'the heart of the enchanted garden']
happened = ['learnt an invaluable lesson', 'broke an ancient curse', 'befriended a mythical creature', 'solved a riddle', 'discovered a long-lost treasure']

print(f"{random.choice(when)} {random.choice(who)} named {random.choice(name)}, that lived in {random.choice(residence)} went to {random.choice(went)} and {random.choice(happened)}")