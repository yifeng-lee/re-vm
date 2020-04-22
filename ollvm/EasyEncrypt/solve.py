from Crypto.Cipher import AES

key = b'thisisthekey!!!!'
enc = AES.new(key,AES.MODE_ECB)
with open('flag.lck','rb') as r:
    c1 = r.read(16)
    c2 = r.read()
plain = enc.decrypt(c1)
with open('a.png','wb') as w:
    w.write(plain)
    w.write(c2)