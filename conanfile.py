from conans import ConanFile, CMake, tools, AutoToolsBuildEnvironment
import os


class ReusepcConan(ConanFile):
    license = "MIT"
    url = "https://github.com/lasote/conan_reuse_pc"
    settings = "os", "compiler", "build_type", "arch"
    requires = "zlib/1.2.11@lasote/stable", "libpng/1.6.23@lasote/stable"

    def build(self):
        import_pcs_and_patch(self, ["zlib", "libpng"])
        build_env = AutoToolsBuildEnvironment(self)
        env_vars = {"PKG_CONFIG_PATH": os.getcwd()}
        env_vars.update(build_env.vars)
        with tools.environment_append(env_vars):
            with tools.chdir(self.conanfile_directory):
                self.run('autoreconf --install')

                self.output.info('Configuring')
                self.run("./configure")

                self.output.info('Compiling')
                self.run('make -j%s' % tools.cpu_count())

                self.output.info('Running tests')
                self.run("src/main_c")


def import_pcs_and_patch(conanfile, libs, dest_dir="."):
    from conans.client.file_copier import FileCopier
    for lib in libs:
        file_copier = FileCopier(conanfile.deps_cpp_info[lib].rootpath, dest_dir)
        pcs = file_copier("*.pc")
        for pcfile in pcs:
            replace_preffix_in_pc(pcfile, conanfile.deps_cpp_info[lib].rootpath)


def replace_preffix_in_pc(pc_file, new_preffix):
    content = tools.load(pc_file)
    lines = []
    for line in content.splitlines():
        if line.startswith("prefix="):
            lines.append("prefix=%s" % new_preffix)
        else:
            lines.append(line)
    tools.save(pc_file, "\n".join(lines))