import json
import re
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

path = "../datas"
filename = "/infomath.json"

with open(path+filename,"r",encoding="utf-8") as f:
  json_load = json.load(f)
largeQuestions = list(json_load.keys())
print("plz input scoring qu number...")
for i in range(len(largeQuestions)):
  print("{}: {}".format(i, largeQuestions[i]))
keyNum = int(input())
answers = json_load[largeQuestions[keyNum]]
go = True

imagePattern = "^image:"
imageCheck = re.compile(imagePattern)

while go:
  print("--------------------------------------------------------")
  for midNum in answers:
    print(" "+midNum)
    for smallNum in answers[midNum]:
      print("  "+smallNum)

      if isinstance(answers[midNum][smallNum], dict):
        # コメントが存在するとき
        print("   answer is : "+answers[midNum][smallNum]["ans"])
        print("   comment is : "+answers[midNum][smallNum]["comment"])

      elif imageCheck.match(answers[midNum][smallNum]):
        # 画像が存在するとき
        _,imageName = answers[midNum][smallNum].split(":")
        im = np.asarray(Image.open(path+imageName))
        fig = plt.figure()
        plt.imshow(im)
        plt.waitforbuttonpress(0) # this will wait for indefinite time
        plt.close(fig)

      else:
        print("   answer is : "+answers[midNum][smallNum])
    next = input("if go next, pless enter: ")
    if next!="":
      go = False
      break
    else:
      print("")