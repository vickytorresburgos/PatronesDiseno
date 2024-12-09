from transport import Transport
from transport_factory import TransportFactory
from truck import Truck

class TruckFactory(TransportFactory):
    def create_transport(self) -> Transport:
        return Truck()
    