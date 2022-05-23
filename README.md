# MorseCodeDP

Hello, this is a quick solution for trying to figure out unspaced morse code. It is written using pure dynamic programming, but still has a runtime of Ω(n2^(n)). The problem is that in prefix codes, losing the seperators between coded words makes it extemely difficult to decode. Thus, the runtime is enormous **because** the output is enormous, and you cannot do much better than that! More detailed analysis soon.

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
