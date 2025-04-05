# 1. Ordenar países por nombre
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
sorted_countries_by_name = sorted(countries)
print(sorted_countries_by_name)

# 2. Ordenar países por capital
# Usamos un ejemplo básico, ya que no tenemos acceso a los datos completos
countries_capitals = {
    'Estonia': 'Tallinn',
    'Finland': 'Helsinki',
    'Sweden': 'Stockholm',
    'Denmark': 'Copenhagen',
    'Norway': 'Oslo',
    'Iceland': 'Reykjavik'
}
sorted_by_capital = sorted(countries_capitals.items(), key=lambda item: item[1])
print(sorted_by_capital)

# 3. Ordenar países por población (sin acceso a datos reales, solo un ejemplo)
countries_population = {
    'Estonia': 1326535,
    'Finland': 5540720,
    'Sweden': 10353442,
    'Denmark': 5818553,
    'Norway': 5421241,
    'Iceland': 364134
}
sorted_by_population = sorted(countries_population.items(), key=lambda item: item[1])
print(sorted_by_population)

# 4. Ordenar los 10 idiomas más hablados por ubicación (esto necesitaría un archivo de datos)
# Aquí se puede realizar un código similar si se tiene acceso a un archivo con los datos relevantes.

# 5. Ordenar los 10 países más poblados (similar al anterior, se requiere un archivo con datos de población)
