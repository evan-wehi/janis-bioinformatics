from .base import Gatk4GatherVcfsBase
from .base_compressed import Gatk4GatherCompressedVcfsBase
from ..versions import Gatk_4_0_12, Gatk_4_1_2_0, Gatk_4_1_3_0, Gatk_4_1_4_0


class Gatk4GatherVcfs_4_0(Gatk_4_0_12, Gatk4GatherVcfsBase):
    pass


class Gatk4GatherVcfs_4_1_2(Gatk_4_1_2_0, Gatk4GatherVcfsBase):
    pass


class Gatk4GatherVcfs_4_1_3(Gatk_4_1_3_0, Gatk4GatherVcfsBase):
    pass


class Gatk4GatherVcfs_4_1_4(Gatk_4_1_4_0, Gatk4GatherVcfsBase):
    pass


class Gatk4GatherCompressedVcfs_4_0(Gatk_4_0_12, Gatk4GatherCompressedVcfsBase):
    pass


class Gatk4GatherCompressedVcfs_4_1_2(Gatk_4_1_2_0, Gatk4GatherCompressedVcfsBase):
    pass


class Gatk4GatherCompressedVcfs_4_1_3(Gatk_4_1_3_0, Gatk4GatherCompressedVcfsBase):
    pass


class Gatk4GatherCompressedVcfs_4_1_4(Gatk_4_1_4_0, Gatk4GatherCompressedVcfsBase):
    pass


Gatk4GatherVcfsLatest = Gatk4GatherVcfs_4_1_4
Gatk4GatherCompressedVcfsLatest = Gatk4GatherCompressedVcfs_4_1_4
