price = int(input("รับค่าราคาสินค้า:"))
vat = price*(7/100)
disc = price*(5/100)
total = price-disc+vat

print("ภาษีมูลค่าเพิ้ม %.3f"% vat , "บาท")
print("ส่วนลด %.3f" % disc, "บาท")
print(ราคารวม %.3f" % total, "บาท")