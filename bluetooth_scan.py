import asyncio
import sys
from bleak import BleakScanner
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich import box
from rich.panel import Panel
from rich.align import Align

console = Console()

async def scan_devices():
    scan_duration = 5.0

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:
        
        scan_task_id = progress.add_task("[cyan]Scanning for devices...", total=100)
        
        try:
            scanner_future = asyncio.create_task(BleakScanner.discover(timeout=scan_duration, return_adv=True))

            for _ in range(100):
                await asyncio.sleep(scan_duration / 100)
                progress.update(scan_task_id, advance=1)

            devices_dict = await scanner_future
            
        except Exception as e:
            console.print(f"\n[bold red]CRITICAL ERROR during scan:[/bold red] {e}")
            return

    try:
        if not devices_dict:
            console.print("[bold red]No devices found.[/bold red]")
        else:
            scanned_devices = list(devices_dict.values())
            scanned_devices.sort(key=lambda x: x[1].rssi if x[1].rssi is not None else -100, reverse=True)

            console.print(f"[green]Scan Complete! Found {len(scanned_devices)} devices.[/green]\n")

            table = Table(title="Bluetooth LE Scanner Results", box=box.ROUNDED)
            table.add_column("Signal", justify="center", style="cyan", no_wrap=True)
            table.add_column("Device Name", style="bold white")
            table.add_column("MAC Address", style="magenta")
            table.add_column("Manufacturer ID", style="dim")

            for device, adv_data in scanned_devices:
                name = device.name or "[italic dim]Unknown[/italic dim]"
                
                rssi = adv_data.rssi if adv_data.rssi is not None else -100
                
                if rssi > -60:
                    rssi_color = "green"
                elif rssi > -80:
                    rssi_color = "yellow"
                else:
                    rssi_color = "red"
                
                rssi_str = f"[{rssi_color}]{rssi} dBm[/{rssi_color}]"

                mf_data = list(adv_data.manufacturer_data.keys()) if adv_data.manufacturer_data else []
                mf_str = str(mf_data[0]) if mf_data else "-"

                table.add_row(rssi_str, name, device.address, mf_str)

            console.print(table)
            console.print("\n[dim]Tip: Closer to 0 dBm = Stronger Signal[/dim]\n")
        
    except Exception as e:
        console.print(f"\n[bold red]Error displaying results:[/bold red] {e}")

    # Credits Section - Always displays at the end
    github_url = "https://github.com/Nawafalzanbaqi"
    credit_text = f"[bold white]Developed by: Nawaf Alzanbaqi[/bold white]\n[link={github_url}][bold cyan]{github_url}[/bold cyan][/link]"
    console.print(Align.center(Panel(credit_text, title="Credits", border_style="cyan", padding=(1, 2))))

if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    try:
        asyncio.run(scan_devices())
    except KeyboardInterrupt:
        print("Scan stopped by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    input("\nPress Enter to exit...")