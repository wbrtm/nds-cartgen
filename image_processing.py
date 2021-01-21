import os, sys
from PIL import Image

size = (380, 415)
thumb_size = (64, 64)

mask = Image.open('nds_label.png')
nds_cart = Image.open('nds_cart.png')
nds_cart_i = Image.open('nds_cart_i.png')
tds_cart = Image.open('3ds_cart.png')

mask = mask.resize(size, Image.LANCZOS)

for infile in sys.argv[1:]:
	filename_ext = os.path.split(infile)[1]
	filename = os.path.splitext(filename_ext)[0]
	outfile_png = "carts/" + filename + ".png"
	outfile_jpg = "carts/" + filename + ".jpg"
	outfile_thumb = "carts/thumbnails/" + filename + ".jpg"
	try:
		with Image.open(infile) as label:
			label = label.resize(size, Image.LANCZOS)
			if filename[0:3] == "NTR" or filename[0:3] == "TWL":
				if filename[4:5] == "I":
					cart = nds_cart_i.copy()
				else:
					cart = nds_cart.copy()
				cart.paste(label, box=(42,27), mask=mask)
			elif filename[0:3] == "CTR":
				cart = tds_cart.copy()
				cart.paste(label, box=(45,43), mask=mask)				
			
			#cart.save(outfile_png, "PNG", optimize=1)
			
			bg = Image.new("RGBA", cart.size, (255, 255, 255, 255))
			bg.alpha_composite(cart)
			
			bg = bg.convert("RGB")
			bg.save(outfile_jpg, "JPEG", quality=80)
			
			thumbnail = cart.convert("RGB")
			thumbnail.thumbnail(thumb_size, Image.LANCZOS)
			thumbnail.save(outfile_thumb, "JPEG", quality=80)
			
			print(filename_ext)
			
	except OSError:
		print("error", infile)
