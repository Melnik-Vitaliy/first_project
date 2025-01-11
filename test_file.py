class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def __init__(self):
        result = []ПОПРОБУЙ СДЕЛАТЬ ИНИТ ЧТОБЫ МАГИЧЕСКИЙ СТРЕНЖ ВЫВЕЛ ВСЕ КАК НУЖНО

    def cipher(self, original_text, shift):
        result = []
        low_original_text = str.lower(original_text)
        words = low_original_text.split()
        big_sup_result: str = ''
        for letter in words:
            sup_result: str = ''
            for cimbol_words in letter:
                if cimbol_words != ',':
                    chip_simbol = self.alphabet.find(cimbol_words)
                    new_chip_simbol = int((chip_simbol + shift) % 33)
                    chip = self.alphabet[new_chip_simbol]
                    sup_result += chip 
                else:
                    sup_result += cimbol_words
            big_sup_result += sup_result + ' '
        result.append(big_sup_result)
        return result

    def decipher(self, cipher_text, shift):
        result = []
        for letter in cipher_text:
            ...  # здесь ваш код
        return ''.join(result)

    def __str__():
        return ' '.join(self.result)
    
cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))
