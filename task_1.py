from hashlib import md5, sha256, sha512

s = "Python Bootcamp"
s_enc = s.encode()

def string_to_hash():
    hash_alg = input('Write hash algorithm (md5, sha256, sha512):')

    if hash_alg == 'md5':
        hash_s = md5(s_enc)
    elif hash_alg == 'sha256':
        hash_s = sha256(s_enc)
    elif hash_alg == 'sha512':
        hash_s = sha512(s_enc)
    else:
        return print('We did not recognize the text, please try again...')
 
    print(f'Hash result {hash_alg}:{hash_s.hexdigest()}')

if __name__ == '__main__':
    string_to_hash()