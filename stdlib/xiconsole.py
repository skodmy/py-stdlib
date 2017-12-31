"""
This module provides an interactive console which is extended with inspection extension.

This console also can be extended with custom extensions.
"""
import abc
import code
import collections
import inspect
import pprint
import sys


def is_module_member(obj):
    # TODO add constant check
    return (inspect.isclass(obj) or inspect.isfunction(obj)) and not inspect.isbuiltin(obj)


class StandardLibraryCursor:
    """
    Python Standard Library cursor.
    """

    def __init__(self):
        self.queries = []

    @staticmethod
    def prepare(query):
        """
        Prepares a query string from a given raw string.

        :param query: a raw string from which the new query will be prepared.
        :return: the query string.
        """
        query = query.split('.')
        if len(query) >= 2:
            return 'from {} import {}'.format('.'.join(query[:-1]), query[-1])
        else:
            return 'import {}'.format(query[0])

    @staticmethod
    def execute(query):
        """
        Executes a given query string.

        :param query: a string that represents a query.
        :return: query execution result.
        """
        glbls = globals()
        name = query.replace('import', '').replace('from', '').strip().split(' ')[-1]
        if name in glbls:
            return glbls[name]
        try:
            exec(query, glbls)
        except OSError:
            print('load error')
        else:
            return glbls[name]

    def fetch(self, query):
        """
        Fetches a query. Is a shortcut for 'self.execute(self.prepare(query))'

        :param query:
        :return:
        """
        assert isinstance(query, str)
        return self.execute(self.prepare(query))

    def prep(self, q):
        self.queries.append(self.prepare(q))

    def exec(self):
        self.execute(self.queries.pop())


class ExtendedInteractiveConsoleExtension(abc.ABC):
    COMMAND_PREFIX = ''
    COMMAND_SUFFIX = ''
    commands_map = collections.defaultdict(lambda: lambda *args, **kwargs: 'command not found')
    commands_map.setdefault('q', sys.exit)

    def register(self, command, handler):
        self.commands_map.setdefault(command, handler)

    @abc.abstractmethod
    def is_acceptable(self, cmd_str):
        return cmd_str.startswith(self.COMMAND_PREFIX) and cmd_str.endswith(self.COMMAND_SUFFIX)

    @abc.abstractmethod
    def parse(self, cmd_str):
        return cmd_str

    @abc.abstractmethod
    def run(self, command, *args, **kwargs):
        return command, args, kwargs


class ExtendedInteractiveConsoleInspectionExtension(ExtendedInteractiveConsoleExtension):
    COMMAND_PREFIX = '$'
    COMMAND_SUFFIX = '?'

    # TODO refactor
    def load(self, obj_name):
        if isinstance(obj_name, str):
            return self.cursor.fetch(obj_name)
        return obj_name

    def ls(self, obj):
        return inspect.getmembers(self.load(obj), getattr(inspect, 'is_module_member'))

    def what_is(self, obj):
        obj = self.load(obj)
        for k, v in inspect.getmembers(inspect, lambda m: inspect.isfunction(m) and m.__name__.startswith('is')):
            if v(obj):
                return obj, k
        return 'uninspectable'

    def info(self, obj):
        obj = self.load(obj)
        if inspect.isfunction(obj):
            # TODO complete
            return obj.__name__ + str(inspect.signature(obj))

    def __init__(self, cursor=None):
        """
        TODO document commands

        $ls module
        $i module.item
        item?

        TODO check if cursor parameter is needed

        :param cursor:
        """
        self.cursor = cursor if cursor else StandardLibraryCursor()
        self.register('ls', self.ls)
        self.register('?', self.what_is)
        self.register('i', self.info)

    def is_acceptable(self, cmd_str):
        return cmd_str.startswith(self.COMMAND_PREFIX) or cmd_str.endswith(self.COMMAND_SUFFIX)

    def parse(self, cmd_str):
        if cmd_str.endswith(self.COMMAND_SUFFIX):
            return cmd_str[-1], cmd_str[:-1]
        cmd_str = cmd_str.split(' ')
        cmd_str[0] = cmd_str[0].replace(self.COMMAND_PREFIX, '')
        return cmd_str

    def run(self, command, *args, **kwargs):
        return self.commands_map[command](*args, **kwargs)


class ExtendedInteractiveConsole(code.InteractiveConsole):
    """
    Extends a standard interactive python console with few more features.
    """
    def __init__(self, extensions=None):
        super().__init__()
        self.extensions = extensions if extensions else (ExtendedInteractiveConsoleInspectionExtension(), )

    def raw_input(self, prompt=""):
        raw_in = super().raw_input(prompt)
        for extension in self.extensions:
            if extension.is_acceptable(raw_in):
                command, *args = extension.parse(raw_in)
                pprint.pprint(extension.run(command, *args))
                self.resetbuffer()
                return 'pass'
        return raw_in


def main():
    setattr(inspect, 'is_module_member', is_module_member)
    # TODO suppress errors by restarting interactive console
    ExtendedInteractiveConsole().interact()


if __name__ == '__main__':
    main()
