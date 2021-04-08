# WoWFileFormat
A set of tools ( both manual, and machine learning ) to allow for classification of internal WoW files.

Requires my PyCASC library.

## Uses

### Manuguess 

Provides a set of python scripts that allow for manually finding files by their "Header" string. This works fairly well, as most WoW files have a 4 character header that represents the extension

### MLGuess

This is a set of machine learning scripts that consume all known files as training data and use that to output possible (and might i say, very accurate) extensions and directories for unknown files.

Most of the meat of this method is that we take the first 35 bytes of every file and associate that with an extension, and possible containing parent directory (i.e. databases, world maps, zones, 3d models, etc).

The extensions produced are to an accuracy of 97%, but since the directories are not as straight-forward, they are only accurate upto the 80% mark.
