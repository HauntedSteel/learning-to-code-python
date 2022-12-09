from PIL import Image
import numpy as np

ascii_vals = ['`','^','"',',',':',';','I','l','!','i','~','+','_','-','?',']',
        '[','}','{','1',')','(','|','/','t','f','j','r','x','n','u','v','c','z',
        'X','Y','U','J','C','L','Q','0','O','Z','m','w','q','p','d','b','k','h',
        'a','o','*','#','M','W','&','8','%','B','@','$']
ascii_vals_brightness = {}
val = 0
increment = 255 // len(ascii_vals)

for x in ascii_vals:
    ascii_vals_brightness[(val, val + increment)] = x
    val += increment + 1

#ascii_vals_brightness = {(0, 3): ' ', (4, 7): '`', (8, 11): '^', (12, 15): '"', (16, 19): ',', (20, 23): ':', (24, 27): ';', (28, 31): 'I', (32, 35): 'l', (36, 39): '!', (40, 43): 'i', (44, 47): '~', (48, 51): '+', (52, 55): '_', (56, 59): '-', (60, 63): '?', (64, 67): ']', (68, 71): '[', (72, 75): '}', (76, 79): '{', (80, 83): '1', (84, 87): ')', (88, 91): '(', (92, 95): '|', (96, 99): '/', (100, 103): 't', (104, 107): 'f', (108, 111): 'j', (112, 115): 'r', (116, 119): 'x', (120, 123): 'n', (124, 127): 'u', (128, 131): 'v', (132, 135): 'c', (136, 139): 'z', (140, 143): 'X', (144, 147): 'Y', (148, 151): 'U', (152, 155): 'J', (156, 159): 'C', (160, 163): 'L', (164, 167): 'Q', (168, 171): '0', (172, 175): 'O', (176, 179): 'Z', (180, 183): 'm', (184, 187): 'w', (188, 191): 'q', (192, 195): 'p', (196, 199): 'd', (200, 203): 'b', (204, 207): 'k', (208, 211): 'h', (212, 215): 'a', (216, 219): 'o', (220, 223): '*', (224, 227): '#', (228, 231): 'M', (232, 235): 'W', (236, 239): '&', (240, 243): '8', (244, 247): '%', (248, 251): 'B', (252, 255): '@', (256, 259): '$'}




def asciiConvert(sourceImagePath, scaledWidth):

    source = Image.open(sourceImagePath).convert("L") #using pillow, opens image as grayscale

    basewidth = scaledWidth
    newPercent = (basewidth / float(source.size[0]))
    hsize = int((float(source.size[1]) * float(newPercent)))
    source = source.resize((basewidth, hsize), Image.Resampling.LANCZOS)

    sourcePixels = np.asarray(source)  # converts into numpy array

    text = ""
    for a in range(len(sourcePixels)):
        for b in range(len(sourcePixels[0])):
            val = sourcePixels[a][b]
            for low, high in ascii_vals_brightness.keys():
                if low <= val <= high:
                    text += ascii_vals_brightness[(low, high)]
                    break
        text += "\n"

    return text
print(asciiConvert("/YOURPATHNAME",100))