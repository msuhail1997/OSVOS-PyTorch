from util.path_abstract import PathAbstract


class Path(PathAbstract):
    @staticmethod
    def db_root_dir():
        return '/path/to/DAVIS-2016'

    @staticmethod
    def save_root_dir():
        return '/content/OSVOS-PyTorch/models'

    @staticmethod
    def models_dir():
        return "/content/OSVOS-PyTorch/models"

