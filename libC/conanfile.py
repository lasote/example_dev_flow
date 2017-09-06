from conans import ConanFile, CMake, tools
import os


class LibcConan(ConanFile):
    name = "libC"
    version = "1.0"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Libc here>"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*", "!build/*"

    def build(self):
        os.mkdir("build")
        with tools.chdir("build"):
            if self.settings.os == "Windows":
                cmake = CMake(self)
                self.run('cmake hello %s' % cmake.command_line)
                self.run("cmake --build . %s" % cmake.build_config)
            else:
                self.run("autoreconf -vfi ..")
                self.run("../configure")
                self.run("make")

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["c"]
