try:
    from ImageGoNord import NordPaletteFile, GoNord
    import os 
except:
    "[+] Missing module: pip install image-go-nord"
    exit
os.system('clear')
print('''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ____                              ______         _   __               __
   /  _/___ ___  ____ _____ ____     / ____/___     / | / /___  _________/ /
   / // __ `__ \/ __ `/ __ `/ _ \   / / __/ __ \   /  |/ / __ \/ ___/ __  / 
 _/ // / / / / / /_/ / /_/ /  __/  / /_/ / /_/ /  / /|  / /_/ / /  / /_/ /  
/___/_/ /_/ /_/\__,_/\__, /\___/   \____/\____/  /_/ |_/\____/_/   \__,_/   
                    /____/                                                  

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''')

image = input("[+] Enter Image File Path:\n\n[+] ")
isfile =  os.path.isfile(image)
if isfile:
    print("\n[+] Image Found! Continuing on...\n")
else:
    while isfile!=True:
        try:
            image = input("\n[+] Image not found, try again. (ex: /home/Nord/example.png):\n\n[+] ")
            isfile =  os.path.isfile(image)
            if isfile:
                print("\n[+] Success! Continuing on...\n")
        except Exception as e:
            print(e)

print("+"*77)
print('''\n[+] Select #1-4 for Color Palette options:

[1] Polar Night
[2] Snow Storm
[3] Frost
[4] Aurora''')

color_int = input("\n[+] ")
while not (color_int=='1' or color_int=='2' or color_int=='3' or color_int=='4'):
        print("[+] Invalid Option, Try Again....")
        color_int = input("[+] ")

def aurora():
    try:
        go_nord=GoNord()
        go_nord.enable_avg_algorithm()
        go_nord.add_file_to_palette(NordPaletteFile.AURORA)
        polar_image = go_nord.open_image(image)
        go_nord.convert_image(polar_image,save_path='/tmp/GoneNord.png')
        print("[+] Success! Image saved as '/tmp/GoneNord.png'")
    except Exception as e:
        print(e)

def polar():
    try:
        go_nord=GoNord()
        go_nord.enable_avg_algorithm()
        go_nord.add_file_to_palette(NordPaletteFile.POLAR_NIGHT)
        polar_image = go_nord.open_image(image)
        go_nord.convert_image(polar_image,save_path='/tmp/GoneNord.png')
        print("[+] Success! Image saved as '/tmp/GoneNord.png'")
    except Exception as e:
        print(e)

def frost():
    try:
        go_nord=GoNord()
        go_nord.enable_avg_algorithm()
        go_nord.add_file_to_palette(NordPaletteFile.FROST)
        polar_image = go_nord.open_image(image)
        go_nord.convert_image(polar_image,save_path='/tmp/GoneNord.png')
        print("[+] Success! Image saved as '/tmp/GoneNord.png'")
    except Exception as e:
        print(e)

def snow_storm():
    try:
        go_nord=GoNord()
        go_nord.enable_avg_algorithm()
        go_nord.add_file_to_palette(NordPaletteFile.SNOW_STORM)
        polar_image = go_nord.open_image(image)
        go_nord.convert_image(polar_image,save_path='/tmp/GoneNord.png')
        print("[+] Success! Image saved as '/tmp/GoneNord.png'")
    except Exception as e:
        print(e)
print("\n")
print("+"*77)
if color_int=='1':
    print("\n[+] Going Nord - Polar Night")
    try:
        polar()
    except Exception as e:
        print(e)
elif color_int=='2':
    print("\n[+] Going Nord - Snow Storm")
    try:
        snow_storm()
    except Exception as e:
        print(e)
elif color_int=='3':
    print("\n[+] Going Nord - Frost")
    try:
        frost()
    except Exception as e:
        print(e)
elif color_int=='4':
    print("\n[+] Going Nord - Aurora")
    try:
        aurora()
    except Exception as e:
        print(e)

#go_nord=GoNord()
#go_nord.enable_avg_algorithm()
#go_nord.add_file_to_palette(NordPaletteFile.POLAR_NIGHT)

#image = go_nord.open_image("/home/justin/Firefox_wallpaper.png")
#go_nord.convert_image(image, save_path='/home/justin/test.png')