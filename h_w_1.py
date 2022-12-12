text_string = "Мама мыла абв иабв раму иабв чтотоабв абв"
text_list = text_string.split(" ")
print(*[ i for i in text_list if "абв" not in i])