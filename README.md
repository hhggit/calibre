# What is this branch for?

In general, calibre make a copy of the book when import it to the calibre library and totally forget about the oringinal book, and organize the copy in a different way. To keep the original book, save disk space and other reasons, I add a column into the meta database to record the books original file path, and the modified calibre use the original file instead of copy.

# How to use?
1. Compile the modified ".py" into ".pyo"

  ```
  python2 -O -m py_compile calibre_src_path\src\calibre\db\backend.py
  python2 -O -m py_compile calibre_src_path\src\calibre\db\cache.py
  python2 -O -m py_compile calibre_src_path\src\calibre\db\tables.py
  ```    
2. Replace the ".pyo" in calibre_binary_path\pylib.zip'.
    Open the calibre_binary_path\pylib.zip with WinRAR, drag the calibre_src_path\src\calibre\db\(backend|cache|talbes).pyo into its calibre\db subdirectory, the compress method choose store only.    

3. Modify the resource calibre_binary_path\resource\meta_data.sql file.


-----------

calibre
=========

calibre is an e-book manager. It can view, convert, edit and catalog e-books 
in all of the major e-book formats. It can also talk to e-book reader 
devices. It can go out to the internet and fetch metadata for your books. 
It can download newspapers and convert them into e-books for convenient 
reading. It is cross platform, running on Linux, Windows and OS X.

For more information, see the [calibre About page](https://calibre-ebook.com/about)

[![Build Status](https://api.travis-ci.org/kovidgoyal/calibre.svg)](https://travis-ci.org/kovidgoyal/calibre)

Screenshots
-------------
[Screenshots page](https://calibre-ebook.com/demo)

Usage
-------
See the [User Manual](https://manual.calibre-ebook.com)

Development
-------------
[Setting up a development environment for calibre](https://manual.calibre-ebook.com/develop.html)


A [tarball of the source code](https://calibre-ebook.com/dist/src) for the 
current calibre release.

Bugs
------

Bug reports and feature requests should be made in the calibre bug tracker at [launchpad](https://bugs.launchpad.net/calibre).
GitHub is only used for code hosting and pull requests.

Support calibre
----------------

calibre is a result of the efforts of many volunteers from all over the world.
If you find it useful, please consider contributing to support its development.
[Donate to support calibre development](https://calibre-ebook.com/donate).

