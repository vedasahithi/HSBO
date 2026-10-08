# Imports PIL module
from PIL import Image

# open method used to open different extension image file
im1 = Image.open(r"Result_graphs\acc_tr.png")
im2 = Image.open(r"Result_graphs\tpr_tr.png")
im3 = Image.open(r"Result_graphs\tnr_tr.png")
im4 = Image.open(r"Result_graphs\acc_a.png")
im5 = Image.open(r"Result_graphs\tpr_a.png")
im6 = Image.open(r"Result_graphs\tnr_a.png")
im7 = Image.open(r"Result_graphs\acc_p1.png")
im8 = Image.open(r"Result_graphs\tpr_p1.png")
im9 = Image.open(r"Result_graphs\tnr_p1.png")
im10 = Image.open(r"Result_graphs\acc_p2.png")
im11 = Image.open(r"Result_graphs\tpr_p2.png")
im12 = Image.open(r"Result_graphs\tnr_p2.png")
im13 = Image.open(r"Result_graphs\loss.png")


# This method will show image in any image viewer
im1.show()
im2.show()
im3.show()
im4.show()
im5.show()
im6.show()
im7.show()
im8.show()
im9.show()
im10.show()
im11.show()
im12.show()
im13.show()