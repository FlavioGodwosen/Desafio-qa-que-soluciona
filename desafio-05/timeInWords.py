def timeInWords(h, m):
    num_to_words = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'quarter', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two',
        23: 'twenty three', 24: 'twenty four', 25: 'twenty five',
        26: 'twenty six', 27: 'twenty seven', 28: 'twenty eight',
        29: 'twenty nine', 30: 'half'
    }

    if m == 0:
        return f"{num_to_words[h]} o' clock"
    elif m == 15:
        return f"quarter past {num_to_words[h]}"
    elif m == 30:
        return f"half past {num_to_words[h]}"
    elif m == 45:
        return f"quarter to {num_to_words[h + 1 if h < 12 else 1]}"
    elif m < 30:
        minute_word = "minute" if m == 1 else "minutes"
        return f"{num_to_words[m]} {minute_word} past {num_to_words[h]}"
    else:
        minute_word = "minute" if 60 - m == 1 else "minutes"
        return f"{num_to_words[60 - m]} {minute_word} to {num_to_words[h + 1 if h < 12 else 1]}"

# Exemplos de uso
print(timeInWords(5, 0))    # Output: five o' clock
print(timeInWords(5, 1))    # Output: one minute past five
print(timeInWords(5, 10))   # Output: ten minutes past five
print(timeInWords(5, 15))   # Output: quarter past five
print(timeInWords(5, 30))   # Output: half past five
print(timeInWords(5, 40))   # Output: twenty minutes to six
print(timeInWords(5, 45))   # Output: quarter to six
print(timeInWords(5, 47))   # Output: thirteen minutes to six
print(timeInWords(5, 28))   # Output: twenty eight minutes past five
