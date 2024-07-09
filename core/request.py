import httpx
from core.format import Format

class Request:

    @staticmethod
    def _get_title(html: str) -> str:
        if html:
            title = Format.clear_value(Format.regex(html, r'<title[^>]*>([^<]+)</title>')[0])
            title = title.replace("'", "")
            if title:
                return title
        return str()
        

    def get(self, url: str) -> str:
        if url.startswith('http'):
            try:
                rest = httpx.get(url=url, verify=False, timeout=3)
                if rest.is_success or rest.is_error or rest.is_redirect:
                    return f"{rest.status_code}; {self._get_title(rest.text)}"
            except Exception:
                pass
        return str() 