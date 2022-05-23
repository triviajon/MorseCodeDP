# MorseCodeDP

Hello, this is a quick solution for trying to figure out unspaced morse code. It is written using pure dynamic programming, and has a theorized runtime of worst case O(n). It will be a little bit slower than expected, due to the .update calls, but O(n) is good enough. Enjoy!

# Usage

Download the MorseCodeDP/MorseCodeDP.py file. From the command line in the directory where you downloaded the file, and type:
```py
python.exe .\MorseCodeDP.py $MorseCode
```
Where MorseCode is the encoded message you are trying to decode, and has proper morse code format (dots (.) and dashes (-), but a variety of other formats are supported. just try!)

# Example
```py
PS C:\fake_dir\MorseCodeDP> python.exe .\MorseCodeDP.py "0101"
{'aet', 'ek', 'aa', 'ent', 'rt', 'etet', 'eta'}

PS C:\fake_dir\MorseCodeDP> python.exe .\MorseCodeDP.py "aaab"
{'ttn', 'mn', 'oe', 'mte', 'ttte', 'tme', 'tg'}
```
