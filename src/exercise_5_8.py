def newbook(book, plaintext_in):
    return book.join([c for c in plaintext_in if c not in book])


def encodewithbook(book, plaintext_in):
    keys = {c: str(book.find(c)) for c in plaintext_in}
    return ''.join(['*' + keys[ch] for ch in plaintext_in])[1:]


def decodewithbook(book, ciphertext):
    decoded = [book[int(c)] for c in ciphertext.split('*')]
    return ''.join(c for c in decoded)


book_1 = (
    'In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of'
    'those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing.')
plaintext = 'No es nO'
newbook_1 = newbook(book_1, plaintext)
cipher_1 = encodewithbook(newbook_1, plaintext)

decipher_1 = decodewithbook(newbook_1, cipher_1)
cipher_2 = '22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*1*37*59*11*23*11*1*57*6*173*7*11'
decipher_2 = decodewithbook(newbook_1, cipher_2)
