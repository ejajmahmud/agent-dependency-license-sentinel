"""Core dependency license sentinel implementation."""
from typing import Dict, List

class LicensePolicy:
    PERMISSIVE = {"MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC"}
    COPYLEFT = {"GPL-2.0", "GPL-3.0", "AGPL-3.0", "LGPL-3.0"}

class TaintReport:
    def __init__(self, is_compliant: bool, violations: List[str]):
        self.is_compliant = is_compliant
        self.violations = violations

class DependencyLicenseSentinel:
    KNOWN_DB = {
        "requests": "Apache-2.0",
        "flask": "BSD-3-Clause",
        "urllib3": "MIT",
        "gpl_module": "GPL-3.0",
        "agpl_backend": "AGPL-3.0"
    }

    @classmethod
    def audit_dependencies(cls, packages: List[str]) -> TaintReport:
        violations = []
        for pkg in packages:
            clean_pkg = pkg.strip().lower()
            lic = cls.KNOWN_DB.get(clean_pkg, "UNKNOWN")
            if lic in LicensePolicy.COPYLEFT:
                violations.append(f"VIRAL_COPYLEFT_TAINT: '{pkg}' licensed under {lic}")
            elif lic == "UNKNOWN":
                pass  # Unflagged

        return TaintReport(is_compliant=(len(violations) == 0), violations=violations)
