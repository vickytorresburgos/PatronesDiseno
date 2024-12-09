from transport import Transport
from transport_factory import TransportFactory
from ship import Ship

class ShipFactory(TransportFactory):
    def create_transport(self)-> Transport :
        return Ship()