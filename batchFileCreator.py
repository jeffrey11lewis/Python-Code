targetPath = input('please enter the full filepath of your directory: ')
shortcutName = input('please enter the name of the shortcut: ')

targetPath = r'{}'.format(targetPath)
#print(targetPath)

writeCode = ('''@echo off
set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"
echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "%USERPROFILE%\Desktop\{}.lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.TargetPath = "{}" >> %SCRIPT%
echo oLink.Arguments = "-h ServerNameOrIP -a ifix" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%
cscript /nologo %SCRIPT%
del %SCRIPT%''').format(shortcutName, targetPath)
print(writeCode)
print('\nPROCESS HAS FINISHED')




#TODO add where you can name the batch file according to what the input is
myBat = open(r'C:\Users\torch\Desktop\clickHere.bat','w+')

myBat.write(writeCode)
myBat.close()