import pyperclip
def clip_to_text():
  text = pyperclip.paste()
  return text

def text_to_clip(text):
  pyperclip.copy(text)

def remove_half_space(text):
  text = text.replace('\r\n','').replace(' ','')
  return text

if __name__ == '__main__':
  text = clip_to_text()
  text = remove_half_space(text)
  text_to_clip(text)