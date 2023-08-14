quixote = ('In a village of La Mancha, the name of which I have no desire to call to mind,'
           'there lived not long since one ofthose gentlemen that keep a lance in the lance-rack,'
           'an old buckler, a lean hack, and a greyhound for coursing.'
           )
text1 = 'no is no'

gen_code_keys = (lambda book, plain_text: (
    {c: str(book.find(c)) for c in plain_text}))

encoder = (lambda code_keys, plain_text:
           ''.join(['*' + code_keys[c] for c in plain_text])[1:])

encrypt = (lambda book, plain_text:
           encoder(gen_code_keys(book, plain_text), plain_text))

cipher1 = encrypt(quixote, text1)
print(cipher1)

gen_decode_keys = (lambda book, cipher_text: {s: book[int(s)] for s in cipher_text.split('*')})
print(gen_decode_keys(quixote, cipher1))

decoder = (lambda decode_keys, cipher_text: ''.join([decode_keys[c] for c in cipher_text.split('*')]))

decode = (lambda book, cipher_text: decoder(gen_decode_keys(book, cipher_text), cipher_text))

uncipher1 = decode(quixote, cipher1)
print(uncipher1)
