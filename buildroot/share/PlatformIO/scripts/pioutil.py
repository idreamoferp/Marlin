#
# pioutil.py
#

# Make sure 'vscode init' is not the current command
def is_pio_build():
<<<<<<< HEAD
	from SCons.Script import DefaultEnvironment
	env = DefaultEnvironment()
	return not env.IsIntegrationDump()

def get_pio_version():
	from platformio import util
	return util.pioversion_to_intstr()
=======
    from SCons.Script import DefaultEnvironment
    env = DefaultEnvironment()
    return not env.IsIntegrationDump()

def get_pio_version():
    from platformio import util
    return util.pioversion_to_intstr()
>>>>>>> e49c3dc0889f1a6b597701ceb69624bdf4365445
