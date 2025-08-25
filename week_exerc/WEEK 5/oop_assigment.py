# Classe base
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"Dispositivo: {self.brand} {self.model}"


# Classe derivada (herança)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Chama o construtor da classe base
        super().__init__(brand, model)
        self.storage = storage
        self.battery = battery
        self.is_on = False

    # Método para ligar o smartphone
    def power_on(self):
        if not self.is_on:
            self.is_on = True
            return f"{self.brand} {self.model} está agora LIGADO."
        return f"{self.brand} {self.model} já estava ligado."

    # Método para desligar
    def power_off(self):
        if self.is_on:
            self.is_on = False
            return f"{self.brand} {self.model} está agora DESLIGADO."
        return f"{self.brand} {self.model} já estava desligado."

    # Método para instalar uma app
    def install_app(self, app_name):
        return f"App '{app_name}' instalada com sucesso em {self.brand} {self.model}."

    # Método polimórfico (sobrescreve da classe base)
    def device_info(self):
        return f"{self.brand} {self.model} | {self.storage}GB | Bateria: {self.battery}mAh"


# Exemplo de uso
phone1 = Smartphone("Apple", "iPhone 15", 256, 4000)
phone2 = Smartphone("Samsung", "Galaxy S23", 512, 5000)

print(phone1.device_info())
print(phone1.power_on())
print(phone1.install_app("WhatsApp"))
print(phone1.power_off())

print("\n--- Outro smartphone ---")
print(phone2.device_info())
print(phone2.power_on())
