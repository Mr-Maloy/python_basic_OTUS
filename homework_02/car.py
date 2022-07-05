from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):

    engine = None

    def set_engine(self, client: Engine):
        if not isinstance(client, Engine):
            raise TypeError("Not an 'Engine' object!")
        self.engine = client

# Комментарий для Pull Request