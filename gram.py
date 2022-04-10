import os
import language_tool_python
os.system("clear")
print("\n Please wait..")
tool = language_tool_python.LanguageTool('en-US')
os.system("clear")
text = input(" Type here : ")
os.system("clear")
print("\n Please wait..")
matches = tool.check(text)
#www.philiphacker.in
c = len(matches)
os.system("clear")
print("\n Total Mistakes : "+str(c)+"\n\n")
input("press any key to see mistakes in detail")
for i in range(0,c):
    os.system("clear")
    print("\n Mistake : "+str(i+1)+"\n\n")
    print(matches[i])
    input("\n\npress any key for next mistake..")
os.system("clear")
print("\n That's all..\n")