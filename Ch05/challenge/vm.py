"""
Use a dataclass, write a VM class that has the following fields:
- id: str, no default
- cpus: int, default to 2
- memory: int, default to 512 (in MB)
- state: one of 'starting', 'running', 'stopped'
- tags: list of str, default to empty

After the VM is created, check that
- id is not empty
- cpus >= 1
- memory >= 256
"""
# %% Creating class
from dataclasses import dataclass, field

@dataclass
class VM:
    id: str
    cpus: int = 2
    memory: int = 512
    states: tuple[str, str, str] = ('starting', 'running', 'stopped')
    tags: list[str] = field(default_factory=list)

    #with pos_init
    def __post_init__(self):
        if not self.id:
            raise ValueError("Empty id")
        if self.cpus < 1:
            raise ValueError(f"Number of cpus is: ({self.cpus})  < 1")
        if self.memory < 256:
            raise ValueError(f"cpu memory not enough: ({self.memory}) < 256")



# %% test
vm = VM(
    id='i-0af01c0123456789a',
    cpus=4,
    memory=2048,
    tags=['db', 'env:qa']
)
print(vm)

# %% check
print('id is null:', vm.id == None)
print('cpus >= 1:', vm.cpus >= 1)
print('memory >= 256:', vm.memory >= 256)
# %% check the wrong vm
vm2 = VM(
    id='',
    cpus=4,
    memory=2048,
    tags=['db', 'env:qa']
)
print(vm2)

# %%
vm3 = VM(
    id='hdojl-12bnk',
    cpus=1,
    memory=112,
    tags=['db', 'env:qa']
)
print(vm3)
# %%
