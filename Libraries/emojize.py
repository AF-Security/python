# emojize
# prompt a user for a str in English and outputs emoji version of that str
# converting any codes (or aliases) therein to their corresponding emoji

import emoji

def main ():
    emoji_text = input("Input: ")
    print(emojize(emoji_text))

def emojize (text):
    emoji_image = emoji.emojize(text)
    return emoji_image







main ()