# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.30

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

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/leo/Desktop/gr-dsmr-rc

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/leo/Desktop/gr-dsmr-rc/build

# Utility rule file for dsmx_docstrings.

# Include any custom commands dependencies for this target.
include python/dsmx/bindings/CMakeFiles/dsmx_docstrings.dir/compiler_depend.make

# Include the progress variables for this target.
include python/dsmx/bindings/CMakeFiles/dsmx_docstrings.dir/progress.make

python/dsmx/bindings/CMakeFiles/dsmx_docstrings: python/dsmx/bindings/docstring_status

python/dsmx/bindings/docstring_status:
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --blue --bold --progress-dir=/home/leo/Desktop/gr-dsmr-rc/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Adding docstrings into dsmx pybind headers ..."
	cd /home/leo/Desktop/gr-dsmr-rc/build/python/dsmx/bindings && /usr/bin/python3 /home/leo/Desktop/gr-dsmr-rc/docs/doxygen/update_pydoc.py sub --json_path /home/leo/Desktop/gr-dsmr-rc/build/python/dsmx/bindings/extracted_docstrings.json --bindings_dir /home/leo/Desktop/gr-dsmr-rc/python/dsmx/bindings/docstrings --output_dir /home/leo/Desktop/gr-dsmr-rc/build/python/dsmx/bindings --filter gr::dsmx

dsmx_docstrings: python/dsmx/bindings/CMakeFiles/dsmx_docstrings
dsmx_docstrings: python/dsmx/bindings/docstring_status
dsmx_docstrings: python/dsmx/bindings/CMakeFiles/dsmx_docstrings.dir/build.make
.PHONY : dsmx_docstrings

# Rule to build all files generated by this target.
python/dsmx/bindings/CMakeFiles/dsmx_docstrings.dir/build: dsmx_docstrings
.PHONY : python/dsmx/bindings/CMakeFiles/dsmx_docstrings.dir/build

python/dsmx/bindings/CMakeFiles/dsmx_docstrings.dir/clean:
	cd /home/leo/Desktop/gr-dsmr-rc/build/python/dsmx/bindings && $(CMAKE_COMMAND) -P CMakeFiles/dsmx_docstrings.dir/cmake_clean.cmake
.PHONY : python/dsmx/bindings/CMakeFiles/dsmx_docstrings.dir/clean

python/dsmx/bindings/CMakeFiles/dsmx_docstrings.dir/depend:
	cd /home/leo/Desktop/gr-dsmr-rc/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/leo/Desktop/gr-dsmr-rc /home/leo/Desktop/gr-dsmr-rc/python/dsmx/bindings /home/leo/Desktop/gr-dsmr-rc/build /home/leo/Desktop/gr-dsmr-rc/build/python/dsmx/bindings /home/leo/Desktop/gr-dsmr-rc/build/python/dsmx/bindings/CMakeFiles/dsmx_docstrings.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : python/dsmx/bindings/CMakeFiles/dsmx_docstrings.dir/depend

