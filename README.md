# Passtools
GitHub repo for the project "passtools" on pypi. This package allows tools that will provide you with functionality to do all kinds of stuff with passwords.

## About this version
- Version = 0.1.0
- This version contains the very core of this package

## Installing and Updating passwordtools
### Installation process

<h4 style="color: #F9C74F; font-size: 17px;">To install  or upgrade passtools on windows</h4>
**To install passwordtools:**
1. Open _cmd_ or _powershell_
2. Run this command
```commandline
pip install passwordtools
```
3. You have successfully installed it!

**To upgrade passwordtools:**
1. Open _cmd_ or _powershell_
2. Run this command
```commandline
pip install passwordtools --upgrade
```
3. You have successfully installed it!

<h4 style="color: #F9C74F; font-size: 17px;">To install or upgrade passtools on mac</h4>
**To install passwordtools:**  
1. Open terminal
2. Run this command
```commandline
pip3 install passwordtools
```
3. You have successfully installed it!

**To upgrade passwordtools:**
1. Open terminal
2. Run this command
```commandline
pip3 install passwordtools --upgrade
```
3. You have successfully upgraded it!

<h4 style="color: #F9C74F; font-size: 17px;">To install or upgrade passtools on linux</h4>
**To install passwordtools:**
1. Open terminal
2. Run this command
```commandline
sudo pip3 install passwordtools
```
3. You have successfully installed it!

**To upgrade passwordtools:**
1. Open terminal
2. Run this command
```commandline
sudo pip3 install passwordtools --upgrade
```
3. You have successfully upgraded it!  

<h2 style="color: #F3722C;">Documentation</h2>

<h3 style="color: #F8961E; font-size: 22px;">Importing passtools</h3>
To import passtools module, just add  this line to your python code
```python
import passtools
```

<h3 style="color: #F8961E; font-size: 22px;">passhash()</h3>
The `passhash()` hashes a string in a secure and fast way.

<h4 style="color: #F9C74F; font-size: 17px;">Parameters</h4>

|   Parameter   |   Default value  |                                                             Description                                                             | Data Type |
|:-------------:|:----------------:|:-----------------------------------------------------------------------------------------------------------------------------------:|:---------:|
| prompt        |  NO DEFULT VALUE | The string to hash                                                                                                                  | string    |
| hash_type     | sha256           | The hash type of your hash.  Hash Types available: 1. sha256 2. sha1 3. sha224 4. sha384 5. sha512 6. md5                           | string    |
| hash_strength | 1                | How strong you want your hash to be. This is done my hashing the hash in a loop. The more the strength, the more time it will take. | integer   |

<h4 style="color: #F9C74F; font-size: 17px;">Code example</h4>
```python
import passtools

password = passtools.passhash("Super Secret password", hash_type="md5", hash_strength=3)

print(password)
```
**Output:**
```commandline
ba1ad8dbb5655bd1b193de019f3f87c2
```

___
**More documentation will be added soon ..**