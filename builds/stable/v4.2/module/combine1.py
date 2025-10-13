from PIL import Image

tex1 = "E:\.Temp\M1_Textures\Game\AA_Landscape\M1_Landscape\Textures\Main\T_Cobblestone1_AO.PNG"
tex2 = "E:\.Temp\M1_Textures\Game\AA_Landscape\M1_Landscape\Textures\Main\T_Cobblestone1_Roughness.PNG"
tex3 = "E:\.Temp\M1_Textures\T_Cobblestone1_AR.PNG"
# Wczytaj tekstury
image1 = Image.open("texture1.png").convert("RGBA")
image2 = Image.open("texture2.png").convert("RGBA")

# Wyciągnij kanał R z obu obrazów
r1, _, _, _ = image1.split()
r2, _, _, _ = image2.split()

# Stwórz nowy obraz łączący te kanały:
# R = r1, G = r2, B = 0, A = 255
zero_channel = Image.new("L", image1.size, 0)      # B = 0
alpha_channel = Image.new("L", image1.size, 255)   # A = 255

# Połącz kanały
merged_image = Image.merge("RGBA", (r1, r2, zero_channel, alpha_channel))

# Zapisz wynik
merged_image.save(tex3)

print(f"Zapisano jako {tex3}")
