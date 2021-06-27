import argparse
import os
try:
    from ImageGoNord import NordPaletteFile, GoNord
    import os 
except:
    "[+] Missing module: pip install image-go-nord"
    exit

parser = argparse.ArgumentParser(description="Quick method to convert images to nord theme.")
parser.add_argument("-p","--palette", type=int, dest="palette", help="Select color Palette, options: [1] Polar Night, [2] Frost, [3] Snow Storm, [4] Aurora", required=True)
parser.add_argument("-f", "--file", dest="file", help="File path to image", required=True)
parser.add_argument("-o","--output",dest="output",help="Output file name", default='images/go2nord.png')
args = parser.parse_args()

isfile =  os.path.isfile(args.file)
if isfile:
    pass
else:
    print("[+] Image not found!")
    exit


def aurora():
    print("[+] Starting Aurora Conversion...")
    try:
        go_nord=GoNord()
        go_nord.enable_avg_algorithm()
        go_nord.add_file_to_palette(NordPaletteFile.AURORA)
        polar_image = go_nord.open_image(args.file)
        go_nord.convert_image(polar_image,save_path=args.output)
        print("[+] Success! Image saved at " + args.output)
    except Exception as e:
        print(e)

def polar():
    print("[+] Starting Polar Night Conversion...")
    try:
        go_nord=GoNord()
        go_nord.enable_avg_algorithm()
        go_nord.add_file_to_palette(NordPaletteFile.POLAR_NIGHT)
        polar_image = go_nord.open_image(args.file)
        go_nord.convert_image(polar_image,save_path=args.output)
        print("[+] Success! Image saved at " + args.output)
    except Exception as e:
        print(e)

def frost():
    print("[+] Starting Frost Conversion...")
    try:
        go_nord=GoNord()
        go_nord.enable_avg_algorithm()
        go_nord.add_file_to_palette(NordPaletteFile.FROST)
        polar_image = go_nord.open_image(args.file)
        go_nord.convert_image(polar_image,save_path=args.output)
        print("[+] Success! Image saved at " + args.output)
    except Exception as e:
        print(e)

def snow_storm():
    print("[+] Starting Snow Storm Converion...")
    try:
        go_nord=GoNord()
        go_nord.enable_avg_algorithm()
        go_nord.add_file_to_palette(NordPaletteFile.SNOW_STORM)
        polar_image = go_nord.open_image(args.file)
        go_nord.convert_image(polar_image,save_path=args.output)
        print("[+] Success! Image saved at " + args.output)
    except Exception as e:
        print(e)


if args.palette==1:
    polar()
elif args.palette==2:
    frost()
elif args.palette==3:
    snow_storm()
elif args.palette==4:
    aurora()
else:
    print("[+] Something went wrong... :(")
    exit
