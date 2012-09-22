# Copyright (c) 2008-2012 testtools developers. See LICENSE for details.

"""All the matchers.

Matchers, a way to express complex assertions outside the testcase.

Inspired by 'hamcrest'.

Matcher provides the abstract API that all matchers need to implement.

Bundled matchers are listed in __all__: a list can be obtained by running
$ python -c 'import testtools.matchers; print testtools.matchers.__all__'
"""

__all__ = [
    'AfterPreprocessing',
    'AllMatch',
    'Annotate',
    'Contains',
    'ContainsAll',
    'DirExists',
    'DocTestMatches',
    'EndsWith',
    'Equals',
    'FileContains',
    'FileExists',
    'GreaterThan',
    'HasPermissions',
    'Is',
    'IsInstance',
    'KeysEqual',
    'LessThan',
    'MatchesAll',
    'MatchesAny',
    'MatchesException',
    'MatchesListwise',
    'MatchesPredicate',
    'MatchesRegex',
    'MatchesSetwise',
    'MatchesStructure',
    'NotEquals',
    'Not',
    'PathExists',
    'Raises',
    'raises',
    'SamePath',
    'StartsWith',
    'TarballContains',
    ]

from ._basic import (
    Contains,
    EndsWith,
    Equals,
    GreaterThan,
    Is,
    IsInstance,
    LessThan,
    MatchesRegex,
    NotEquals,
    StartsWith,
    )
from ._datastructures import (
    ContainsAll,
    MatchesListwise,
    MatchesSetwise,
    MatchesStructure,
    )
from ._dict import (
    KeysEqual,
    )
from ._doctest import (
    DocTestMatches,
    )
from ._exception import (
    MatchesException,
    Raises,
    raises,
    )
from ._filesystem import (
    DirExists,
    FileContains,
    FileExists,
    HasPermissions,
    PathExists,
    SamePath,
    TarballContains,
    )
from ._higherorder import (
    AfterPreprocessing,
    AllMatch,
    Annotate,
    MatchesAll,
    MatchesAny,
    MatchesPredicate,
    Not,
    )

# XXX: These are not explicitly included in __all__.  It's unclear how much of
# the public interface they really are.
from ._impl import (
    Matcher,
    Mismatch,
    MismatchError,
    )