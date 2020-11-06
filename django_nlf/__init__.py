def __read_version_from_env():
    """
        Attempts to read the version information from the DJANGO_NLF_VERSION environment
        variable. Returns 'latest' if nothing found.
    """
    import os

    version = os.environ.get('DJANGO_NLF_VERSION', 'latest')
    if version.startswith('refs/tags/'): # $GITHUB_REF in github actions
        return version[10:]

    return version


__version__ = __read_version_from_env()
