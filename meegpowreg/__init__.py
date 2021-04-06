# Authors: David Sabbagh <david@sabbagh.fr>
#
# License: MIT
"""M/EEG power regression pipelines in Python"""

# PEP0440 compatible formatted version, see:
# https://www.python.org/dev/peps/pep-0440/
#
# Generic release markers:
#   X.Y
#   X.Y.Z   # For bugfix releases
#
# Admissible pre-release markers:
#   X.YaN   # Alpha release
#   X.YbN   # Beta release
#   X.YrcN  # Release Candidate
#   X.Y     # Final release
#
# Dev branch marker is: 'X.Y.devN' where N is an integer.
#

__version__ = '0.1.dev'

from .featuring import Riemann, Diag, LogDiag, ExpandFeatures, NaiveVec, RiemannSnp  # noqa

from .pipelines import make_pipelines  # noqa

from .power_features import compute_features  # noqa

from .spfiltering import ProjIdentitySpace, ProjCommonSpace, ProjLWSpace, ProjRandomSpace, ProjSPoCSpace  # noqa
