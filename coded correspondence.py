def cc_decrypt(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    message = (message.lower()).split(' ')
    decrypted = []
    for word in message:
        word_split = []
        for letter in word:
            if not letter in alphabet:
                word_split.append(letter)
            else:
                word_split.append(alphabet[alphabet.find(letter) + offset])
        word_split = ''.join(word_split)
        decrypted.append(word_split)
    decrypted = ' '.join(decrypted)
    return decrypted

def cc_encrypt(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    message = (message.lower()).split(' ')
    decrypted = []
    for word in message:
        word_split = []
        for letter in word:
            if not letter in alphabet:
                word_split.append(letter)
            else:
                word_split.append(alphabet[alphabet.find(letter) - offset])
        word_split = ''.join(word_split)
        decrypted.append(word_split)
    decrypted = ' '.join(decrypted)
    return decrypted

def cc_brute(message):
    for i in range(1,26):
        print(cc_decrypt(message, i))
    return

def vc_encrypt(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    message = (message.lower()).split(' ')
    message_xtra_rm = []

    #removes extra symbols
    for word in message:
        word_split = []
        for i in word:
            if alphabet.find(i) == -1:
                continue
            word_split.append(i)
        word_split = ''.join(word_split)
        message_xtra_rm.append(word_split)
    message = message_xtra_rm
    message_join = ' '.join(message)
    message_idxd = []
    message_idxd_keyed = []
    key = key.lower()

    #adjusts key length to handle message length
    while len(key) < len(message_join):
        key += key

    #indexes key
    key_idxd = []
    for i in key:
        key_idxd.append(alphabet.find(i))

    #indexes message/words in message list
    for word in message:
        message_idx = []
        for letter in word:
            message_idx.append(alphabet.find(letter))
        message_idxd.append(message_idx)
    
    #shifts message letter indexes according to key
    key_idxd_idx = 0
    for lst in message_idxd:
        lst_idx = 0
        keyed_word = []
        for i in lst:
            keyed_word.append(lst[lst_idx] + key_idxd[key_idxd_idx])
            lst_idx += 1
            key_idxd_idx += 1
        message_idxd_keyed.append(keyed_word)
    
    #converts encrpyted index numbers back to letters
    message_encrypted_lst = []
    for word in message_idxd_keyed:
        wrd_encrypted_lst = []
        for bit in word:
            wrd_encrypted_lst.append(alphabet[bit])
        wrd_encrypted_lst = ''.join(wrd_encrypted_lst)
        message_encrypted_lst.append(wrd_encrypted_lst)
    message_encrypted_lst = ' '.join(message_encrypted_lst)
            
    return message_encrypted_lst

def vc_decrypt(message, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    message = (message.lower()).split(' ')

    #removes extra symbols
    message_xtra_rm = []
    for word in message:
        word_split = []
        for i in word:
            if alphabet.find(i) == -1:
                continue
            word_split.append(i)
        word_split = ''.join(word_split)
        message_xtra_rm.append(word_split)
    message = message_xtra_rm
    message_join = ' '.join(message)
    message_idxd = []
    message_idxd_keyed = []
    key = key.lower()

    #adjusts key length to handle message length
    while len(key) < len(message_join):
        key += key

    #indexes key
    key_idxd = []
    for i in key:
        key_idxd.append(alphabet.find(i))

    #indexes message/words in message list
    for word in message:
        message_idx = []
        for letter in word:
            message_idx.append(alphabet.find(letter))
        message_idxd.append(message_idx)
    
    #shifts message letter indexes according to key
    key_idxd_idx = 0
    for lst in message_idxd:
        lst_idx = 0
        keyed_word = []
        for i in lst:
            keyed_word.append(lst[lst_idx] - key_idxd[key_idxd_idx])
            lst_idx += 1
            key_idxd_idx += 1
        message_idxd_keyed.append(keyed_word)
    
    #converts encrpyted index numbers back to letters
    message_encrypted_lst = []
    for word in message_idxd_keyed:
        wrd_encrypted_lst = []
        for bit in word:
            wrd_encrypted_lst.append(alphabet[bit])
        wrd_encrypted_lst = ''.join(wrd_encrypted_lst)
        message_encrypted_lst.append(wrd_encrypted_lst)
    message_encrypted_lst = ' '.join(message_encrypted_lst)
            
    return message_encrypted_lst

#print(brute('vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px\'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.'))
#print(decrypt('qrstuvwxyzabcdefghijklmnop!!!!', 10))
#print(encrypt('AbcdefghijklmNopqrstuvwxyz!!!!', 10))
#print(vc_encrypt('barry is the spy', 'dog'))
#print(vc_decrypt('dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!', 'friends'))