# py-stdlib-librarian
A command-line utility which is primarily designed for fast searching of an object in the Python's standard library.
Also it provides some other features like listing of the standard library's contents and displaying information about an object from the standard library.

## Python version
Works on both python2.7.x and python3.x.x versions.

## Usage
    usage: stdliblibrarian.py [-h] [-l [group's name [group's name ...]]]
                          [-s name [name ...]] [-g keyword [keyword ...]]
                          [-i name [name ...]] [-a] [-e]

    optional arguments:
      -h, --help            show this help message and exit
      -l [group's name [group's name ...]]
                            list all or a single group of modules names
      -s name [name ...]    search an object in stdlib with specified name
      -g keyword [keyword ...]
                            select groups for search by keyword
      -i name [name ...]    show info about object with specified name
      -a, --all             all flag for listing or search
      -e, --extended        extended search that include similar items

## Usage examples
### Listing the standard library's contents
1. Listing all contents:

    python stdliblibrarian.py -l
    ==================================================
    String And Text Processing Services:
          — string
          — re
          — difflib
          — textwrap
          — unicodedata
          — stringprep
          — readline
          — rlcompleter
    ==================================================
    ==================================================
    Binary Data Services:
          — struct
          — codecs
    ==================================================
    ==================================================
    Data Types:
          — datetime
          — calendar
          — collections
          — collections.abc
          — heapq
          — bisect
          — array
          — weakref
          — types
          — copy
          — pprint
          — reprlib
          — enum
    ==================================================
    ==================================================
    Numeric And Mathematical Modules:
          — numbers
          — math
          — cmath
          — decimal
          — fractions
          — random
          — statistics
    ==================================================
    ==================================================
    Functional Programming Modules:
          — itertools
          — functools
          — operator
    ==================================================
    ==================================================
    File And Directory:
          — pathlib
          — os.path
          — fileinput
          — stat
          — filecmp
          — tempfile
          — glob
          — fnmatch
          — linecache
          — shutil
          — macpath
    ==================================================
    ==================================================
    Data Persistence:
          — pickle
          — copyreg
          — shelve
          — marshal
          — dbm
          — sqlite3
    ==================================================
    ==================================================
    Data Compression And Archiving:
          — zlib
          — gzip
          — bz2
          — lzma
          — zipfile
          — tarfile
    ==================================================
    ==================================================
    File Formats:
          — csv
          — configparser
          — netrc
          — xdrlib
          — plistlib
    ==================================================
    ==================================================
    Cryptographic Services:
          — hashlib
          — hmac
          — secrets
    ==================================================
    ==================================================
    Generic Operating System Services:
          — os
          — io
          — time
          — argparse
          — optparse
          — getopt
          — logging
          — logging.config
          — logging.handlers
          — getpass
          — curses
          — curses.textpad
          — curses.ascii
          — curses.panel
          — platform
          — errno
          — ctypes
    ==================================================
    ==================================================
    Concurrent Execution:
          — threading
          — multiprocessing
          — concurrent.futures.thread
          — concurrent.futures.process
          — subprocess
          — sched
          — queue
          — dummy_threading
          — _thread
          — _dummy_thread
    ==================================================
    ==================================================
    Interprocess Communication And Networking:
          — socket
          — ssl
          — select
          — selectors
          — asyncio
          — asyncore
          — asynchat
          — signal
          — mmap
    ==================================================
    ==================================================
    Internet Data Handling:
          — email
          — json
          — mailcap
          — mailbox
          — mimetypes
          — base64
          — binhex
          — binascii
          — quopri
          — uu
    ==================================================
    ==================================================
    Structured Markup Processing Tools:
          — html
          — html.parser
          — html.entities
          — xml.etree.ElementTree
          — xml.dom
          — xml.dom.minidom
          — xml.dom.pulldom
          — xml.sax
          — xml.sax.handler
          — xml.sax.saxutils
          — xml.sax.xmlreader
          — xml.parsers.expat
    ==================================================
    ==================================================
    Internet Protocols And Support:
          — webbrowser
          — cgi
          — cgitb
          — wsgiref
          — urllib
          — urllib.request
          — urllib.response
          — urllib.parse
          — urllib.error
          — urllib.robotparser
          — http
          — http.client
          — ftplib
          — poplib
          — imaplib
          — nntplib
          — smtplib
          — smtpd
          — telnetlib
          — uuid
          — socketserver
          — http.server
          — http.cookies
          — http.cookiejar
          — xmlrpc
          — xmlrpc.client
          — xmlrpc.server
          — ipaddress
    ==================================================
    ==================================================
    Multimedia Services:
          — audioop
          — aifc
          — sunau
          — wave
          — chunk
          — colorsys
          — imghdr
          — sndhdr
    ==================================================
    ==================================================
    Internationalization:
          — gettext
          — locale
    ==================================================
    ==================================================
    Program Frameworks:
          — turtle
          — cmd
          — shlex
    ==================================================
    ==================================================
    Graphical User Interfaces With Tk:
          — tkinter
          — tkinter.ttk
          — tkinter.tix
          — tkinter.scrolledtext
          — idlelib
    ==================================================
    ==================================================
    Development Tools:
          — typing
          — pydoc
          — doctest
          — unittest
          — unittest.mock
          — lib2to3
          — test
          — test.support
    ==================================================
    ==================================================
    Debugging And Profiling:
          — bdb
          — faulthandler
          — pdb
          — profile
          — cProfile
          — pstats
          — timeit
          — trace
          — tracemalloc
    ==================================================
    ==================================================
    Software Packaging And Distribution:
          — distutils
          — ensurepip
          — venv
          — zipapp
    ==================================================
    ==================================================
    Python Runtime Services:
          — sys
          — sysconfig
          — builtins
          — __main__
          — warnings
          — contextlib
          — abc
          — atexit
          — traceback
          — __future__
          — gc
          — inspect
          — site
    ==================================================
    ==================================================
    Custom Python Interpreters:
          — code
          — codeop
    ==================================================
    ==================================================
    Importing Modules:
          — imp
          — importlib
          — zipimport
          — pkgutil
          — modulefinder
          — runpy
    ==================================================
    ==================================================
    Python Language Services:
          — parser
          — ast
          — symtable
          — symbol
          — token
          — keyword
          — tokenize
          — tabnanny
          — pyclbr
          — py_compile
          — compileall
          — dis
          — pickletools
    ==================================================
    ==================================================
    Miscellaneous Services:
          — formatter
    ==================================================
    ==================================================
    Superseded Modules:
          — optparse
          — imp
    ==================================================
    ==================================================
    Undocumented Modules:
          — ntpath
          — posixpath
    ==================================================
    ==================================================
    Unix Specific Services:
          — posix
          — pwd
          — spwd
          — grp
          — crypt
          — termios
          — tty
          — pty
          — fcntl
          — pipes
          — resource
          — nis
          — syslog
    ==================================================

2. Listing content of a specific group:
    python stdliblibrarian.py -l string
    ==================================================
    String And Text Processing Services:
          — string
          — re
          — difflib
          — textwrap
          — unicodedata
          — stringprep
          — readline
          — rlcompleter
    ==================================================

### Search
1. Simple search

    python stdliblibrarian.py -s match
    match function found in re

2. Simple search of multiple items

    python stdliblibrarian.py -s match compile fullmatch
    match function found in re
    compile function found in re
    fullmatch function found in re

2. Simple search within a specified group

    python stdliblibrarian.py -s fullmatch -g text
    fullmatch function found in re

3. Simple search within a specified groups

    python stdliblibrarian.py -s compile -g string language
    compile function found in py_compile

4. Simple search of multiple items within a specified groups

    python stdliblibrarian.py -s compile match -g string language
    compile function found in py_compile
    match function found in re

5. Extended search

    python stdliblibrarian.py -es ru
    run function found in subprocess

6. Extended search of multiple items within multiple groups

    python stdliblibrarian.py -es ru call -g subproc str
    run function found in subprocess
    SSLSyscallError type found in ssl

7. Search all

    python stdliblibrarian.py -as compile
    compile function found in re
    compile builtin_function_or_method found in builtins
    compile function found in py_compile

8. Search all within specified groups

    python stdliblibrarian.py -as run -g conc net
    run function found in subprocess

8. Extended search all

    python stdliblibrarian.py -eas compl
    set_completer builtin_function_or_method found in readline
    get_completer builtin_function_or_method found in readline
    get_completion_type builtin_function_or_method found in readline
    set_completer_delims builtin_function_or_method found in readline
    get_completer_delims builtin_function_or_method found in readline
    set_completion_display_matches_hook builtin_function_or_method found in readline
    complete_statement builtin_function_or_method found in _sqlite3
    IncompleteReadError type found in asyncio.streams
    as_completed function found in asyncio.tasks
    Incomplete type found in binascii
    IncompleteRead type found in http.client
    complex type found in builtins
    enablerlcompleter function found in site

10. Extended search all within specified groups

    python stdliblibrarian.py -eas run -g conc net
    run function found in subprocess
    _set_running_loop function found in asyncio.events
    _get_running_loop function found in asyncio.events
    LimitOverrunError type found in asyncio.streams
    run_coroutine_threadsafe function found in asyncio.tasks
