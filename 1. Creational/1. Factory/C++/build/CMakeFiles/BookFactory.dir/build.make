# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.20

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\CMake\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\CMake\bin\cmake.exe" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "D:\Programming\Design Patterns\1. Creational\1. Factory\C++"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "D:\Programming\Design Patterns\1. Creational\1. Factory\C++\build"

# Include any dependencies generated for this target.
include CMakeFiles/BookFactory.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/BookFactory.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/BookFactory.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/BookFactory.dir/flags.make

CMakeFiles/BookFactory.dir/main.cpp.obj: CMakeFiles/BookFactory.dir/flags.make
CMakeFiles/BookFactory.dir/main.cpp.obj: ../main.cpp
CMakeFiles/BookFactory.dir/main.cpp.obj: CMakeFiles/BookFactory.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="D:\Programming\Design Patterns\1. Creational\1. Factory\C++\build\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/BookFactory.dir/main.cpp.obj"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/BookFactory.dir/main.cpp.obj -MF CMakeFiles\BookFactory.dir\main.cpp.obj.d -o CMakeFiles\BookFactory.dir\main.cpp.obj -c "D:\Programming\Design Patterns\1. Creational\1. Factory\C++\main.cpp"

CMakeFiles/BookFactory.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/BookFactory.dir/main.cpp.i"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "D:\Programming\Design Patterns\1. Creational\1. Factory\C++\main.cpp" > CMakeFiles\BookFactory.dir\main.cpp.i

CMakeFiles/BookFactory.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/BookFactory.dir/main.cpp.s"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "D:\Programming\Design Patterns\1. Creational\1. Factory\C++\main.cpp" -o CMakeFiles\BookFactory.dir\main.cpp.s

# Object files for target BookFactory
BookFactory_OBJECTS = \
"CMakeFiles/BookFactory.dir/main.cpp.obj"

# External object files for target BookFactory
BookFactory_EXTERNAL_OBJECTS =

BookFactory.exe: CMakeFiles/BookFactory.dir/main.cpp.obj
BookFactory.exe: CMakeFiles/BookFactory.dir/build.make
BookFactory.exe: CMakeFiles/BookFactory.dir/linklibs.rsp
BookFactory.exe: CMakeFiles/BookFactory.dir/objects1.rsp
BookFactory.exe: CMakeFiles/BookFactory.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="D:\Programming\Design Patterns\1. Creational\1. Factory\C++\build\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable BookFactory.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\BookFactory.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/BookFactory.dir/build: BookFactory.exe
.PHONY : CMakeFiles/BookFactory.dir/build

CMakeFiles/BookFactory.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\BookFactory.dir\cmake_clean.cmake
.PHONY : CMakeFiles/BookFactory.dir/clean

CMakeFiles/BookFactory.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" "D:\Programming\Design Patterns\1. Creational\1. Factory\C++" "D:\Programming\Design Patterns\1. Creational\1. Factory\C++" "D:\Programming\Design Patterns\1. Creational\1. Factory\C++\build" "D:\Programming\Design Patterns\1. Creational\1. Factory\C++\build" "D:\Programming\Design Patterns\1. Creational\1. Factory\C++\build\CMakeFiles\BookFactory.dir\DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/BookFactory.dir/depend

