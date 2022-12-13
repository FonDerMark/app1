from cryptography.fernet import Fernet
from os.path import join, exists

key_folder_path = 'cks'
encrypted_path = 'files/encrypted'
decrypted_path = 'files/decrypted'


def write_key(key_name='crypto.key'):
    """creates a new key file"""
    key_path = join(key_folder_path, key_name)
    if exists(key_path):
        print('Файл уже создан')
    else:
        key = Fernet.generate_key()
        with open(join('cks', key_name), 'wb') as file:
            file.write(key)


def key_return(key_name='crypto.key'):
    """returns the contents of the key"""
    path_to_key = join(key_folder_path, key_name)
    with open(path_to_key, 'rb') as key:
        return key.read()


def filename_mod(filename, mod='decrypted'):
    """modifies the file name by adding to it the value passed in the 'mod' variable"""
    file_names = filename.split('.')
    mod_plus_name = file_names[-2] + '_' + mod + '.'
    ext = file_names[-1]
    return mod_plus_name + ext


def encrypt(file_to_encrypt):
    """encrypts the contents of the file and creates a new encrypted file in the 'encrypted' folder"""
    path_to_file = join(decrypted_path, file_to_encrypt)
    key = Fernet(key_return())
    with open(path_to_file, 'rb') as file:
        file_data = file.read()
    encrypted_data = key.encrypt(file_data)
    with open(join(encrypted_path, file_to_encrypt), 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)


def decrypt(file_to_decrypt):
    """decrypts the contents of the file and creates a new decrypted file in the 'decrypted' folder"""
    path_to_file = join(encrypted_path, file_to_decrypt)
    key = Fernet(key_return())
    path_to_safe_file = join(decrypted_path, filename_mod(file_to_decrypt))
    with open(path_to_file, 'rb') as file:
        decrypted_data = key.decrypt(file.read())
        with open(path_to_safe_file, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)


if __name__ == '__main__':
    write_key()
