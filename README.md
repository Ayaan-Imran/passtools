# Passtools
pypasstools allows tools that will provide you with functionality to do all kinds of stuff with passwords.

## About this version
- Version = 0.0.11
- This version contains documentation updates
## Installing and Updating pypasstools
Follow the installation process accroding to your OS.
### To install or upgrade pypasstools on windows
**To install pypasstools:**
1. Open _cmd_ or _powershell_
2. Run this command
```commandline
pip install pypasstools
```
3. You have successfully installed it!

**To upgrade pypasstools:**
1. Open _cmd_ or _powershell_
2. Run this command
```commandline
pip install pypasstools --upgrade
```
3. You have successfully installed it!

### To install or upgrade pypasstools on mac
**To install pypasstools:**  
1. Open terminal
2. Run this command
```commandline
pip3 install pypasstools
```
3. You have successfully installed it!

**To upgrade pypasstools:**
1. Open terminal
2. Run this command
```commandline
pip3 install pypasstools --upgrade
```
3. You have successfully upgraded it!

### To install or upgrade pypasstools on linux
**To install pypasstools:**
1. Open terminal
2. Run this command
```commandline
sudo pip3 install pypasstools
```
3. You have successfully installed it!

**To upgrade pypasstools:**
1. Open terminal
2. Run this command
```commandline
sudo pip3 install pypasstools --upgrade
```
3. You have successfully upgraded it!  

## Documentation
### Importing pypasstools
To import pypasstools module, just add this line to your python code. As you can see, you import it with a different name
```python
import passtools
```
### passhash()
The `passhash()` hashes a string in a secure and fast way.
#### Parameters

|   Parameter   |   Default value  |                                                             Description                                                             | Data Type |
|:-------------:|:----------------:|:-----------------------------------------------------------------------------------------------------------------------------------:|:---------:|
| prompt        |  NO DEFULT VALUE | The string to hash                                                                                                                  | string    |
| hash_type     | sha256           | The hash type of your hash.  Hash Types available: 1. sha256 2. sha1 3. sha224 4. sha384 5. sha512 6. md5                           | string    |
| hash_strength | 1                | How strong you want your hash to be. This is done my hashing the hash in a loop. The more the strength, the more time it will take. | integer   |

#### Code example
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