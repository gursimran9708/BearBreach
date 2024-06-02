from intro import display_my_info
from rich import print
from vt_domain_api import vt_domain_api
from vt_hash_api import vt_api_files
from vt_ip_api import vt_ip_api
from vt_url_api import vt_url_api
from criminalIP_ip_api import criminalIP_ip_api
from threatfox_domain_api import threatfox_domain_api
from threatfox_ip_api import threatfox_ip_api
from threatfox_url_api import threatfox_url_api
from otx_domain_api import otx_domain_api
from otx_ip_api import otx_ip_api
from opswat_domain_api import opswat_domain_api
from opswat_hash_api import opswatmetadefender_api_files
from opswat_url_api import opswatmetadefender_url_api
from polyswarm_hash_api import polyswarm_api_files
from polyswarm_url_api import polyswarm_url_api
from urlhaus_url_api import urlhaus_url_api
from urlscan_domain_api import urlscan_domain_api
from greynoise_ip_api import greynoise_ip_api
from AbuseIPdb_ip_api import abuseipdb_ip_api
from malshare_hash_api import malshare_api_files
from malwarebazaar_hash_api import malwarebazaar_api_files
from falconsandbox_hash_api import falcon_api_files


from rich import print
from rich.console import Console
from intro import display_my_info

console = Console()
display_my_info()
def main():
    while True:
        
        try:
            console.print(
                """[bold cyan]Choose an IOC type [1-4]:[/bold cyan]
[green]1.[/green] [bold]IP Address[/bold]
[green]2.[/green] [bold]File Hash[/bold]
[green]3.[/green] [bold]Domain[/bold]
[green]4.[/green] [bold]URL[/bold]
                """, highlight=False
            )

            ioc_type = int(input("Enter your choice: "))

            if ioc_type == 1:
                ioc_value = console.input("[bold cyan]Input IOC Value: [/bold cyan]")
                console.print(
                    """[bold cyan]Choose a Threat Intelligence Platform [1-6]:[/bold cyan]
                [yellow]---------------------[/yellow]
                |[green]1.[/green] [bold]Virustotal[/bold]       |
                |[green]2.[/green] [bold]Criminal IP[/bold]      |    
                |[green]3.[/green] [bold]AbuseIPdb[/bold]        |
                |[green]4.[/green] [bold]Greynoise[/bold]        |
                |[green]5.[/green] [bold]Alienvault OTX[/bold]   |
                |[green]6.[/green] [bold]Threatfox[/bold]        |
                [yellow]---------------------[/yellow]
                """, highlight=False
                )
                intel_platform = int(input("Enter your choice: "))
                if intel_platform == 1:
                    vt_ip_api(ioc_value)
                elif intel_platform == 2:
                    criminalIP_ip_api(ioc_value)
                elif intel_platform == 3:
                    abuseipdb_ip_api(ioc_value)
                elif intel_platform == 4:
                    greynoise_ip_api(ioc_value)
                elif intel_platform == 5:
                    otx_ip_api(ioc_value)
                elif intel_platform == 6:
                    threatfox_ip_api(ioc_value)

            elif ioc_type == 2:
                ioc_value = console.input("[bold cyan]Input IOC Value: [/bold cyan]")
                console.print(
                    """[bold cyan]Choose a Threat Intelligence Platform [1-6]:[/bold cyan]
                [yellow]-----------------------------[/yellow]
                |[green]1.[/green] [bold]Virustotal[/bold]              |
                |[green]2.[/green] [bold]Malshare[/bold]                |    
                |[green]3.[/green] [bold]Falcon Sandbox[/bold]          |
                |[green]4.[/green] [bold]Malware Bazaar[/bold]          |
                |[green]5.[/green] [bold]OPSWAT Metadefender[/bold]     |
                |[green]6.[/green] [bold]Polyswarm[/bold]               |
                [yellow]-----------------------------[/yellow]
                """, highlight=False
                )
                intel_platform = int(input("Enter your choice: "))
                if intel_platform == 1:
                    vt_api_files(ioc_value)
                elif intel_platform == 2:
                    malshare_api_files(ioc_value)
                elif intel_platform == 3:
                    falcon_api_files(ioc_value)
                elif intel_platform == 4:
                    malwarebazaar_api_files(ioc_value)
                elif intel_platform == 5:
                    opswatmetadefender_api_files(ioc_value)
                elif intel_platform == 6:
                    polyswarm_api_files(ioc_value)

            elif ioc_type == 3:
                ioc_value = console.input("[bold cyan]Input IOC Value: [/bold cyan]")
                console.print(
                    """[bold cyan]Choose a Threat Intelligence Platform [1-6]:[/bold cyan]
                [yellow]-----------------------------[/yellow]
                |[green]1.[/green] [bold]Virustotal[/bold]              |   
                |[green]2.[/green] [bold]Threatfox[/bold]               |      
                |[green]3.[/green] [bold]Urlscan[/bold]                 |
                |[green]4.[/green] [bold]OPSWAT Metadefender[/bold]     |        
                |[green]5.[/green] [bold]Alienvault OTX[/bold]          |
                [yellow]-----------------------------[/yellow]    
                """, highlight=False
                )
                intel_platform = int(input("Enter your choice: "))
                if intel_platform == 1:
                    vt_domain_api(ioc_value)
                elif intel_platform == 2:
                    threatfox_domain_api(ioc_value)
                elif intel_platform == 3:
                    urlscan_domain_api(ioc_value)
                elif intel_platform == 4:
                    opswat_domain_api(ioc_value)
                elif intel_platform == 5:
                    otx_domain_api(ioc_value)

            
            elif ioc_type == 4:
                ioc_value = console.input("[bold cyan]Input IOC Value: [/bold cyan]")
                console.print(
                    """[bold cyan]Choose a Threat Intelligence Platform [1-6]:[/bold cyan]
                [yellow]-----------------------------[/yellow]
                |[green]1.[/green] [bold]Virustotal[/bold]              |
                |[green]2.[/green] [bold]Polyswarm[/bold]               |    
                |[green]3.[/green] [bold]Urlhaus[/bold]                 |
                |[green]4.[/green] [bold]OPSWAT Metadefender[/bold]     |
                |[green]5.[/green] [bold]Threatfox[/bold]               |
                [yellow]-----------------------------[/yellow]
                """, highlight=False
                )
                intel_platform = int(input("Enter your choice: "))
                if intel_platform == 1:
                    vt_url_api(ioc_value)
                elif intel_platform == 2:
                    polyswarm_url_api(ioc_value)
                elif intel_platform == 3:
                    urlhaus_url_api(ioc_value)
                elif intel_platform == 4:
                    opswatmetadefender_url_api(ioc_value)
                elif intel_platform == 5:
                    threatfox_url_api(ioc_value)
                    
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
    
