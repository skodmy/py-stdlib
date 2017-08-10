# -*- coding: utf-8 -*-
import sys
import os
import collections
import importlib
import pickle

STDLIB_MODULES_NAMES_GROUPS = {
    'string and text processing services': [
        'string', 're', 'difflib', 'StringIO', 'cStringIO', 'textwrap', 'unicodedata', 'stringprep', 'readline',
        'rlcompleter', 'fpformat',
    ],
    'binary data services': [
        'struct', 'codecs',
    ],
    'data types': [
        'datetime', 'calendar', 'collections', 'collections.abc', 'heapq', 'bisect', 'array', 'sets', 'mutex',
        'Queue', 'weakref', 'UserDict', 'UserList', 'UserString', 'types', 'new', 'copy', 'pprint', 'repr', 'reprlib',
        'enum',
    ],
    'numeric and mathematical modules': [
        'numbers', 'math', 'cmath', 'decimal', 'fractions', 'random', 'statistics',
    ],
    'functional programming modules': [
        'itertools', 'functools', 'operator',
    ],
    'file and directory': [
        'pathlib', 'os.path', 'fileinput', 'stat', 'statvfs', 'filecmp', 'tempfile', 'glob', 'fnmatch', 'linecache',
        'shutil', 'dircache', 'macpath',
    ],
    'data persistence': [
        'pickle', 'cPickle', 'copy_reg', 'copyreg', 'shelve', 'marshal', 'anydbm', 'whichdbm', 'dbm', 'gdbm',
        'dbhash', 'bsddb', 'dumbdbm', 'sqlite3',
    ],
    'data compression and archiving': [
        'zlib', 'gzip', 'bz2', 'lzma', 'zipfile', 'tarfile',
    ],
    'file formats': [
        'csv', 'ConfigParser', 'configparser', 'robotparser', 'netrc', 'xdrlib', 'plistlib',
    ],
    'cryptographic services': [
        'hashlib', 'hmac', 'md5', 'sha', 'secrets',
    ],
    'generic operating system services': [
        'os', 'io', 'time', 'argparse', 'optparse', 'getopt', 'logging', 'logging.config', 'logging.handlers',
        'getpass', 'curses', 'curses.textpad', 'curses.ascii', 'curses.panel', 'platform', 'errno', 'ctypes',
    ],
    'concurrent execution': [
        'threading', 'thread', 'multiprocessing', 'concurrent.futures.thread', 'concurrent.futures.process',
        'subprocess', 'sched', 'queue', 'dummy_threading', 'dummy_thread', '_thread', '_dummy_thread',
    ],
    'interprocess communication and networking': [
        'socket', 'ssl', 'select', 'selectors', 'asyncio', 'asyncore', 'asynchat', 'signal', 'popen2', 'mmap',
    ],
    'internet data handling': [
        'email', 'json', 'mailcap', 'mailbox', 'mhlib', 'mimetools', 'mimetypes', 'MimeWriter', 'mimify', 'multifile',
        'rfc822', 'base64', 'binhex', 'binascii', 'quopri', 'uu',
    ],
    'structured markup processing tools': [
        'HTMLParser', 'sgmllib', 'htmllib', 'htmlentitydefs', 'html', 'html.parser', 'html.entities',
        'xml.etree.ElementTree', 'xml.dom', 'xml.dom.minidom', 'xml.dom.pulldom', 'xml.sax', 'xml.sax.handler',
        'xml.sax.saxutils', 'xml.sax.xmlreader', 'xml.parsers.expat',
    ],
    'internet protocols and support': [
        'webbrowser', 'cgi', 'cgitb', 'wsgiref', 'urllib', 'urllib2', 'httplib', 'urllib.request', 'urllib.response',
        'urllib.parse', 'urllib.error', 'urllib.robotparser', 'http', 'http.client', 'ftplib', 'poplib', 'imaplib',
        'nntplib', 'smtplib', 'smtpd', 'telnetlib', 'uuid', 'urlparse', 'SocketServer', 'BaseHttpServer',
        'SimpleHttpServer', 'CGIHttpServer', 'cookielib', 'Cookie', 'xmlrpclib', 'SimpleXMLRPCServer',
        'DocXMLRPCServer', 'socketserver', 'http.server', 'http.cookies', 'http.cookiejar', 'xmlrpc', 'xmlrpc.client',
        'xmlrpc.server', 'ipaddress',
    ],
    'multimedia services': [
        'audioop', 'imageop', 'aifc', 'sunau', 'wave', 'chunk', 'colorsys', 'imghdr', 'sndhdr', 'ossaaudiodev',
    ],
    'internationalization': [
        'gettext', 'locale',
    ],
    'program frameworks': [
        'turtle', 'cmd', 'shlex',
    ],
    'graphical user interfaces with tk': [
        'Tkinter', 'ttk', 'Tix', 'ScrolledText', 'tkinter', 'tkinter.ttk', 'tkinter.tix', 'tkinter.scrolledtext',
        'idlelib',
    ],
    'development tools': [
        'typing', 'pydoc', 'doctest', 'unittest', 'unittest.mock', 'lib2to3', 'test', 'test.support',
    ],
    'debugging and profiling': [
        'bdb', 'faulthandler', 'pdb', 'profile', 'cProfile', 'hotshot', 'pstats', 'timeit', 'trace', 'tracemalloc',
    ],
    'software packaging and distribution': [
        'distutils', 'ensurepip', 'venv', 'zipapp',
    ],
    'python runtime services': [
        'sys', 'sysconfig', '__builtin__', 'future_builtins', 'builtins', '__main__', 'warnings', 'contextlib', 'abc',
        'atexit', 'traceback', '__future__', 'gc', 'inspect', 'site', 'user', 'fpectl',
    ],
    'custom python interpreters': [
        'code', 'codeop',
    ],
    'restricted execution': [
        'rexec', 'Bastion',
    ],
    'importing modules': [
        'imp', 'importlib', 'imputil', 'zipimport', 'pkgutil', 'modulefinder', 'runpy',
    ],
    'python language services': [
        'parser', 'ast', 'symtable', 'symbol', 'token', 'keyword', 'tokenize', 'tabnanny', 'pyclbr', 'py_compile',
        'compileall', 'dis', 'pickletools',
    ],
    'python compiler package': [
        'compiler', 'compiler.ast', 'compiler.consts', 'compiler.future', 'compiler.misc', 'compiler.pyassem',
        'compiler.pycodegen', 'compiler.symbols', 'compiler.transformer', 'compiler.visitor',
    ],
    'miscellaneous services': [
        'formatter',
    ],
    'superseded modules': [
        'optparse', 'imp',
    ],
    'undocumented modules': [
        'ihooks', 'ntpath', 'posixpath', 'bsddb185', 'audiodev', 'linuxaudiodev', 'sunaudio', 'toaiff', 'applesingle',
        'buildtools', 'cfmfile', 'icopen', 'macerrors', 'macresource', 'Nav', 'PixMapWrapper', 'videoreader', 'W',
        'timing', 'cl', 'sv',
    ],
}

MS_WINDOWS_MODULES_NAMES_GROUPS = {
    'mS windows specific services': ['msilib', 'msvcrt', '_winreg', 'winreg', 'winsound', ],
}

UNIX_MODULES_NAMES_GROUPS = {
    'unix specific services': [
        'posix', 'pwd', 'spwd', 'grp', 'crypt', 'dl', 'termios', 'tty', 'pty', 'fcntl', 'pipes', 'posixfile',
        'resource', 'nis', 'syslog', 'commands',
    ],
}

MAC_OS_X_MODULES_NAMES_GROUPS = {
    'mac oS x specific services': [
        'ic', 'MacOS', 'macostools', 'findertools', 'EasyDialogs', 'FrameWork', 'autoGIL', 'Carbon', 'Carbon.AE',
        'Carbon.AH', 'Carbon.App', 'Carbon.Appearance', 'Carbon.CF', 'Carbon.CG', 'Carbon.CarbonEvt',
        'Carbon.CarbonEvents', 'Carbon.Cm', 'Carbon.Components', 'Carbon.ControlAccessor', 'Carbon.Controls',
        'Carbon.CoreFounation', 'Carbon.CoreGraphics', 'Carbon.Ctl', 'Carbon.Dialogs', 'Carbon.Dlg', 'Carbon.Drag',
        'Carbon.Dragconst', 'Carbon.Events', 'Carbon.Evt', 'Carbon.File', 'Carbon.Files', 'Carbon.Fm', 'Carbon.Folder',
        'Carbon.Folders', 'Carbon.Fonts', 'Carbon.Help', 'Carbon.IBCarbon', 'Carbon.IBCarbonRuntime', 'Carbon.Icn',
        'Carbon.Icons', 'Carbon.Launch', 'Carbon.LaunchServices', 'Carbon.List', 'Carbon.Lists', 'Carbon.MacHelp',
        'Carbon.MediaDescr', 'Carbon.Menu', 'Carbon.Menus', 'Carbon.Mlte', 'Carbon.OSA', 'Carbon.OSAconst',
        'Carbon.QDOffscreen', 'Carbon.Qd', 'Carbon.Qdoffs', 'Carbon.Qt', 'Carbon.QuickDraw', 'Carbon.QuickTime',
        'Carbon.Res', 'Carbon.Resources', 'Carbon.Scrap', 'Carbon.Snd', 'Carbon.Sound', 'Carbon.TE', 'Carbon.TextEdit',
        'Carbon.Win', 'Carbon.Windows', 'ColorPicker',
    ],
    'macPython oSA modules': [
        'gensuitemodule', 'aetools', 'aepack', 'aetypes', 'MiniAEFrame',
    ],
}

SGI_IRIX_MODULES_NAMES_GROUPS = {
    'sGI iRIX specific services': [
        'al', 'AL', 'cd', 'fl', 'FL', 'flp', 'fm', 'gl', 'DEVICE', 'GL', 'imgfile', 'jpeg',
    ],
}

SUN_OS_MODULES_NAMES_GROUPS = {
    'sunOS specific services': [
        'sunaudiodev', 'SUNAUDIODEV',
    ],
}

CACHE_DIRECTORY = os.path.join(os.environ['HOME'], '.py-in-stdlib-searcher')
CACHE_FILENAME = 'search_cache{}.cch'
CACHE_SIZE = 100
CACHE = collections.deque()

# updating standard library modules names groups dictionary with platform specific modules names groups
if sys.platform.startswith('win') or sys.platform.startswith('cygwin'):
    STDLIB_MODULES_NAMES_GROUPS.update(MS_WINDOWS_MODULES_NAMES_GROUPS)
elif sys.platform.startswith('linux'):
    STDLIB_MODULES_NAMES_GROUPS.update(UNIX_MODULES_NAMES_GROUPS)

# updating standard library modules names groups dictionary due to python version
if sys.version_info[0] == 2:
    STDLIB_MODULES_NAMES_GROUPS.pop('superseded modules', None)
    if sys.platform.startswith('darwin') or sys.platform.startswith('mac'):
        STDLIB_MODULES_NAMES_GROUPS.update(MAC_OS_X_MODULES_NAMES_GROUPS)
    elif sys.platform.startswith('sgi') or sys.platform.find('irix') != -1:
        STDLIB_MODULES_NAMES_GROUPS.update(SGI_IRIX_MODULES_NAMES_GROUPS)
    elif sys.platform.startswith('sunos'):
        STDLIB_MODULES_NAMES_GROUPS.update(SUN_OS_MODULES_NAMES_GROUPS)
    STDLIB_MODULES_NAMES_GROUPS['string and text processing services'].extend(
        STDLIB_MODULES_NAMES_GROUPS['binary data services']
    )
    STDLIB_MODULES_NAMES_GROUPS.pop('binary data services', None)
    STDLIB_MODULES_NAMES_GROUPS['numeric and mathematical modules'].extend(
        STDLIB_MODULES_NAMES_GROUPS['functional programming modules']
    )
    STDLIB_MODULES_NAMES_GROUPS.pop('functional programming modules', None)
    CACHE_FILENAME = CACHE_FILENAME.format('2')
elif sys.version_info[0] == 3:
    STDLIB_MODULES_NAMES_GROUPS.pop('restricted execution', None)
    STDLIB_MODULES_NAMES_GROUPS.pop('python compiler package', None)
    CACHE_FILENAME = CACHE_FILENAME.format('3')


def remove_from_groups_names_of_unavailable_modules(src=STDLIB_MODULES_NAMES_GROUPS):
    """
    Removes from modules names groups dictionary names of unavailable modules.
    
    :param src: modules names groups dictionary source.
    :return: None.
    """
    for group_name in src:
        objects_to_remove = []
        for module_name in src[group_name]:
            try:
                importlib.import_module(module_name)
            except ImportError:
                objects_to_remove.append(module_name)
        for object_to_remove in objects_to_remove:
            src[group_name].remove(object_to_remove)


# calling here for better code look
remove_from_groups_names_of_unavailable_modules()


def extract_modules_names_group_by(keyword, src=STDLIB_MODULES_NAMES_GROUPS):
    """
    Extracts a modules names group by a given keyword. It's a generator.
    
    :param keyword: the keyword that specifies the group.
    :param src: modules names groups dictionary source.
    :return: next extracted modules names group like a dictionary.
    """
    for group_name in src:
        if group_name.lower().find(keyword.lower()) != -1:
            yield {group_name: src[group_name]}


def print_groups_of_modules_names(src=STDLIB_MODULES_NAMES_GROUPS):
    """
    Prints groups of modules names.
    
    :param src: modules names groups dictionary source.
    :return: None.
    """
    modules_names_groups_delimiter = '=' * 50
    module_name_print_pattern = "— {}".rjust(10)
    for key in src:
        print(modules_names_groups_delimiter)
        print(key.title() + ':')
        for item in src[key]:
            print(module_name_print_pattern.format(item))
        print(modules_names_groups_delimiter)


def add_to_cache(items, dst=CACHE, max_items=CACHE_SIZE):
    """
    Adds items to cache.
    
    :param items: a single or a sequence of objects to add.
    :param dst: a cache's destination.
    :param max_items: a maximum number of items that can be added to cache.
    :return: None.
    """
    if not isinstance(items, (tuple, list)):
        items = items,
    for item in items:
        if item in dst:
            dst.remove(item)
        if len(dst) >= max_items:
            dst.pop()
        dst.appendleft(item)


def save_cache(src=CACHE, directory=CACHE_DIRECTORY, filename=CACHE_FILENAME):
    """
    Saves a cache in a file on a hard drive.
    
    :param src: a cache's source.
    :param directory: path to directory in which a cache file will be located.
    :param filename: name of a file in which cache will be saved.
    :return: None.
    """
    pth = os.path.join(directory, filename)
    if not os.path.exists(directory):
        return
    with open(pth, 'wb') as cache_file:
        pickle.dump(src, cache_file)


def load_cache(directory=CACHE_DIRECTORY, filename=CACHE_FILENAME):
    """
    Loads a cache from a file on a hard drive.
    
    :param directory: path to directory in which cache file is located.
    :param filename: cache file's name.
    :return: an "unpickled" deque object.
    """
    pth = os.path.join(directory, filename)
    if not os.path.exists(pth) or not os.path.isfile(pth):
        return collections.deque()
    with open(pth, 'rb') as cache_file:
        return pickle.load(cache_file)


def are_equal(name0, name1):
    """
    Checks if names are equal.
    
    :param name0: must be a string or an object which has __name__ attribute.
    :param name1: must be a string
    :return: True if names are equal, False otherwise.
    """
    return name0.__name__ if hasattr(name0, '__name__') else name0 == name1


def are_similar(name0, name1):
    """
    Checks if names are similar.

    :param name0: must be a string or an object which has __name__ attribute.
    :param name1: must be a string
    :return: True if name0 contains name1, False otherwise.
    """
    return name0.__name__ if hasattr(name0, '__name__') else name0.find(name1) != -1


def search_in_modules_names_groups(name, condition_for_names=are_equal, src=STDLIB_MODULES_NAMES_GROUPS, first=True):
    """
    Searches an object with a given name in a dictionary.
    
    :param name: searched object's name.
    :param condition_for_names: a callback that must return a boolean value which indicates that the object was found.
    :param src: a source for searching, must be a dictionary.
    :param first: a boolean flag that indicates to return only the first searched object or not.
    :return: a list with found objects.
    """
    for group_name in src:
        for module_name in src[group_name]:
            try:
                mdl = importlib.import_module(module_name)
                mdl_items = mdl.__all__ if hasattr(mdl, '__all__') else mdl.__dict__
                for mdl_item in mdl_items:
                    if condition_for_names(mdl_item, name):
                        yield getattr(mdl, mdl_item)
                        if first:
                            return
            except ImportError:
                continue


def search_in_cache(name, condition_for_names=are_equal, src=CACHE, first=True):
    """
    Searches an object with a given name in a cache.
    
    :param name: searched object's name.
    :param condition_for_names: a callback that must return a boolean value which indicates that the object was found.
    :param src: a source for searching.
    :param first: a boolean flag that indicates to return only the first searched object or not.
    :return: a list with found objects.
    """
    for cached_item in src:
        if hasattr(cached_item, '__name__'):
            if condition_for_names(cached_item.__name__, name):
                yield cached_item
                if first:
                    return


def search(name, condition_for_names, cache, modules_names_groups, first_only):
    """
    Searches an object with a given name. 
    
    First tries to find it in a cache and, if it wasn't found, searches in a provided dictionary.
    
    :param name: searched object's name.
    :param condition_for_names: a callback that must return a boolean value which indicates that the object was found.
    :param cache: a deque object which contains results of previous searches.
    :param modules_names_groups: a dictionary which will be used for searching if the object was not found in the cache. 
    :param first_only: a boolean flag that indicates to return only the first searched object or not.
    :return: a list with found objects.
    """
    if not first_only:
        return list(search_in_modules_names_groups(name, condition_for_names, modules_names_groups, first_only))
    search_results = list(search_in_cache(name, condition_for_names, cache, first_only))
    if len(search_results) == 0:
        search_results = search_in_modules_names_groups(name, condition_for_names, modules_names_groups, first_only)
    return list(search_results)


def print_search_results(src):
    """
    Prints search results. For printing chose each result object's __name__, __class__, __module__ attributes.
    
    If the result object hasn't some of the listed attributes then they will be replaced by defaults or 'undefined'.
    
    :param src: 
    :return: None.
    """
    for search_result in src:
        print("{} {} found in {}".format(
            search_result.__name__ if hasattr(search_result, '__name__') else search_result.__class__.__name__,
            search_result.__class__.__name__
            if hasattr(search_result, '__class__') and hasattr(search_result.__class__, '__name__') else 'undefined',
            search_result.__module__ if hasattr(search_result, '__module__') else 'builtins'
        ))


def print_info_about(objects, wanted_attributes_names=('__name__', '__module__', '__doc__')):
    """
    Prints information about each object in objects.
    
    :param objects: a single object or a tuple or a list of objects to print information about.
    :param wanted_attributes_names: attributes of each object which you want to print.
    :return: None.
    """
    if not isinstance(objects, (list, tuple)):
        objects = objects,
    obj_delimiter_pattern = "=" * 120
    obj_attr_delimiter_pattern = "-" * 120
    obj_attr_print_template = "{}: {}"
    for obj in objects:
        print(obj_delimiter_pattern)
        for wanted_attr_name in wanted_attributes_names:
            obj_attr_print_pattern = obj_attr_print_template.format(wanted_attr_name.strip('_').upper(), '{}')
            wanted_attr_value = getattr(obj, wanted_attr_name) if hasattr(obj, wanted_attr_name) else 'undefined'
            print(obj_attr_delimiter_pattern)
            if wanted_attr_value.find('\n') != -1:
                print(obj_attr_print_pattern.format('\n{}').format(wanted_attr_value))
            else:
                print(obj_attr_print_pattern.format(wanted_attr_value))
            print(obj_attr_delimiter_pattern)
        print(obj_delimiter_pattern)


def __parse_args():
    """
    Parse command-line arguments. For internal use only.
    
    :return: parsed command-line arguments.
    """
    from argparse import ArgumentParser
    args_parser = ArgumentParser()
    args_parser.add_argument("-l", metavar="group's name", type=str, nargs='*',
                             help="list all or a single group of modules names")
    args_parser.add_argument("-s", metavar='name', type=str, nargs='+',
                             help="search an object in stdlib with specified name")
    args_parser.add_argument("-g", metavar="keyword", type=str, nargs='+', help="select groups for search by keyword")
    args_parser.add_argument("-i", metavar='name', type=str, nargs='+',
                             help="show info about object with specified name")
    args_parser.add_argument("-a", "--all", action='store_true', help="all flag for listing or search")
    args_parser.add_argument("-e", "--extended", action='store_true', help="extended search that include similar items")
    return args_parser.parse_args()


def __main():
    """
    Script's __main__. For internal use only.
    
    :return: None.
    """
    # here goes initialization section
    if not os.path.exists(CACHE_DIRECTORY):
        os.mkdir(CACHE_DIRECTORY)
    global CACHE
    CACHE.extend(load_cache())
    # here goes arguments parsing section
    parsed_args = __parse_args()
    # here goes sections which execute code due to arguments provided for script
    # here goes listing section
    if parsed_args.l is not None:
        if len(parsed_args.l) == 0 or parsed_args.all:
            print_groups_of_modules_names()
        else:
            for keyword in parsed_args.l:
                for modules_names_group in extract_modules_names_group_by(keyword):
                    print_groups_of_modules_names(modules_names_group)
    # here goes search section
    if parsed_args.s is not None:
        cond_4names = are_similar if parsed_args.extended else are_equal
        first = not parsed_args.all
        modules_names_groups = STDLIB_MODULES_NAMES_GROUPS
        if parsed_args.g is not None:
            modules_names_groups = {}
            for modules_names_group_name in parsed_args.g:
                for modules_names_group in extract_modules_names_group_by(modules_names_group_name):
                    modules_names_groups.update(modules_names_group)
        for name_for_search in parsed_args.s:
            search_results = search(name_for_search, cond_4names, CACHE, modules_names_groups, first)
            print_search_results(search_results)
            add_to_cache(search_results)
        save_cache()
    # here goes info section
    if parsed_args.i is not None:
        for obj_full_name in parsed_args.i:
            obj_full_name = obj_full_name.split(".")
            if len(obj_full_name) == 1:
                print("full name must be specified, for example 're.match'")
                continue
            mdl_attr_name = obj_full_name.pop()
            mdl_name = ".".join(obj_full_name)
            mdl = importlib.import_module(mdl_name)
            if not hasattr(mdl, mdl_attr_name):
                print("module {} has not attribute with name '{}'".format(mdl_name, mdl_attr_name))
                continue
            print_info_about(getattr(mdl, mdl_attr_name))


if __name__ == '__main__':
    __main()
