class View:

    def printDetalhe(self, **dados):
        string = ""
        for i in dados:
            string += i + "\n"

        print(string)
