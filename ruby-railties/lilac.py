
from lilaclib import *

def pre_build():
  update_pkgver_and_pkgrel(_G.newver)
  add_depends(["ruby-method_source"])

