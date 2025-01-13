class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        result = []
        low_text = str.lower(text)
        for letter in low_text:
            if letter not in self.alphabet:
                result.append(letter)
            else:
                if is_encrypt is True:
                    old_letter = self.alphabet.find(letter)
                    new_letter = int((old_letter + shift) % 33)
                    chip_letter = str(self.alphabet[new_letter])
                    result.append(chip_letter)
                else:
                    old_letter = self.alphabet.find(letter)
                    new_letter = int((old_letter - shift) % 33)
                    chip_letter = str(self.alphabet[new_letter])
                    result.append(chip_letter)
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))
