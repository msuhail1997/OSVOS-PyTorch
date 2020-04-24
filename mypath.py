from util.path_abstract import PathAbstract


class Path(PathAbstract):
    @staticmethod
    def db_root_dir():
        return '/content/drive/My Drive/DAVIS 2016/DAVIS/'

    @staticmethod
    def save_root_dir():
        return '/content/drive/Shared drives/CIS 599 Independent Study/OSVOS-DAVIS/models'

    @staticmethod
    def models_dir():
        return "/content/drive/Shared drives/CIS 599 Independent Study/OSVOS-DAVIS/models"

