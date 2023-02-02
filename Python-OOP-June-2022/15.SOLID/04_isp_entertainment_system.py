class HdmiConnectable:
    def connect_via_hdmi(self, device):
        return f'Connected via HDMI to {device}'


class EthernetConnectable:
    def connect_via_ethernet(self, device):
        return f'Connected via ETHERNET to {device}'


class PowerOutletConnectable:
    def connect_to_power_outlet(self, device):
        return f'Connected via power cable to {device}'



class Television(HdmiConnectable, PowerOutletConnectable, EthernetConnectable):
    def connect_to_game_console(self, game_console):
        return self.connect_via_hdmi(game_console)

    def plug_in_power(self):
        return self.connect_to_power_outlet(self)

    def connect_to_router(self, router):
        return self.connect_via_ethernet(router)


class GameConsole(HdmiConnectable, EthernetConnectable, PowerOutletConnectable):
    def connect_to_tv(self, television):
        return self.connect_via_hdmi(television)

    def connect_to_router(self, router):
        return self.connect_via_ethernet(router)

    def plug_in_power(self):
        return self.connect_to_power_outlet(self)


class Router(EthernetConnectable, PowerOutletConnectable):
    def connect_to_tv(self, television):
        return self.connect_via_ethernet(television)

    def connect_to_game_console(self, game_console):
        return self.connect_via_ethernet(game_console)

    def plug_in_power(self):
        return self.connect_to_power_outlet(self)

tv = Television()
print(tv.connect_to_game_console("game_console"))