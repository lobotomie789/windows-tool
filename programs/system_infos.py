import os, psutil, platform, colorama, msvcrt, socket, requests, time
from colorama import Fore

colorama.init(autoreset=True)
cyan = Fore.LIGHTCYAN_EX
red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX
green = Fore.LIGHTGREEN_EX
end = Fore.WHITE

def clear_buffer():
    while msvcrt.kbhit():
        msvcrt.getch()

def values():
    global current_freq,max_freq,min_freq,time_user,time_system,time_idle,time_interrupt,time_dpc,usage_total,usage_free
    global read_bytes,write_bytes,read_time,write_time,ram_total,ram_used,ram_available,ram_percent,memory_available,memory_percent
    global days,hours,minutes,seconds,usage_used,usage_percent,read_count,write_count,memory_total,memory_used,public_ip,local_ip
    freq = psutil.cpu_freq(True)[-1]
    current_freq = freq.current
    max_freq = freq.max
    min_freq = freq.min
    
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    public_ip = requests.get('https://api.ipify.org').text
    boot_time = psutil.boot_time()
    uptime_seconds = int(time.time() - boot_time)
    days = uptime_seconds // (24 * 3600)
    hours = (uptime_seconds % (24 * 3600)) // 3600
    minutes = (uptime_seconds % 3600) // 60
    seconds = uptime_seconds % 60

    cpu_time = psutil.cpu_times()
    time_user = cpu_time.user / 60
    time_system = cpu_time.system / 60
    time_idle = cpu_time.idle / 60
    time_interrupt = cpu_time.interrupt / 60
    time_dpc = cpu_time.dpc / 60

    disk_usage = psutil.disk_usage('C:')
    usage_total = disk_usage.total / 1024**3
    usage_used = disk_usage.used / 1024**3
    usage_free = disk_usage.free / 1024**3
    usage_percent = disk_usage.percent

    disk_io = psutil.disk_io_counters()
    read_count = disk_io.read_count
    write_count = disk_io.write_count
    read_bytes = disk_io.read_bytes / 1024**3
    write_bytes = disk_io.write_bytes / 1024**3
    read_time = disk_io.read_time / 1000
    write_time = disk_io.write_time / 1000

    ram = psutil.virtual_memory()
    ram_total = ram.total / 1024**3
    ram_used = ram.used / 1024**3
    ram_available = ram.available / 1024**3
    ram_percent = ram.percent

    virtual_memory = psutil.swap_memory()
    memory_total = virtual_memory.total / 1024**3
    memory_used = virtual_memory.used / 1024**3
    memory_available = virtual_memory.free / 1024**3
    memory_percent = virtual_memory.percent

def get_env_var(var):
    env_var = os.environ.get(var)
    return env_var

def get_all_infos():
    values()
    print(f'{cyan}═════════ : OS INFOS : ═════════')
    print('OS:', f'{yellow}{get_env_var('OS')}{end}')
    print('System:', f'{yellow}{platform.system()} {platform.release()}{end}')
    print('Machine:', f'{yellow}{platform.machine()}{end}')
    print('Processor:', f'{yellow}{platform.processor()}{end}')
    try:
        print('Architecture:', f'{yellow}{platform.architecture()[-1]}{end}')
    except:
        pass
    print('Platform:', f'{yellow}{platform.platform()}{end}')
    print('Version:', f'{yellow}{platform.version()}{end}')
    print('Node:', f'{yellow}{platform.node()}{end}')
    print('Computer Name:', f'{yellow}{get_env_var('COMPUTERNAME')}{end}')
    print('Username:', f'{yellow}{get_env_var('USERNAME')}{end}')
    print('User Profile:', f'{yellow}{get_env_var('USERPROFILE')}{end}')
    print('Appdata PATH:', f'{yellow}{get_env_var('APPDATA')}{end}')
    print('Local IP:', f'{yellow}{local_ip}{end}')
    if public_ip == 'None':
        pass
    else:
        print('Public IP:', f'{yellow}{public_ip}{end}')
    print(f"Uptime: {yellow}{days}d {hours}h {minutes}m {seconds}s")
    print()
    print(f'{cyan}═════════ : CPU INFOS : ═════════')
    try:
        print('CPU Architecture:', f'{yellow}{get_env_var('PROCESSOR_ARCHITECTURE')}{end}')
        print('CPU Identifier:', f'{yellow}{get_env_var('PROCESSOR_IDENTIFIER')}{end}')
        print('CPU Level:', f'{yellow}{get_env_var('OS')}{end}')
        print('CPU Revision:', f'{yellow}{get_env_var('OS')}{end}')
        print()
    except:
        pass
    print('CPU Count:', f'{yellow}{psutil.cpu_count()}{end}')
    print('CPU Current Frequency:', f'{green}{current_freq:.1f} GHz{end}')
    print('CPU Maximum Frequency:', f'{green}{max_freq:.1f} GHz{end}')
    print('CPU Minimum Frequency:', f'{red}{min_freq:.1f} GHz{end}')
    print()
    print('CPU Time User:', f'{green}{time_user:.2f} min{end}')
    print('CPU Time Sytem:', f'{green}{time_system:.2f} min{end}')
    print('CPU Time Idle:', f'{yellow}{time_idle:.2f} min{end}')
    print('CPU Time Interrupt:', f'{red}{time_interrupt:.2f} min{end}')
    print('CPU Time DPC:', f'{yellow}{time_dpc:.2f} min{end}')
    print()
    print(f'{cyan}═════════ : RAM INFOS : ═════════')
    if ram_percent > 60:
        C = red
    else:
        C = green
    print('RAM Total:', f'{green}{ram_total:.2f} GB{end}')
    print('RAM Used:', f'{C}{ram_used:.2f} GB{end}')
    print('RAM Available:', f'{C}{ram_available:.2f} GB{end}')
    print('RAM Usage:', f'{C}{ram_percent:.1f} %{end}')
    print()
    if memory_percent > 60:
        C = red
    else:
        C = green
    print('Virtual Memory Total:', f'{green}{memory_total:.2f} GB{end}')
    print('Virtual Memory Used:', f'{C}{memory_used:.2f} GB{end}')
    print('Virtual Memory Available:', f'{C}{memory_available:.2f} GB{end}')
    print('Virtual Memory Usage:', f'{C}{memory_percent:.1f} %{end}')
    print()
    print(f'{cyan}═════════ : DISK INFOS : ═════════')
    if usage_percent > 70:
        C = red
    else:
        C = green
    print('Disk Total Space:', f'{green}{usage_total:.2f} GB{end}')
    print('Disk Used Space:', f'{C}{usage_used:.2f} GB{end}')
    print('Disk Free Space:', f'{C}{usage_free:.2f} GB{end}')
    print('Disk Usage:', f'{C}{usage_percent:.1f} %{end}')
    print()
    print('Disk IO Read Count:', f'{yellow}{read_count} Times{end}')
    print('Disk IO Read Bytes:', f'{yellow}{read_bytes:.2f} GB{end}')
    print('Disk IO Read Time:', f'{yellow}{read_time:.2f} s{end}')
    print('Disk IO Write Count:', f'{yellow}{write_count} Times{end}')
    print('Disk IO Write Bytes:', f'{yellow}{write_bytes:.2f} GB{end}')
    print('Disk IO Write Time:', f'{yellow}{write_time:.2f} s{end}')
    
def infos_loop():
    while True:
        os.system('cls')
        get_all_infos()
        print()
        print(f'{red}[!] Press ENTER to go back.')
        print(f'{green}[?] Press ANY OTHER KEY to refresh the values.')
        clear_buffer()

        key = msvcrt.getch()
        if key == b'\r':
            break
        elif key != b'\r':
            continue
