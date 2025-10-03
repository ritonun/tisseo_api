import requests

class TisseoAPI:
    def __init__(self, api_key: str):
        """
        Initialisation du client API
        :param api_key: Votre cle api Tisseo
        """
        self.api_key = api_key
        # https://api.tisseo.fr/v2/<nom du service>.<format>?<paramètres>&key=<votre_clé>
        self.base_url = "https://api.tisseo.fr/v2/"

    def _build_url(self, service: str, format: str = "json", parametres: dict = {}) -> str:
        """
        Construit l'url complet pour l'api
        :param service: Service Tisseo
        :param format: Format de la reponse ("json" ou "xml")
        :param parametre: Dict des parametres de la demande api
        :return: URL Complet
        """
        parametres["key"] = self.api_key

        query_url = ""
        for key, value in parametres.items():
            query_url += f"&{key}={value}"

        full_url = f"{self.base_url}{service}.{format}?{query_url[1:]}"
        return full_url

    def get_stops_schedule(self):
        """
        Faire une requete a l'api tisseo pour obtenir les prochains passages de cet arret
        cf. p26 api doc
        """

        parametres = {
            "number": 10,
            "displayRealTime": 1,

        }
