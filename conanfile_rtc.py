from conans import ConanFile


class YamlCppConan(ConanFile):
    name = "yaml-cpp"
    version = "0.6.2"
    url = "https://github.com/Esri/yaml-cpp/tree/runtimecore"
    license = "https://github.com/Esri/yaml-cpp/blob/runtimecore/LICENSE"
    description = "A YAML parser and emitter in C++."

    # RTC specific triple
    settings = "platform_architecture_target"

    def package(self):
        base = self.source_folder + "/"
        relative = "3rdparty/yaml-cpp/"

        # headers
        self.copy("*.h", src=base + "include", dst=relative + "include")

        # libraries
        output = "output/" + str(self.settings.platform_architecture_target) + "/staticlib"
        self.copy("*" + self.name + "*", src=base + "../../" + output, dst=output)
