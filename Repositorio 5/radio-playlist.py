weekly_playlist = [
    "Blinding Lights",
    "Levitating",
    "As It Was",
    "Heat Waves",
    "Good 4 u",
]

weekly_playlist.append("Drivers License")

weekly_playlist.insert(0, "Bohemian Rhapsody")

weekly_playlist.remove("Good 4 u")

print(f"La canción 'Levitating' está en el índice: {weekly_playlist.index('Levitating')}")

print(f"Hay {weekly_playlist.count('As It Was')} canción(es) de Harry Styles en la lista.")

weekly_playlist.reverse()
print(f"Lista de Jueves de Retro (en orden inverso): {weekly_playlist}")

weekly_playlist.sort()
print(f"Lista alfabética: {weekly_playlist}")

print(f"Lista de reproducción semanal final: {weekly_playlist}")

print(f"Número total de canciones en la lista final: {len(weekly_playlist)}")