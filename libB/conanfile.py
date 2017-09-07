from conans import ConanFile, CMake, tools, AutoToolsBuildEnvironment
import os


class LibBConan(ConanFile):
    name = "libB"
    version = "1.0"
    license = "MIT"
    url = "https://github.com/lasote/example_dev_flow"
    description = "Example of dev flow with CMake"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*", "!build/*"
    requires = "libC/1.0@myuser/channel"

    def build(self):
        os.mkdir("build")
        with tools.chdir("build"):
            cmake = CMake(self)
            cmake.configure()
            cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["b"]
