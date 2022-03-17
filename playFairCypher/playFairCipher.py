
from typing import List

DELETED_LETTER = 'j'
SUBSTIT_LETTER = 'i'

EXTRA_CHARACTERS = [' ', '.', ',', ':', ';']

class PlayFairCipher(object):
    
    def __init__(self) -> None:
        pass

    def validateText(self, text: str) -> bool:
        '''
        Checks if encrypted / decrypted text is in the correct format.
        '''
        for char in text:
            if not char.isalpha() and char not in EXTRA_CHARACTERS:
                print(char)
                return False
        return True
        
    def validatePassword(self, password: str) -> bool:
        '''
        Checks if password is in the correct format.
        '''
        for char in password:
            if not char.isalpha():
                print(char)
                return False
        return True

    def __countNonAlpha(self, text: str) -> int:
        result = 0
        for char in text:
            if not char.isalpha():
                result += 1
        return result

    def __createMatrix(self, password: str) -> List[List[str]]:
        '''
        Creates matrix to encipher or decipher a text.
        '''
        matrix: List[List[str]] = []
        password = password.lower()
        orderedLetters = []

        for char in password:
            char = SUBSTIT_LETTER if char == DELETED_LETTER else char
            if char not in orderedLetters:
                orderedLetters.append(char)

        for asciiNumber in range(97, 123):
            char = chr(asciiNumber)
            if char not in orderedLetters and char != DELETED_LETTER:
                orderedLetters.append(char)

        for i in range(5):
            matrix.append(orderedLetters[i * 5: i * 5 + 5])

        return matrix

    def __getRowAndColumn(self, matrix: List[List[str]], char: str) -> tuple[int]:
        '''
        Returns row and column index of given character in the matrix.
        '''        
        char = SUBSTIT_LETTER if char == DELETED_LETTER else char
        for i in range(len(matrix)):
            if char in matrix[i]:
                return i, matrix[i].index(char)
        return -1, -1
    
    def __preprocessing(self, plainText: str) -> str:
        '''
        Corrects plain text to encipher it properly.

        Preprocessing contains:
        - changing all letters to lowercase
        - replace all 'j' letters for 'i'
        - inserting the 'x' letter between the same characters (only if they would be in pair during enciphering)
        - inserting the 'x' letter at the text end, if the number of letters is odd
        '''
        if len(plainText) == 0:
            return ''

        plainText = plainText.lower()
        plainText = plainText.replace(DELETED_LETTER, SUBSTIT_LETTER)

        i, nonLettersNum = 0, 0
        while i < len(plainText) - 1:
            while not plainText[i].isalpha() and i < len(plainText) - 1:
                i, nonLettersNum = i + 1, nonLettersNum + 1
            if i == len(plainText) - 1:
                break

            j = i + 1
            while not plainText[j].isalpha() and j < len(plainText) - 1:
                j, nonLettersNum = j + 1, nonLettersNum + 1
            if j == len(plainText) - 1 and not plainText[j].isalpha():
                break

            if plainText[i] == plainText[j]:
                plainText = plainText[0: i + 1] + 'x' + plainText[i + 1:]
            i += 2

        if not plainText[-1].isalpha():
            nonLettersNum += 1
        if (len(plainText) - nonLettersNum) % 2 == 1:
            plainText += 'x'
        
        print(f'Preprocessed plain text: {plainText}')
        return plainText

    def __postprocessing(self, plainText: str) -> str:
        '''
        Corrects text after deciphering.

        Postprocessing contains:
        - deleting the 'x' character, if the number of letters is even
        - deleting the 'x' character, if two neighboring letters are the same and they would be in 
          pair during encryption
        '''
        if len(plainText) == 0:
            return ''

        if plainText[-1] == 'x' and (len(plainText) - self.__countNonAlpha(plainText)) % 2 == 0:
            plainText = plainText[:-1]

        i = 1
        while i < len(plainText) - 1:
            k = i
            if plainText[i] == 'x':
                j, k = i - 1, i + 1
                while not plainText[j].isalpha() and j > 0:
                    j -= 1
                
                while not plainText[k].isalpha() and k < len(plainText) - 1:
                    k += 1

                if plainText[j].isalpha() and plainText[k].isalpha():
                    if plainText[j] == plainText[k]:
                        plainText = plainText[: i] + plainText[i + 1:]
                        k -= 1
            i = k + 1
        print(f'Text after postprocessing: {plainText}')
        return plainText

    def encipher(self, plainText: str, password: str) -> str:
        '''
        Enciphers a plain text.
        '''
        plainText = self.__preprocessing(plainText)
        matrix    = self.__createMatrix(password)

        cipherText: str = ''
        i = 0
        while i < len(plainText) - 1:
            strAfterFirstChar = ''

            while not plainText[i].isalpha() and i < len(plainText) - 1:
                cipherText, i = cipherText + plainText[i], i + 1
            if i == len(plainText) - 1:
                break

            j = i + 1
            while not plainText[j].isalpha():
                strAfterFirstChar += plainText[j]
                j += 1

            charRow1, charCol1 = self.__getRowAndColumn(matrix, plainText[i])
            charRow2, charCol2 = self.__getRowAndColumn(matrix, plainText[j])

            # case 1 - both characters are in the same row
            if charRow1 == charRow2:
                cipherText +=   matrix[charRow1][(charCol1 + 1) % 5] + \
                                strAfterFirstChar + \
                                matrix[charRow2][(charCol2 + 1) % 5]

            # case 2 - both characters are in the same column
            elif charCol1 == charCol2:
                cipherText +=   matrix[(charRow1 + 1) % 5][charCol1] + \
                                strAfterFirstChar + \
                                matrix[(charRow2 + 1) % 5][charCol2]
            # case 3
            else:
                cipherText +=   matrix[charRow1][charCol2] + \
                                strAfterFirstChar + \
                                matrix[charRow2][charCol1]
            i = j + 1
        if i == len(plainText) - 1:
            cipherText += plainText[-1]
        print(f'Enciphered text: {cipherText}')
        return cipherText

    def decipher(self, cipherText: str, password: str) -> str:
        '''
        Deciphers a ciphered text.
        '''
        matrix = self.__createMatrix(password)
        cipherText = cipherText.lower()

        plainText: str = ''
        i = 0
        while i < len(cipherText) - 1:
            strAfterFirstChar = ''

            while not cipherText[i].isalpha() and i < len(cipherText) - 1:
                plainText, i = plainText + cipherText[i], i + 1
            if i == len(cipherText) - 1:
                break

            j = i + 1
            while not cipherText[j].isalpha():
                strAfterFirstChar += cipherText[j]
                j += 1

            charRow1, charCol1 = self.__getRowAndColumn(matrix, cipherText[i])
            charRow2, charCol2 = self.__getRowAndColumn(matrix, cipherText[j])

            # case 1 - both characters are in the same row
            if charRow1 == charRow2:
                plainText +=   matrix[charRow1][(charCol1 + 4) % 5] + \
                               strAfterFirstChar + \
                               matrix[charRow2][(charCol2 + 4) % 5]

            # case 2 - both characters are in the same column
            elif charCol1 == charCol2:
                plainText +=   matrix[(charRow1 + 4) % 5][charCol1] + \
                               strAfterFirstChar + \
                               matrix[(charRow2 + 4) % 5][charCol2]
            # case 3
            else:
                plainText +=   matrix[charRow1][charCol2] + \
                               strAfterFirstChar + \
                               matrix[charRow2][charCol1]
            i = j + 1

        plainText = self.__postprocessing(plainText)
        print(f'Plain text: {plainText}')
        return plainText
