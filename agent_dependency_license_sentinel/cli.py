"""CLI for agent-dependency-license-sentinel."""
import argparse
import sys
from .core import DependencyLicenseSentinel

def main():
    parser = argparse.ArgumentParser(description="Agent Dependency License Sentinel CLI")
    parser.add_argument("--demo", action="store_true", help="Run license sentinel demo")
    args = parser.parse_args()

    if args.demo:
        packages = ["requests", "flask", "gpl_module"]
        rep = DependencyLicenseSentinel.audit_dependencies(packages)
        print(f"[+] Audited packages: {packages}")
        print(f"[+] Compliant: {rep.is_compliant}")
        for v in rep.violations:
            print(f"    - {v}")
    else:
        parser.print_help()
    sys.exit(0)

if __name__ == "__main__":
    main()
