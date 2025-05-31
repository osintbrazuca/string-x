from core.basemodule import BaseModule
import socket
import subprocess

class DnsInfo(BaseModule):
    """
    Coleta informações DNS de hosts.
    """
    
    def __init__(self):
        super().__init__()
        
        self.meta = {
            'name': 'DNS Information Collector',
            "author": "MrCl0wn",
            'version': '1.0',
            'description': 'Coleta registros DNS de hosts',
            'type': 'collector'
        }
        
        self.options = {
            'data': str(),  # Nome do host a ser pesquisado
            'records': ['A', 'MX', 'TXT', 'NS'],
            'timeout': 5,
            'resolver': '8.8.8.8'
        }
    
    def _get_dns_record(self, host: str, record_type: str) -> list:
        """Obtém registro DNS específico."""
        try:
            cmd = ['dig', f'@{self.options["resolver"]}', 
                   '+short', host, record_type]
            result = subprocess.run(cmd, capture_output=True, 
                                  text=True, timeout=self.options['timeout'])
            if result.stdout:
                return result.stdout.strip().split('\n')
        except Exception:
            pass
        return []
    
    def run(self):
        """
        Coleta informações DNS.
        
        Args:
            data (str): Nome do host
        """
        host = self.options.get("data", "").strip()
        
        if not host:
            return None
        
        dns_info = {
            'host': host,
            'records': {}
        }
        
        # Coletar cada tipo de registro
        for record_type in self.options['records']:
            records = self._get_dns_record(host, record_type)
            if records:
                dns_info['records'][record_type] = records
        
        # Formatar resultado
        if dns_info['records']:
            result = f"Host: {host}\n"
            for rtype, values in dns_info['records'].items():
                result += f"  {rtype}: {', '.join(values)}\n"
            
            self.set_result(result)
        