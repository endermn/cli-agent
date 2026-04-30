import psutil

from typing import Any

from .interfaces import Tool

from tools.tool_utils import logger

class SystemHealthTool(Tool):
    @property
    def name(self) -> str:
        return "system_health_tool"

    @property
    def description(self) -> str:
        return "returns the health of the system (memory usage, disk usage...)"

    def get_system_health(self) -> dict[str, Any]:
        logger.info("Tool 'get_system_health' called")
        cpu_percent = psutil.cpu_percent(interval=1)

        mem = psutil.virtual_memory()
        mem_total = mem.total
        mem_available = mem.available
        mem_used = mem.used
        mem_percent = mem.percent

        disk = psutil.disk_usage("/")
        disk_total = disk.total
        disk_used = disk.used
        disk_free = disk.free
        disk_percent = disk.percent

        net_io = psutil.net_io_counters()
        bytes_sent = net_io.bytes_sent
        bytes_recv = net_io.bytes_recv

        num_processes = len(psutil.Process().children()) + 1

        return {
            "cpu_percent": cpu_percent,
            "mem_total": mem_total,
            "mem_available": mem_available,
            "mem_used": mem_used,
            "mem_percent": mem_percent,
            "disk_total": disk_total,
            "disk_used": disk_used,
            "disk_free": disk_free,
            "disk_percent": disk_percent,
            "bytes_sent": bytes_sent,
            "bytes_recv": bytes_recv,
            "num_processes": num_processes,
        }
