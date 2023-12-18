import subprocess
from dataclasses import dataclass

from .printing import print


@dataclass
class PortSpec:
    local_host: str
    local_port: int
    remote_host: str
    remote_port: int

    @classmethod
    def parse(cls, text: str) -> "PortSpec":
        parts = text.split(":")
        if len(parts) == 1:
            (port,) = parts
            return PortSpec(
                local_host="localhost",
                local_port=int(port),
                remote_host="localhost",
                remote_port=int(port),
            )
        elif len(parts) == 2:
            local_port, remote_port = parts
            return PortSpec(
                local_host="localhost",
                local_port=int(local_port),
                remote_host="localhost",
                remote_port=int(remote_port),
            )
        elif len(parts) == 3:
            local_port, remote_host, remote_port = parts
            return PortSpec(
                local_host="localhost",
                local_port=int(local_port),
                remote_host=remote_host,
                remote_port=int(remote_port),
            )
        elif len(parts) == 4:
            local_host, local_port, remote_host, remote_port = parts
            return PortSpec(
                local_host=local_host,
                local_port=int(local_port),
                remote_host=remote_host,
                remote_port=int(remote_port),
            )
        else:
            raise ValueError(f"Invalid port spec: {text}")

    def to_tuple(self) -> tuple[str, int, str, int]:
        return (self.local_host, self.local_port, self.remote_host, self.remote_port)

    def to_ssh_arg(self) -> str:
        parts: list[str] = []
        if self.local_host != "localhost":
            parts.append(self.local_host)
        parts.append(str(self.local_port))
        parts.append(self.remote_host)
        parts.append(str(self.remote_port))
        return ":".join(parts)


def exec_ssh_cmd(
    *args: str, check: bool = True, **kwargs
) -> subprocess.CompletedProcess[str]:
    print(f"[not bold dim grey89]> ssh {' '.join(args)}")
    return subprocess.run(["ssh", *args], check=check, **kwargs)


def open_tunnel(ssh_host: str, *specs: str) -> None:
    port_specs = [PortSpec.parse(spec) for spec in specs]

    print(f"Making services from SSH host [cyan bold]{ssh_host}[/] available locally")

    ssh_args = []
    ssh_args.extend(["-N", "-T"])
    for spec in port_specs:
        ssh_args.extend(["-L", spec.to_ssh_arg()])
    ssh_args.append(ssh_host)

    exec_ssh_cmd(*ssh_args)
