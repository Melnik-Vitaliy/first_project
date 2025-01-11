class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        result = []
        low_original_text = str.lower(original_text)
        words = low_original_text.split()
        for letter in words:
            sup_result = []
            for cimbol_words in letter:
                chip_simbol = self.alphabet.find(cimbol_words)
                new_chip_simbol = int(chip_simbol + shift)
                chip = self.alphabet[new_chip_simbol]
                sup_result += chip 
            result.append(sup_result)
        return result

    def decipher(self, cipher_text, shift):
        result = []
        for letter in cipher_text:
            ...  # здесь ваш код
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))
