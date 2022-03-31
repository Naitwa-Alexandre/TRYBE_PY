from manipulador_de_log import ManipuladorDeLog

class LogEmArquivo(ManipuladorDeLog):
    @classmethod
    def log(cls, msg):
        with open("log.txt", "a") as file:
            print(msg, file=file)