from ship_factory import ShipFactory
from transport_factory import TransportFactory
from truck_factory import TruckFactory

def main(transport_factory: TransportFactory):
    transport = transport_factory.create_transport()
    transport.deliver()

truck_factory = TruckFactory()
main(truck_factory)

ship_factory = ShipFactory()
main(ship_factory)

