# SPDX-License-Identifier: MIT

import sys
import os

import pep517
import pytest

import build
import build.__main__


if sys.version_info >= (3,):  # pragma: no cover
    build_open_owner = 'builtins'
else:  # pragma: no cover
    build_open_owner = 'build'


cwd = os.getcwd()
out = os.path.join(cwd, 'dist')


@pytest.mark.parametrize(
    ('cli_args', 'build_args'),
    [
        ([],            [cwd, out, ['sdist', 'wheel'], True, False]),
        (['-n'],        [cwd, out, ['sdist', 'wheel'], False, False]),
        (['-s'],        [cwd, out, ['sdist'], True, False]),
        (['-w'],        [cwd, out, ['wheel'], True, False]),
        (['source'],    ['source', out, ['sdist', 'wheel'], True, False]),
        (['-o', 'out'], [cwd, 'out', ['sdist', 'wheel'], True, False]),
        (['-x'],        [cwd, out, ['sdist', 'wheel'], True, True]),
    ]
)
def test_parse_args(mocker, cli_args, build_args):
    mocker.patch('build.__main__.build')

    build.__main__.main(cli_args)
    build.__main__.build.assert_called_with(*build_args)


def test_build(mocker):
    open_mock = mocker.mock_open(read_data='')
    mocker.patch('{}.open'.format(build_open_owner), open_mock)
    mocker.patch('importlib.import_module')
    mocker.patch('build.ProjectBuilder.check_depencencies')
    mocker.patch('build.ProjectBuilder.build')
    mocker.patch('build.__main__._error')
    mocker.patch('pep517.envbuild.BuildEnvironment.pip_install')

    build.ProjectBuilder.check_depencencies.side_effect = [[], ['something'], [], []]

    # isolation=True
    build.__main__.build('.', '.', ['sdist'])
    build.ProjectBuilder.build.assert_called_with('sdist', '.')

    # check_dependencies = []
    build.__main__.build('.', '.', ['sdist'], isolation=False)
    build.ProjectBuilder.build.assert_called_with('sdist', '.')
    pep517.envbuild.BuildEnvironment.pip_install.assert_called_with(set(build._DEFAULT_BACKEND['requires']))

    # check_dependencies = ['something']
    build.__main__.build('.', '.', ['sdist'], isolation=False)
    build.ProjectBuilder.build.assert_called_with('sdist', '.')
    build.__main__._error.assert_called_with('Missing dependencies:\n\tsomething')

    build.ProjectBuilder.build.side_effect = [build.BuildException, build.BuildBackendException]
    build.__main__._error.reset_mock()

    # BuildException
    build.__main__.build('.', '.', ['sdist'])
    build.__main__._error.assert_called_with('')

    build.__main__._error.reset_mock()

    # BuildBackendException
    build.__main__.build('.', '.', ['sdist'])
    build.__main__._error.assert_called_with('')
