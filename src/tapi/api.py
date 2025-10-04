import requests


class TisseoAPI:
    def __init__(self, api_key: str, timeout_request=10):
        """
        Initialisation du client API
        :param api_key: Votre cle api Tisseo
        """
        self.api_key = api_key
        self.timeout_request = timeout_request
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

    def _request(self, service: str, format: str = "json", parametres: dict = {}):
        url = self._build_url(service, format=format, parametres=parametres)

        debug_msg = f"service: {service}, format: {format}, parametres: {parametres}, url: {url}"

        try:
            response = requests.get(url, timeout=self.timeout_request)
            response.raise_for_status()
            if format.lower() == "json":
                return response.json()
            else:
                return response.text
        except requests.exceptions.Timeout:
            raise RuntimeError(f"Tisséo API request a dépassé le timeout {self.timeout_request}; {debug_msg}")
        except requests.exceptions.HTTPError as e:
            raise RuntimeError(f"HTTP Error en reponse de la requete Tisseo API {debug_msg}: {e}")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Fail de l'appel Tisseo API {debug_msg}: {e}")
        except ValueError:
            raise RuntimeError(f"Erreur lors du parsing du json en reponse de l'api {debug_msg}")

    def get_stops_schedules(self, parametres: dict = {}):
        """
        Faire une requete a l'api tisseo pour obtenir les prochains passages de cet arret
        cf. p26 api doc
        """

        parametres_api_default = {
            "displayRealTime": 1,
            "maxDays": 1
        }

        if not parametres:
            parametres = parametres_api_default

        return self._request("stops_schedules", format="json", parametres=parametres)
