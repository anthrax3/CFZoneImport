import urllib


class CrimeFlare:

    """Docstring for CrimeFlare. """

    def __init__(self):

        return True

    def process(self):
        self.download();

        return True

    def download(self):
        DLFile = urllib.URLopener()
        DLFile.retrieve(self.config.CrimeFlare.DownloadFile, self.config.General.TmpPath + "/crimeflare.zip")

        pass
