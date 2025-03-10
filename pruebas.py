it_companies = ["Google", "Apple", "Microsoft", "Amazon", "Tesla"]
for i in range(len(it_companies)):
    if it_companies[i] != "IBM":
        it_companies[i] = it_companies[i].upper()
        break  
print("Updated list of IT companies:", it_companies)
