import os, sys
from PIL import Image

size = (380, 415)

mask = Image.open('nds_label.png')
cart = Image.open('nds_cart.png')

mask = mask.resize(size)

for infile in sys.argv[1:]:
	filename_ext = os.path.split(infile)[1]
	filename = os.path.splitext(filename_ext)[0]
	outfile = "carts/" + filename + ".png"
	outfile_thumb = "carts/thumbnails/" + filename + ".jpg"
	if infile != outfile and (filename[0:3] == "NTR" or filename[0:3] == "TWL"):
		try:
			with Image.open(infile) as label:
				label = label.resize((mask.width, mask.height))
				empty = Image.new("RGBA", size, (0,0,0,0))
				empty.paste(label, mask)
				cart.alpha_composite(empty, (42,27))
				cart.save(outfile, "PNG")
				print(filename_ext)

				thumb = cart.resize((59, 64))
				thumb = thumb.convert("RGB")
				thumb.save(outfile_thumb, quality=90)

		except OSError:
			print("error", infile)
