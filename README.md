# MOSAIQUE-DL

A little Fun-Project for myself for learning Python

## Why?

I wanted those Wallpapers and animated profile pictures, but also didn't
want to download all by myself so thought about to write a script. At
the first seconds I joked with myself, but then I thought "Why not?".

## Conclusion

It was completely profitable! I learned alot about Python and also of
course about Selenium. I think I would do one or another Project in this
direction.

## Technician Documentation

### Required

- Python 3.9.5 (at least)
- Selenium Module
- Your prefered Browser
- The right browser driver for Selenium

### Configuration/Installation

The python script works only with the brave browser but you can
modify the execution path to the right binary.

You can do this in the chromium driver settings in the script (2nd Section after imports)

```python
chromeOptions.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser-Nightly\Application\brave.exe"
```
The ``r`` is imported, else it doesn't work. After that you can insert your own
path to your browser executable.

After that modification it should work when you type in your terminal the following command:

```python
python mosaique-dl-SBRE-xxx.py
```
The ``xxx`` specifiys the version you need for your operating system.

| Name | Version               |
|------|-----------------------|
| WSE  | Windows Edition       |
| LXE  | Linux Editon          |
| JPYN | Jupyter Notebook      |
| BSE  | BeautifulSoup Edition |
