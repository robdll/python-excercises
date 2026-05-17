heroes = {
  "Thor": 100,
  "Iron Man": 85,
  "Wolverine": 75,
  "Spider-Man": 55,
  "Batman": 26
}

#Print Thor's strength
print(heroes['Thor'])

# Loop through the dictionary and print each hero name and strength in this format:
# Thor has strength 100
for k,v in heroes.items():
  print(f'{k} has strength {v}')

# Find and print the name of the strongest hero (without using max() — use a loop)
best, name = 0, ''
for k,v in heroes.items():
  if v > max:
    best = v
    name = k
print(f'strongest hero is {name}')
