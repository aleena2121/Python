list_of_dictionaries = [ {"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
unique_vals = set()
for dictionary in list_of_dictionaries:
    for value in dictionary.values():
        unique_vals.add(value)             # Extract unique values using a set
print("Unique values:", unique_vals)