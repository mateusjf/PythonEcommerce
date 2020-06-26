class Command:

    @abstractmethod
    def execute(self):
        raise NotImplementedError()