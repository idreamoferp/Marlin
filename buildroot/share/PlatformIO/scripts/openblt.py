#
# Convert the ELF to an SREC file suitable for some bootloaders
#
import pioutil
if pioutil.is_pio_build():
<<<<<<< HEAD
	import os,sys
	from os.path import join

	Import("env")

	board = env.BoardConfig()
	board_keys = board.get("build").keys()
	if 'encode' in board_keys:
		env.AddPostAction(
			join("$BUILD_DIR", "${PROGNAME}.bin"),
			env.VerboseAction(" ".join([
				"$OBJCOPY", "-O", "srec",
				"\"$BUILD_DIR/${PROGNAME}.elf\"", "\"" + join("$BUILD_DIR", board.get("build.encode")) + "\""
			]), "Building " + board.get("build.encode"))
		)
=======
    from os.path import join

    Import("env")

    board = env.BoardConfig()
    board_keys = board.get("build").keys()
    if 'encode' in board_keys:
        env.AddPostAction(
            join("$BUILD_DIR", "${PROGNAME}.bin"),
            env.VerboseAction(" ".join([
                "$OBJCOPY", "-O", "srec",
                "\"$BUILD_DIR/${PROGNAME}.elf\"", "\"" + join("$BUILD_DIR", board.get("build.encode")) + "\""
            ]), "Building " + board.get("build.encode"))
        )
>>>>>>> e49c3dc0889f1a6b597701ceb69624bdf4365445
