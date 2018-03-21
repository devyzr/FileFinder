# FileFinder
A really simple module for finding filenames and dirs in a specified or local directory. There's a thing to let us rename files en masse as well.

What I like to do is create a symlink from the file in github to my site-packages folder. You can find your site-packages folder with:

```
python -m site --user-site
```

And you can make a symlink in windows with:
```
mklink /H "C:\Path\To\Your\site-packages\FileFinder.py" "C:\Path\To\Your\GitFolder\FileFinder\FileFinder.py"
```
## Tests

Currently the "tests" are near worthless. I don't think I'll change that soon.
