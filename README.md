# stlarray
Make numpy array into stl files

## Install

```
git clone https://github.com/matthew-w-lundy/stlarray
cd stlarray
python setup.py install
```

## Usage
```
from stlarray.array2stl import makestl
makestl(<array>)
```
Big arrays make big files

### Options

```
makestl(filename="output.stl",basefrac=0.125,relheight=0.5)
```
