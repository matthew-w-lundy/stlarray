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
makestl(filename="output.stl",basefrac=0.125,relheight=0.5,method='histogram')
```
There are two methods, "interp" and "histogram". Histogram makes a block for each entry in the array, interp connects each entry with all of its neighbours. In general histogram is more truthful but interp may produce smoother prints. 

You may need to downsample your arrays. You can see how to do this in the test folders. 
