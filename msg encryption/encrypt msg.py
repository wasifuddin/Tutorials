# pip install stegano

from stegano import lsb
encoded_img = lsb.hide("coin.png.", "Hello World")
encoded_img.save("encrypted_coin.png")
decrypted_msg = lsb.reveal("encrypted_coin.png")
print(decrypted_msg)
