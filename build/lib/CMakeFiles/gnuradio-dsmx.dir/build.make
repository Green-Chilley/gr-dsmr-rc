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

# Include any dependencies generated for this target.
include lib/CMakeFiles/gnuradio-dsmx.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include lib/CMakeFiles/gnuradio-dsmx.dir/compiler_depend.make

# Include the progress variables for this target.
include lib/CMakeFiles/gnuradio-dsmx.dir/progress.make

# Include the compile flags for this target's objects.
include lib/CMakeFiles/gnuradio-dsmx.dir/flags.make

lib/CMakeFiles/gnuradio-dsmx.dir/preambleDetection_impl.cc.o: lib/CMakeFiles/gnuradio-dsmx.dir/flags.make
lib/CMakeFiles/gnuradio-dsmx.dir/preambleDetection_impl.cc.o: /home/leo/Desktop/gr-dsmr-rc/lib/preambleDetection_impl.cc
lib/CMakeFiles/gnuradio-dsmx.dir/preambleDetection_impl.cc.o: lib/CMakeFiles/gnuradio-dsmx.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/leo/Desktop/gr-dsmr-rc/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object lib/CMakeFiles/gnuradio-dsmx.dir/preambleDetection_impl.cc.o"
	cd /home/leo/Desktop/gr-dsmr-rc/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT lib/CMakeFiles/gnuradio-dsmx.dir/preambleDetection_impl.cc.o -MF CMakeFiles/gnuradio-dsmx.dir/preambleDetection_impl.cc.o.d -o CMakeFiles/gnuradio-dsmx.dir/preambleDetection_impl.cc.o -c /home/leo/Desktop/gr-dsmr-rc/lib/preambleDetection_impl.cc

lib/CMakeFiles/gnuradio-dsmx.dir/preambleDetection_impl.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/gnuradio-dsmx.dir/preambleDetection_impl.cc.i"
	cd /home/leo/Desktop/gr-dsmr-rc/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/leo/Desktop/gr-dsmr-rc/lib/preambleDetection_impl.cc > CMakeFiles/gnuradio-dsmx.dir/preambleDetection_impl.cc.i

lib/CMakeFiles/gnuradio-dsmx.dir/preambleDetection_impl.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/gnuradio-dsmx.dir/preambleDetection_impl.cc.s"
	cd /home/leo/Desktop/gr-dsmr-rc/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/leo/Desktop/gr-dsmr-rc/lib/preambleDetection_impl.cc -o CMakeFiles/gnuradio-dsmx.dir/preambleDetection_impl.cc.s

lib/CMakeFiles/gnuradio-dsmx.dir/Despreader_impl.cc.o: lib/CMakeFiles/gnuradio-dsmx.dir/flags.make
lib/CMakeFiles/gnuradio-dsmx.dir/Despreader_impl.cc.o: /home/leo/Desktop/gr-dsmr-rc/lib/Despreader_impl.cc
lib/CMakeFiles/gnuradio-dsmx.dir/Despreader_impl.cc.o: lib/CMakeFiles/gnuradio-dsmx.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/leo/Desktop/gr-dsmr-rc/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object lib/CMakeFiles/gnuradio-dsmx.dir/Despreader_impl.cc.o"
	cd /home/leo/Desktop/gr-dsmr-rc/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT lib/CMakeFiles/gnuradio-dsmx.dir/Despreader_impl.cc.o -MF CMakeFiles/gnuradio-dsmx.dir/Despreader_impl.cc.o.d -o CMakeFiles/gnuradio-dsmx.dir/Despreader_impl.cc.o -c /home/leo/Desktop/gr-dsmr-rc/lib/Despreader_impl.cc

lib/CMakeFiles/gnuradio-dsmx.dir/Despreader_impl.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/gnuradio-dsmx.dir/Despreader_impl.cc.i"
	cd /home/leo/Desktop/gr-dsmr-rc/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/leo/Desktop/gr-dsmr-rc/lib/Despreader_impl.cc > CMakeFiles/gnuradio-dsmx.dir/Despreader_impl.cc.i

lib/CMakeFiles/gnuradio-dsmx.dir/Despreader_impl.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/gnuradio-dsmx.dir/Despreader_impl.cc.s"
	cd /home/leo/Desktop/gr-dsmr-rc/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/leo/Desktop/gr-dsmr-rc/lib/Despreader_impl.cc -o CMakeFiles/gnuradio-dsmx.dir/Despreader_impl.cc.s

lib/CMakeFiles/gnuradio-dsmx.dir/bindListener_impl.cc.o: lib/CMakeFiles/gnuradio-dsmx.dir/flags.make
lib/CMakeFiles/gnuradio-dsmx.dir/bindListener_impl.cc.o: /home/leo/Desktop/gr-dsmr-rc/lib/bindListener_impl.cc
lib/CMakeFiles/gnuradio-dsmx.dir/bindListener_impl.cc.o: lib/CMakeFiles/gnuradio-dsmx.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/leo/Desktop/gr-dsmr-rc/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object lib/CMakeFiles/gnuradio-dsmx.dir/bindListener_impl.cc.o"
	cd /home/leo/Desktop/gr-dsmr-rc/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT lib/CMakeFiles/gnuradio-dsmx.dir/bindListener_impl.cc.o -MF CMakeFiles/gnuradio-dsmx.dir/bindListener_impl.cc.o.d -o CMakeFiles/gnuradio-dsmx.dir/bindListener_impl.cc.o -c /home/leo/Desktop/gr-dsmr-rc/lib/bindListener_impl.cc

lib/CMakeFiles/gnuradio-dsmx.dir/bindListener_impl.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/gnuradio-dsmx.dir/bindListener_impl.cc.i"
	cd /home/leo/Desktop/gr-dsmr-rc/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/leo/Desktop/gr-dsmr-rc/lib/bindListener_impl.cc > CMakeFiles/gnuradio-dsmx.dir/bindListener_impl.cc.i

lib/CMakeFiles/gnuradio-dsmx.dir/bindListener_impl.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/gnuradio-dsmx.dir/bindListener_impl.cc.s"
	cd /home/leo/Desktop/gr-dsmr-rc/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/leo/Desktop/gr-dsmr-rc/lib/bindListener_impl.cc -o CMakeFiles/gnuradio-dsmx.dir/bindListener_impl.cc.s

# Object files for target gnuradio-dsmx
gnuradio__dsmx_OBJECTS = \
"CMakeFiles/gnuradio-dsmx.dir/preambleDetection_impl.cc.o" \
"CMakeFiles/gnuradio-dsmx.dir/Despreader_impl.cc.o" \
"CMakeFiles/gnuradio-dsmx.dir/bindListener_impl.cc.o"

# External object files for target gnuradio-dsmx
gnuradio__dsmx_EXTERNAL_OBJECTS =

lib/libgnuradio-dsmx.so.1.0.0.0: lib/CMakeFiles/gnuradio-dsmx.dir/preambleDetection_impl.cc.o
lib/libgnuradio-dsmx.so.1.0.0.0: lib/CMakeFiles/gnuradio-dsmx.dir/Despreader_impl.cc.o
lib/libgnuradio-dsmx.so.1.0.0.0: lib/CMakeFiles/gnuradio-dsmx.dir/bindListener_impl.cc.o
lib/libgnuradio-dsmx.so.1.0.0.0: lib/CMakeFiles/gnuradio-dsmx.dir/build.make
lib/libgnuradio-dsmx.so.1.0.0.0: /usr/lib/x86_64-linux-gnu/libgnuradio-runtime.so.3.10.11.0
lib/libgnuradio-dsmx.so.1.0.0.0: /usr/lib/x86_64-linux-gnu/libgnuradio-pmt.so.3.10.11.0
lib/libgnuradio-dsmx.so.1.0.0.0: /usr/lib/x86_64-linux-gnu/libvolk.so.3.1.2
lib/libgnuradio-dsmx.so.1.0.0.0: /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.83.0
lib/libgnuradio-dsmx.so.1.0.0.0: /usr/lib/x86_64-linux-gnu/libboost_atomic.so.1.83.0
lib/libgnuradio-dsmx.so.1.0.0.0: /usr/lib/x86_64-linux-gnu/libspdlog.so.1.12.0
lib/libgnuradio-dsmx.so.1.0.0.0: /usr/lib/x86_64-linux-gnu/libfmt.so.9.1.0
lib/libgnuradio-dsmx.so.1.0.0.0: /usr/lib/x86_64-linux-gnu/libgmpxx.so
lib/libgnuradio-dsmx.so.1.0.0.0: /usr/lib/x86_64-linux-gnu/libgmp.so
lib/libgnuradio-dsmx.so.1.0.0.0: lib/CMakeFiles/gnuradio-dsmx.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/home/leo/Desktop/gr-dsmr-rc/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX shared library libgnuradio-dsmx.so"
	cd /home/leo/Desktop/gr-dsmr-rc/build/lib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/gnuradio-dsmx.dir/link.txt --verbose=$(VERBOSE)
	cd /home/leo/Desktop/gr-dsmr-rc/build/lib && $(CMAKE_COMMAND) -E cmake_symlink_library libgnuradio-dsmx.so.1.0.0.0 libgnuradio-dsmx.so.1.0.0 libgnuradio-dsmx.so

lib/libgnuradio-dsmx.so.1.0.0: lib/libgnuradio-dsmx.so.1.0.0.0
	@$(CMAKE_COMMAND) -E touch_nocreate lib/libgnuradio-dsmx.so.1.0.0

lib/libgnuradio-dsmx.so: lib/libgnuradio-dsmx.so.1.0.0.0
	@$(CMAKE_COMMAND) -E touch_nocreate lib/libgnuradio-dsmx.so

# Rule to build all files generated by this target.
lib/CMakeFiles/gnuradio-dsmx.dir/build: lib/libgnuradio-dsmx.so
.PHONY : lib/CMakeFiles/gnuradio-dsmx.dir/build

lib/CMakeFiles/gnuradio-dsmx.dir/clean:
	cd /home/leo/Desktop/gr-dsmr-rc/build/lib && $(CMAKE_COMMAND) -P CMakeFiles/gnuradio-dsmx.dir/cmake_clean.cmake
.PHONY : lib/CMakeFiles/gnuradio-dsmx.dir/clean

lib/CMakeFiles/gnuradio-dsmx.dir/depend:
	cd /home/leo/Desktop/gr-dsmr-rc/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/leo/Desktop/gr-dsmr-rc /home/leo/Desktop/gr-dsmr-rc/lib /home/leo/Desktop/gr-dsmr-rc/build /home/leo/Desktop/gr-dsmr-rc/build/lib /home/leo/Desktop/gr-dsmr-rc/build/lib/CMakeFiles/gnuradio-dsmx.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : lib/CMakeFiles/gnuradio-dsmx.dir/depend

