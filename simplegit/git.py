import subprocess
import shlex


class Git(object):
    def __init__(self, logger=None):
        self.logger = logger

    def __getattr__(self, key):
        """Proxy the attribute request to function that executes subprocess."""
        return self._func_for_key(key)

    def call(self, key, args_string, **kwargs):
        return self._func_for_key(key)(args_string, **kwargs)

    def _func_for_key(self, key):
        def proxy(cmd=None, **kwargs):
            args = ["git", key]
            if cmd:
                args.extend(shlex.split(cmd))
            process = subprocess.Popen(
                args,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            output, error = process.communicate()
            return output.splitlines(), process.returncode, error.splitlines()
        return proxy
